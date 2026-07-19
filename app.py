import logging
from datetime import date, datetime

from flask import Flask, jsonify, request
from flask.json.provider import DefaultJSONProvider
from flask_cors import CORS

import settings
from core.postgres import ContentRepository


class ISOJSONProvider(DefaultJSONProvider):
    """
    Flask defaults to RFC 822 dates ('Sat, 12 Oct 2024 19:52:39 GMT'). ISO 8601
    is the friendlier contract for a JS front end, so timestamps go out as
    '2024-10-12T19:52:39+00:00'.
    """

    def default(self, o):
        if isinstance(o, datetime | date):
            return o.isoformat()

        return super().default(o)


app = Flask(__name__)
app.json = ISOJSONProvider(app)
CORS(app, origins=settings.CORS_ALLOWED_ORIGINS)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

repository = ContentRepository()


def error(message: str, status: int):
    return jsonify({'error': message}), status


def read_pagination() -> tuple[int, int]:
    """
    Parses limit/offset, clamping limit so a caller cannot pull the whole table
    in one request.
    """
    try:
        limit = int(request.args.get('limit', 50))
        offset = int(request.args.get('offset', 0))
    except ValueError:
        raise ValueError('limit and offset must be integers')

    if offset < 0:
        raise ValueError('offset must not be negative')

    return max(1, min(limit, 100)), offset


def list_content(kind: str | None):
    """
    Shared list handler. `kind` of None means every kind, newest first.
    """
    if kind is not None and kind not in settings.CONTENT_KINDS:
        return error(
            f'unknown kind {kind!r}, expected one of {", ".join(settings.CONTENT_KINDS)}',
            settings.HTTP_BAD_REQUEST,
        )

    try:
        limit, offset = read_pagination()
    except ValueError as exc:
        return error(str(exc), settings.HTTP_BAD_REQUEST)

    try:
        rows = repository.search(
            kind=kind,
            tag=request.args.get('tag'),
            limit=limit,
            offset=offset,
        )
    except Exception:
        # Logged with traceback so failures stay diagnosable, while the response
        # stays generic instead of leaking database internals.
        log.exception('content search failed')
        return error('could not retrieve content', settings.HTTP_SERVER_ERROR)

    return jsonify({'results': rows, 'count': len(rows)})


@app.route('/content', methods=['GET'])
def content_index():
    """
    GET /content?kind=article&tag=physics&limit=20&offset=0
    """
    return list_content(request.args.get('kind'))


@app.route('/content/<kind>/<slug>', methods=['GET'])
def content_detail(kind: str, slug: str):
    """
    GET /content/article/kinematics-in-one-dimension
    """
    if kind not in settings.CONTENT_KINDS:
        return error(f'unknown kind {kind!r}', settings.HTTP_BAD_REQUEST)

    try:
        row = repository.get_by_slug(kind, slug)
    except Exception:
        log.exception('content lookup failed for %s/%s', kind, slug)
        return error('could not retrieve content', settings.HTTP_SERVER_ERROR)

    if row is None:
        return error(f'no {kind} with slug {slug!r}', settings.HTTP_NOT_FOUND)

    return jsonify(row)


# Plain resource URLs for the front end; same handler, kind pinned.
@app.route('/articles', methods=['GET'])
def articles_index():
    return list_content('article')


@app.route('/projects', methods=['GET'])
def projects_index():
    return list_content('project')


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

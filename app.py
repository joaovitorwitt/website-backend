import logging

from flask import Flask
from flask import request

import psycopg
import settings

from entities.article import Article

from entities.base import BaseEntity



app = Flask(__name__)

# fix this
log = logging.getLogger(__name__)


@app.route("/get/articles", methods=['GET'])
def list_articles():
    pass

@app.route("/create/article", methods=['POST'])
def create_article():
    article_data = request.get_json()

    article = Article(
        title=article_data['title'],
        description=article_data['description'],
        content=article_data['content'],
        image_url=article_data['image_url']
    )

    with psycopg.connect(dbname='test-new-infra', user='postgres', password='barezia12', port=5432) as connection: # pylint: disable=not-context-manager
        with connection.cursor() as cur:
            cur.execute(
                'INSERT INTO "Articles" ("UUID", "Title", "Description", "created_at", "date", "Content", "image_url", "url_title") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (article.id, article.title, article.description, article.creation_time, article.date, article.content, article.image_url, article.url_title)
            )

            # cur.execute("SELECT * FROM Articles")
            # cur.fetchone()

            connection.commit()
            cur.close()
            connection.close()

    out = {
        'response': 'OK',
        'status_code': settings.HTTP_OK_REQUEST
    }

    # return a status code 200 and a message indicating that the article was created
    # json.dumps(article.__dict__)
    return out

@app.route("/delete/articles<id>")
def delete_article(id: int):
    pass

@app.route("/update/article/<id>")
def update_article(id: int):
    pass

@app.route("/get/article/<id>")
def list_single_articles(id: int):
    pass


# project endpoints
@app.route('/get/projects', methods=['GET'])
def list_projects():
    pass


@app.route('/get/project/<id>', methods=['GET'])
def list_project(id: int):
    pass


@app.route('/create/project', methods=['POST'])
def create_project():
    pass


@app.route('/delete/project/<id>', methods=['DELETE'])
def delete_project(id: int):
    pass


@app.route('/update/project/<id>', methods=['PUT'])
def update_project(id: int):
    pass

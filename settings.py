# pylint: disable=line-too-long

import os

from dotenv import load_dotenv

load_dotenv()

HTTP_OK_REQUEST = 200

HTTP_BAD_REQUEST = 400

# Supabase hands you a single connection string. When it is set it wins over the
# individual POSTGRES_* vars below, which stay around for a local postgres.
DATABASE_URL = os.environ.get('DATABASE_URL')

DEFAULT_POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
DEFAULT_POSTGRES_PORT = int(os.environ.get('POSTGRES_PORT', 5432))
DEFAULT_POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
DEFAULT_POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'password')
DEFAULT_POSTGRES_DB = os.environ.get('POSTGRES_DB', 'postgres')

# Supabase requires TLS; a local postgres normally does not have it configured.
POSTGRES_SSLMODE = os.environ.get('POSTGRES_SSLMODE', 'prefer')

# Each gunicorn worker builds its own pool, so the real ceiling against Supabase
# is POOL_MAX_SIZE * worker count. Keep both small.
POOL_MIN_SIZE = int(os.environ.get('POOL_MIN_SIZE', 1))
POOL_MAX_SIZE = int(os.environ.get('POOL_MAX_SIZE', 3))

# Supabase's transaction pooler (port 6543) cannot hold session-level prepared
# statements, so psycopg's automatic preparing has to be turned off there.
PREPARE_THRESHOLD = None if os.environ.get('USE_TRANSACTION_POOLER') else 5

CONTENT_KINDS = ('article', 'project')

HTTP_NOT_FOUND = 404

HTTP_SERVER_ERROR = 500

# Origins are matched against the browser's Origin header, which always carries
# a scheme, so bare hostnames never match. A leading '*' would also make every
# other entry here dead weight.
CORS_ALLOWED_ORIGINS = [
    'https://joaovitorwitt.com',
    'https://www.joaovitorwitt.com',
    'https://joaovitorwitt.pythonanywhere.com',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

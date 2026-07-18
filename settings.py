# pylint: disable=line-too-long

import os

from dotenv import load_dotenv

load_dotenv()

HTTP_OK_REQUEST = 200

HTTP_BAD_REQUEST = 400

# Supabase hands you a single connection string. When it is set it wins over the
# individual POSTGRES_* vars below, which stay around for a local postgres.
DATABASE_URL = os.environ.get("DATABASE_URL")

DEFAULT_POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
DEFAULT_POSTGRES_PORT = int(os.environ.get("POSTGRES_PORT", 5432))
DEFAULT_POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
DEFAULT_POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "password")
DEFAULT_POSTGRES_DB = os.environ.get("POSTGRES_DB", "postgres")

# Supabase requires TLS; a local postgres normally does not have it configured.
POSTGRES_SSLMODE = os.environ.get("POSTGRES_SSLMODE", "prefer")

CORS_ALLOWED_ORIGINS = [
    "*",
    "joaovitorwitt.com",
    "www.joaovitorwitt.com",
    "localhost:3000",
    "127.0.0.1",
    "https://joaovitorwitt.pythonanywhere.com",
]

# pylint: disable=line-too-long

import os

HTTP_OK_REQUEST = 200

HTTP_BAD_REQUEST = 400

DEFAULT_POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "localhost")
DEFAULT_POSTGRES_PORT = int(os.environ.get("POSTGRES_PORT", 5432))
DEFAULT_POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
DEFAULT_POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "password")
DEFAULT_POSTGRES_DB = os.environ.get("POSTGRES_DB", "postgres")

CORS_ALLOWED_ORIGINS = [
    "*",
    "joaovitorwitt.com",
    "www.joaovitorwitt.com",
    "localhost:3000",
    "127.0.0.1",
    "https://joaovitorwitt.pythonanywhere.com",
]

# pylint: disable=line-too-long


HTTP_OK_REQUEST = 200 # request succeeded depending of the HTTP method.

HTTP_BAD_REQUEST = 400 # Server will not process the request due to some client error (wrong syntax, deceptive routing)

DEFAULT_POSTGRES_PORT=5432
DEFAULT_POSTGRES_USER='postgres'
DEFAULT_POSTGRES_PASSWORD='barezia12'

STANDARD_LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

CORS_ALLOWED_ORIGINS = ["*", "joaovitorwitt.com", "www.joaovitorwitt.com", "localhost:3000", "127.0.0.1", "https://joaovitorwitt.pythonanywhere.com"]

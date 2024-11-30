# pylint: disable=line-too-long

FRONT_END_DEVELOPMENT_URL='https://websitefront-git-dev-joaovitorwitts-projects.vercel.app/'
DOMAIN_NAME='https://joaovitorwitt.com'

###################################################
# Successful Responses
###################################################
HTTP_OK_REQUEST = 200 # request succeeded depending of the HTTP method.
HTTP_CREATED = 201 # Some resource was created, typically sent after a POST or a PUT request.

###################################################
# Client Error Responses
###################################################
HTTP_BAD_REQUEST = 400 # Server will not process the request due to some client error (wrong syntax, deceptive routing)
HTTP_UNAUTHORIZED = 401 # client must be authenticated in order to retrieve the response
HTTP_FORBIDDEN = 403 # client does not have access rights to the content, the identity of the client is known
HTTP_NOT_FOUND = 404 # client cannot find the requested resource, maybe invalid endpoint or wrong browser URL.
HTTP_TOO_MANY_REQUESTS = 429 # client has sent too many requests in a given amount of time.

###################################################
# Server Error Responses
###################################################
HTTP_INTERNAL_SERVER_ERROR = 500 # server encountered a situation it does not know how to handle.

###################################################
# database stuff
###################################################
DEFAULT_POSTGRES_PORT=5432
DEFAULT_POSTGRES_USER='postgres'
DEFAULT_POSTGRES_PASSWORD='barezia12'

###################################################
#  logging stuff
###################################################
STANDARD_LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

###################################################
#  cors
###################################################
CORS_ALLOWED_ORIGINS = ["*", "joaovitorwitt.com", "www.joaovitorwitt.com", "localhost:3000", "127.0.0.1", "https://joaovitorwitt.pythonanywhere.com"]

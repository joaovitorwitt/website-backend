# pylint: disable=line-too-long
PYTHON_VERSION='3.11.7'

# Database configuration
DATABASE_NAME='website_backend_0fvg'
DATABASE_USER='website_backend_0fvg_user'
DATABASE_PASSWORD='-4DfgdeGBDFDFg*d2eG2cCGF*6F2*bE2'
DATABASE_HOST='dpg-cma3qpi1hbls73ci605g-a.oregon-postgres.render.com'
DATABASE_PORT='5432'



API_URL = 'https://portfolio-backend-fdxe.onrender.com'
DATABASE_URL= 'postgres://website_backend_0fvg_user:aL7a9VkJTAXsEXJbMcs89hrY55k1Xd1k@dpg-cma3qpi1hbls73ci605g-a.oregon-postgres.render.com/website_backend_0fvg'


FRONT_END_DEVELOPMENT_URL='https://websitefront-git-dev-joaovitorwitts-projects.vercel.app/'
PRODUCTION_URL='https://joaovitorwitt.com'


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

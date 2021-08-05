#--------- Flask settings
from os import environ

HOST = environ.get('SERVER_HOST', 'localhost')
try:
    PORT = int(environ.get('SERVER_PORT', '8000'))
except ValueError:
    PORT = 8000

FLASK_DEBUG = True # Do not use debug mode in prod

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

#-------- Azure constants

# API_URL format: "https://[FUNCTION_APP_NAME_GOES_HERE].azurewebsites.net"
#API_URL = " https://neighborlyapi.azurewebsites.net/api/"

# for local host if Azure functions served locally
API_URL = "https://neighborly-app-udacity-api.azurewebsites.net/api/"

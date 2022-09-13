from flask import Flask
from decouple import config

# creating flask app and specifying the html/css file locations
app = Flask(__name__,
            template_folder='www/templates',
            static_folder='www/static')

# adding a secret key
app.secret_key = config('SECRET_KEY')

from wikipedia_app import routes
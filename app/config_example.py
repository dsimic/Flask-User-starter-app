import os

# *****************************
# Environment specific settings
# *****************************

# The settings below can (and should) be over-ruled by OS environment
# variable settings

# Flask settings
# Generated with: import os; os.urandom(24)
SECRET_KEY = '\x96\xb5\xe7\x81\xfa\xa1\t\xc7\xe2\x88\xa4\x89\x06\x08' +\
    '\x07\xe7\xf3\x8fwI2\xa2'
# PLEASE USE A DIFFERENT KEY FOR PRODUCTION ENVIRONMENTS!

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.sqlite'

APP_NAME = "MyApp"

# Flask-Mail settings
MAIL_USERNAME = os.getenv(
    APP_NAME + "MAIL_USERNAME", 'email@example.com')
MAIL_PASSWORD = os.getenv(
    APP_NAME + "MAIL_PASSWORD", 'password')
MAIL_DEFAULT_SENDER = '%s <noreply@example.com>' % APP_NAME
MAIL_SERVER = os.getenv(
    APP_NAME + "MAIL_SERVER", 'smtp.gmail.com')
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True

ADMINS = [
    '"Admin One" <admin1@gmail.com>',
    ]

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

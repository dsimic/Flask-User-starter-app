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

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
DEBUG = True


# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(BASE_DIR, 'app.sqlite')

print SQLALCHEMY_DATABASE_URI

from app.startup.common_settings import APP_NAME

# Flask-Mail settings
MAIL_USERNAME = "admin@example.com"
MAIL_PASSWORD = "Password1"
MAIL_DEFAULT_SENDER = '%s <admin@example.com>' % APP_NAME
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True

ADMINS = [
    '"Admin One" <admin1@example.com>',
    ]

# Initial users by role
APP_USER_ADMINS = [
    ('Bob', 'Admin', 'admin@example.com', 'Password1'),
]
APP_USER_REGULAR = [
    ('Julie', 'User', 'user@example.com', 'Password1'),
]

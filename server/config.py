import logging
import os
from dotenv import load_dotenv
import tempfile


class EnvironmentConfig:
    """ Base class for configuration. """
    """ Most settings can be defined through environment variables. """

    # Load configuration from file
    load_dotenv(os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'tasking-manager.env')))

    # The base url the application is reachable
    APP_BASE_URL = os.getenv('TM_APP_BASE_URL', 'http://127.0.0.1:5000')

    # The default tag used in the OSM changeset comment
    DEFAULT_CHANGESET_COMMENT = os.getenv('TM_DEFAULT_CHANGESET_COMMENT', None)

    # The address to use as the sender on auto generated emails
    EMAIL_FROM_ADDRESS = os.getenv('TM_EMAIL_FROM_ADDRESS', None)

    # A freely definable secret key for connecting the front end with the back end
    SECRET_KEY = os.getenv('TM_SECRET', None)

    # Database connection
    POSTGRES_USER = os.getenv('POSTGRES_USER', None)
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', None)
    POSTGRES_ENDPOINT = os.getenv('POSTGRES_ENDPOINT', 'postgresql')
    POSTGRES_DB = os.getenv('POSTGRES_DB', None)
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')

    # Assamble the database uri
    if os.getenv('TM_DB', False):
        SQLALCHEMY_DATABASE_URI = os.getenv('TM_DB', None)
    else:
        SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}' +  \
                                        f':{POSTGRES_PASSWORD}' + \
                                            f'@{POSTGRES_ENDPOINT}:' + \
                                                f'{POSTGRES_PORT}' + \
                                                    f'/{POSTGRES_DB}'

    # Logging settings
    LOG_LEVEL = os.getenv('TM_LOG_LEVEL', logging.DEBUG)
    LOG_DIR = os.getenv('TM_LOG_DIR', 'logs')

    # Mapper Level values represent number of OSM changesets
    MAPPER_LEVEL_INTERMEDIATE = os.getenv('TM_MAPPER_LEVEL_INTERMEDIATE', 250)
    MAPPER_LEVEL_ADVANCED = os.getenv('TM_MAPPER_LEVEL_ADVANCED', 500)

    # Time to wait until task auto-unlock (e.g. '2h' or '7d' or '30m' or '1h30m')
    TASK_AUTOUNLOCK_AFTER = os.getenv('TM_TASK_AUTOUNLOCK_AFTER', '2h')

    # Where the additional project files are stored. Defaults to a temporary directory
    PROJECT_FILES_DIR = os.getenv('PROJECT_FILES_DIR', tempfile.gettempdir())

    # Image sources
    MAPILLARY_API = {'base': 'https://a.mapillary.com/v3/', 'clientId': os.getenv('MAPILLARY_API_KEY', None)}
    MAPILLARY_TIME_CORRELATION = os.getenv('MAPILLARY_TIME_CORRELATION', 60)

    # Configuration for sending emails
    SMTP_SETTINGS = {
        'host': os.getenv('TM_SMTP_HOST', None),
        'smtp_user': os.getenv('TM_SMTP_USER', None),
        'smtp_port': os.getenv('TM_SMTP_PORT', 25),
        'smtp_password': os.getenv('TM_SMTP_PASSWORD', None),
    }

    # Languages offered by the Tasking Manager
    # Please note that there must be exactly the same number of Codes as languages.
    SUPPORTED_LANGUAGES = {
        'codes': os.getenv('TM_SUPPORTED_LANGUAGES_CODES', 'ar, cs, da, de, en, es, fa_IR, fi, fr, hu, gl, id, it, ja, ko, lt, mg, nb, nl_NL, pl, pt, pt_BR, ru, si, sl, ta, uk, vi, zh_TW'),
        'languages': os.getenv('TM_SUPPORTED_LANGUAGES', 'Arabic, Česky, Dansk, Deutsch, English, Español, Persian (Iran), Suomi, Français, Magyar, Galician, Indonesia, Italiano, 日本語, 한국어, Lietuvos, Malagasy, Bokmål, Nederlands, Polish, Português, Português (Brasil), Русский, සිංහල, Slovenščina, தமிழ், Українська, tiếng Việt, 中文')
    }

    # Connection to OSM authentification system
    OSM_OAUTH_SETTINGS = {
        'base_url': 'https://www.openstreetmap.org/api/0.6/',
        'consumer_key': os.getenv('TM_CONSUMER_KEY', None),
        'consumer_secret': os.getenv('TM_CONSUMER_SECRET', None),
        'request_token_url': 'https://www.openstreetmap.org/oauth/request_token',
        'access_token_url': 'https://www.openstreetmap.org/oauth/access_token',
        'authorize_url': 'https://www.openstreetmap.org/oauth/authorize'
    }

    # Some more definitions (not overridable)
    API_DOCS_URL = f'{APP_BASE_URL}/api/docs'
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_MAX_OVERFLOW = 10
    SECRET_KEY = os.getenv('TM_SECRET', None)
    SMTP_SETTINGS = {
        'host': os.getenv('TM_SMTP_HOST', None),
        'smtp_user': os.getenv('TM_SMTP_USER', None),
        'smtp_port': os.getenv('TM_SMTP_PORT', 25),  # GMail SMTP is over port 587 and will fail on the default port
        'smtp_password': os.getenv('TM_SMTP_PASSWORD', None),
    }
    # Note that there must be exactly the same number of Codes as languages, or errors will occur
    SUPPORTED_LANGUAGES = {
        'codes': 'ar, cs, da, de, en, es, fr, hu, id, it, ja, lt, mg, nb, nl_NL, pl, pt, pt_BR, ru, si, sl, ta, uk, zh_TW',
        'languages': 'Arabic, Česky, Dansk, Deutsch, English, Español, Français, Magyar, Indonesia, Italiano, 日本語, Lietuvos, Malagasy, Bokmål, Nederlands, Polish, Português, Português (Brasil), Русский, සිංහල, Slovenščina, தமிழ், Українська, 中文'
    }
    PROJECT_FILES_DIR = './server/project_files'
    MAPILLARY_API = {
        "base": "https://a.mapillary.com/v3/",
        "clientId": "LVZRT2ZMZkl5RFpGZFp3NzZKaGhaQTpmMGVmNDU1NDI0NmI2YjNm"
    }


class ProdConfig(EnvironmentConfig):
    APP_BASE_URL = 'https://tasks.kaart.com'
    API_DOCS_URL = f'{APP_BASE_URL}/api-docs/swagger-ui/index.html?' + \
                   f'url={APP_BASE_URL}/api/docs'
    LOG_DIR = '/var/log/tasking-manager-logs'
    LOG_LEVEL = logging.ERROR


class StageConfig(EnvironmentConfig):
    APP_BASE_URL = 'https://tasks-stage.kaart.com'
    API_DOCS_URL = f'{APP_BASE_URL}/api-docs/swagger-ui/index.html?' + \
                   f'url={APP_BASE_URL}/api/docs'
    LOG_DIR = '/var/log/tasking-manager-stage-logs'
    LOG_LEVEL = logging.DEBUG


class DemoConfig(EnvironmentConfig):
    APP_BASE_URL = 'https://tasks-demo.hotosm.org'
    API_DOCS_URL = f'{APP_BASE_URL}/api-docs/swagger-ui/index.html?' + \
                   f'url={APP_BASE_URL}/api/docs'
    LOG_DIR = '/var/log/tasking-manager-logs'
    LOG_LEVEL = logging.DEBUG


class StagingConfig(EnvironmentConfig):
    # Currently being used by Thinkwhere
    APP_BASE_URL = 'http://tasking-manager-staging.eu-west-1.elasticbeanstalk.com'
    API_DOCS_URL = f'{APP_BASE_URL}/api-docs/swagger-ui/index.html?' + \
                   f'url={APP_BASE_URL}/api/docs'
    LOG_DIR = '/var/log/tasking-manager-logs'
    LOG_LEVEL = logging.DEBUG


class DevConfig(EnvironmentConfig):
    APP_BASE_URL = 'http://127.0.0.1:5000'
    API_DOCS_URL = f'{APP_BASE_URL}/api-docs/swagger-ui/index.html?' + \
                   f'url={APP_BASE_URL}/api/docs'
    LOG_DIR = 'logs'
    LOG_LEVEL = logging.DEBUG


class DevIPv6Config(EnvironmentConfig):
    APP_BASE_URL = 'http://[::1]:5000'
    API_DOCS_URL = f'{APP_BASE_URL}/api-docs/swagger-ui/index.html?' + \
                   f'url={APP_BASE_URL}/api/docs'
    LOG_DIR = 'logs'
    LOG_LEVEL = logging.DEBUG

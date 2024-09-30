import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Remove fallback values for sensitive data and fail if they are not set
    SECRET_KEY = os.getenv('SECRET_KEY')  
    DB_NAME = os.getenv('DB_NAME')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    
    # You can retain defaults for non-sensitive paths or settings
    UPLOADS = os.getenv('UPLOADS', '/home/username/app/app/static/uploads')
    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

    # Optionally, check if critical variables are missing and raise an error
    if not SECRET_KEY or not DB_NAME or not DB_USERNAME or not DB_PASSWORD:
        raise ValueError("Missing essential environment variables! Ensure SECRET_KEY, DB_NAME, DB_USERNAME, and DB_PASSWORD are set.")

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class DebugConfig(Config):
    DEBUG = False

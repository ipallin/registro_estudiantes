import os
from dotenv import load_dotenv

# Load .env
load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    DEBUG = os.environ.get('DEBUG', default='').upper() in ['TRUE','YES','1']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = (f"postgresql://{os.getenv('DB_USER') or 'db_user'}:"
                                            f"{os.getenv('DB_PASSWORD') or 'db_p4ssw0rd'}@"
                                            f"{os.getenv('DB_HOST') or 'localhost'}/"
                                            f"{os.getenv('DB_NAME') or 'studentRecord'}")
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    ENV = 'development'

class TestingConfig(Config):
    TESTING = True
    ENV = 'testing'


class ProductionConfig(Config):
    ENV = 'production'


config = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig,
    default=DevelopmentConfig
)

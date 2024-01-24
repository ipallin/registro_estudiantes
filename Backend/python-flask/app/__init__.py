from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

from config import config

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name):
    """Construct the core app object."""
    app = Flask(__name__)

    # Application Configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Database
    db.init_app(app)
    ma.init_app(app)


    # Blueprint register and db creation
    with app.app_context():
        from .controllers.StudentRecord import student_bp
        from .controllers.healthcheck import healthcheck_bp
        from .controllers.errors import errors_bp
        db.create_all()
        app.register_blueprint(student_bp, url_prefix='/api/StudentRecords')
        app.register_blueprint(healthcheck_bp, url_prefix='/healthcheck')
        app.register_blueprint(errors_bp)

    return app

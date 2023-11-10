from flask import Flask

from .config import Config
from .extensions import db, bcrypt

def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="/static")

    app.config.from_object(Config)
    app.config["DATABASE"] = "testing.db"
    
    db.init_app(app)
    bcrypt.init_app(app)

    from starterProject.main.routes import main
    app.register_blueprint(main, url_prefix="/")

    from starterProject.admin.routes import admin
    app.register_blueprint(admin, url_prefix="/portal")

    return app

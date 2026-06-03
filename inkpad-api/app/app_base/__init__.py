from flask import Flask
from database.db import Config, db, init_db

from app.app_menu.menu_models import Menu
from app.app_login.login_models import User

app = Flask(__name__)
app.config.from_object(Config)


def init_route():
    from app.app_index.index_route import bp as index_bp
    from app.app_menu.menu_route import bp as menu_bp
    from app.app_login.login_route import bp as login_bp

    app.register_blueprint(index_bp, url_prefix="/inkpad/index")
    app.register_blueprint(menu_bp, url_prefix="/inkpad/menu")
    app.register_blueprint(login_bp, url_prefix="/inkpad")


def first_run():
    init_route()
    init_db(app)


first_run()
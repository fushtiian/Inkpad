from app.app_menu.menu_models import Menu
from database.db import db


def get_all_menus():
    return Menu.query.order_by(Menu.sort_order).all()


def add_menu(name, sort_order=0):
    menu = Menu(name=name, sort_order=sort_order)
    db.session.add(menu)
    db.session.commit()
    return menu

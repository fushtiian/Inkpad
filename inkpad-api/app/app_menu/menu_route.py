from flask import Blueprint
from utils.response import success
from app.app_menu.menu_dao import get_all_menus

bp = Blueprint("menu", __name__)


@bp.route('/list')
def get_menu_list():
    menus = get_all_menus()
    return success([menu.to_dict() for menu in menus])


@bp.route('/seed')
def seed_menus():
    from app.app_menu.menu_dao import add_menu, get_all_menus
    if get_all_menus():
        return success(msg="already seeded")
    for name in ["Inkpad", "首页", "理论", "应用", "更多"]:
        add_menu(name)
    return success(msg="seed ok")


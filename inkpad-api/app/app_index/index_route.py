from flask import Blueprint
from utils.response import success

bp = Blueprint("index", __name__)


@bp.route('/')
def index():
    return success("Index Page!")


@bp.route('/index')
def get_info():
    return success("这里是首页！")

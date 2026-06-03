from flask import Blueprint, request
from utils.response import success, fail
from app.app_login.login_dao import create_user, get_user_by_username

bp = Blueprint("login", __name__)


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not username or not password:
        return fail("用户名和密码不能为空")

    if get_user_by_username(username):
        return fail("用户名已存在")

    # 暂不实现，后续接入api邮箱发送验证码
    print(email)

    user = create_user(username, password)
    return success(user.to_dict(), msg="注册成功")


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return fail("用户名和密码不能为空")

    user = get_user_by_username(username)
    if not user or user.password != password:
        return fail("用户名或密码错误")

    return success(user.to_dict(), msg="登录成功")

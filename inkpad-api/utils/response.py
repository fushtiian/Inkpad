from flask import jsonify


def success(data=None, msg="success", code=200):
    return jsonify({"code": code, "data": data, "msg": msg})


def fail(msg="error", code=400, data=None):
    return jsonify({"code": code, "data": data, "msg": msg})

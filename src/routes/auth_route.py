from flask import Blueprint
from src.controllers.auth_controller import (
    login_controller,
    register_controller,
    get_user_by_id_controller,
    get_all_users_controller,
)

auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth_bp.route("/register", methods=["POST"])
def register():
    return register_controller()


@auth_bp.route("/login", methods=["POST"])
def login():
    return login_controller()

@auth_bp.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(id):
    return get_user_by_id_controller(id)

@auth_bp.route("/users", methods=["GET"])
def get_all_users():
    return get_all_users_controller()






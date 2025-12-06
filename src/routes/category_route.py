from flask import Blueprint
from src.controllers.category_controller import (
    get_all_categories_controller,
    get_category_controller,
    create_category_controller,
)

category_bp = Blueprint("category", __name__, url_prefix="/api/v1/categories")


@category_bp.route("/<string:id>", methods=["GET"])
def get_category(id):
    return get_category_controller(id)


@category_bp.route("/", methods=["GET"])
def get_all_categories():
    return get_all_categories_controller()


@category_bp.route("/", methods=["POST"])
def create_category():
    return create_category_controller()


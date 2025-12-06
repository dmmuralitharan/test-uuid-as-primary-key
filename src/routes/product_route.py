from flask import Blueprint
from src.controllers.product_controller import (
    get_all_products_controller,
    get_product_controller,
    create_product_controller,
)

product_bp = Blueprint("product", __name__, url_prefix="/api/v1/products")


@product_bp.route("/<string:id>", methods=["GET"])
def get_product(id):
    return get_product_controller(id)


@product_bp.route("/", methods=["GET"])
def get_all_products():
    return get_all_products_controller()


@product_bp.route("/", methods=["POST"])
def create_product():
    return create_product_controller()

from flask import jsonify, request
from src import db
from src.models.product_model import Product


def create_product_controller():
    data = request.get_json()

    name = data.get("name")
    desc = data.get("desc")

    if not name:
        return jsonify({"error": "Name is required"}), 400

    existing = Product.query.filter_by(name=name).first()
    if existing:
        return jsonify({"error": "Product name already exists"}), 409

    new_product = Product(name=name, desc=desc)

    db.session.add(new_product)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "Product created successfully",
                "data": {
                    "id": new_product.id,
                    "name": new_product.name,
                    "desc": new_product.desc,
                },
            }
        ),
        201,
    )


def get_all_products_controller():
    products = Product.query.all()
    result = [{"id": p.id, "name": p.name, "desc": p.desc} for p in products]
    return jsonify(result), 200


def get_product_controller(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    result = {"id": product.id, "name": product.name, "desc": product.desc}
    return jsonify(result), 200

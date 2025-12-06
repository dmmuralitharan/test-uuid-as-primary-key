from flask import jsonify, request
from src import db
from src.models.category_model import Category


def get_all_categories_controller():
    categories = Category.query.all()
    result = [{"id": c.id, "name": c.name, "desc": c.desc} for c in categories]
    return jsonify(result), 200


def get_category_controller(id):
    category = Category.query.get(id)
    if not category:
        return jsonify({"error": "Category not found"}), 404

    result = {"id": category.id, "name": category.name, "desc": category.desc}
    return jsonify(result), 200

def create_category_controller():
    data = request.get_json()

    name = data.get("name")
    desc = data.get("desc")

    if not name:
        return jsonify({"error": "Name is required"}), 400

    existing = Category.query.filter_by(name=name).first()
    if existing:
        return jsonify({"error": "Category name already exists"}), 409

    new_category = Category(
        name=name,
        desc=desc
    )

    db.session.add(new_category)
    db.session.commit()

    return jsonify({
        "message": "Category created successfully",
        "data": {
            "id": new_category.id,
            "name": new_category.name,
            "desc": new_category.desc
        }
    }), 201
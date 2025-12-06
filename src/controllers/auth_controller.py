import datetime
import bcrypt
from src import db
from flask import jsonify, request
from src.models.user_model import User
from src.utils.jwt import generate_jwt_token


def register_controller():

    try:

        data = request.get_json()

        username = data.get("username")
        password = data.get("password")
        role = data.get("role", "user")

        if User.query.filter_by(username=username).first():
            return jsonify({"msg": "User already exists", "success": 2})

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        new_user = User(
            username=username, password=hashed_password.decode("utf-8"), role=role
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"msg": "User registered successfully", "status": 1}), 201

    except Exception as e:
        db.session.rollback()
        return (jsonify({"success": 0, "error": str(e)}), 500)


def login_controller():

    try:

        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return (
                jsonify({"message": "Username and password required", "status": 0}),
                400,
            )

        user = User.query.filter_by(username=username).first()

        if not user or not bcrypt.checkpw(
            password.encode("utf-8"), user.password.encode("utf-8")
        ):
            return jsonify({"message": "Invalid credentials", "status": 0})

        additional_claims = {
            "user_id": user.id,
            "username": user.username,
            "role": user.role,
        }

        access_token = generate_jwt_token(user.id)
        db.session.commit()

        return (
            jsonify(
                {
                    "message": "Login successful",
                    "access_token": access_token,
                    "username": user.username,
                    "role": user.role,
                    "status": 1,
                }
            ),
            200,
        )

    except Exception as e:
        db.session.rollback()
        return (jsonify({"success": 0, "error": str(e)}), 500)


def get_all_users_controller():
    users = User.query.all()
    result = [{"id": u.id, "username": u.username, "role": u.role} for u in users]
    return jsonify(result), 200


def get_user_by_id_controller(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    result = {"id": user.id, "username": user.username, "role": user.role}

    return jsonify(result), 200

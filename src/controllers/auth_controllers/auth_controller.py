from datetime import timedelta

import bcrypt
from src import db
from flask import jsonify, request
from src.models.auth_models.user_model import User
from flask_jwt_extended import create_access_token


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
        if "MySQL server has gone away" in str(e):
            return register_controller()
        else:
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

        print(username, password)
        user = User.query.filter_by(username=username).first()
        print(user)

        if not user or not bcrypt.checkpw(
            password.encode("utf-8"), user.password.encode("utf-8")
        ):
            return jsonify({"message": "Invalid credentials", "status": 0})

        additional_claims = {
            "user_id": user.id,
            "username": user.username,
            "role": user.role,
        }

        # Generate JWT token
        access_token = create_access_token(
            identity=user.id,
            additional_claims=additional_claims,
            expires_delta=timedelta(days=1),
        )
        return jsonify(
            {
                "message": "Login successful",
                "token": access_token,
                "username": user.username,
                "role": user.role,
                "status": 1,
            }
        ), 200

    except Exception as e:
        db.session.rollback()
        if "MySQL server has gone away" in str(e):
            return login_controller()
        else:
            return (jsonify({"success": 0, "error": str(e)}), 500)

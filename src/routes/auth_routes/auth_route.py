from flask import Blueprint
from src.controllers.auth_controllers.auth_controller import login_controller, register_controller
from werkzeug.security import generate_password_hash, check_password_hash
from src import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Register route
@auth_bp.route('/register', methods=['POST'])
def register():
    return register_controller()


# Login route
@auth_bp.route('/login', methods=['POST'])
def login():
    return login_controller()




# additional_claims = {
#         'user_id': user_id,
#         'username': username
#     }
    
# # Generate the access token with custom claims and optional expiration
# access_token = create_access_token(
#     identity=user_id,  # Primary identity (often user_id)
#     additional_claims=additional_claims,  # Custom claims like username
#     expires_delta=timedelta(hours=1)  # Custom expiration time (1 hour in this case)
# )

# return jsonify(access_token=access_token), 200


# ---


# @app.route('/dashboard', methods=['GET'])
# @jwt_required()  # This route is protected by JWT authentication
# def dashboard():
#     jwt_data = get_jwt()  # Retrieve the current JWT claims
    
#     # Access custom claims
#     user_id = jwt_data.get('user_id')
#     username = jwt_data.get('username')

#     # Return the user info as a response
#     return jsonify(logged_in_as=username, user_id=user_id), 200

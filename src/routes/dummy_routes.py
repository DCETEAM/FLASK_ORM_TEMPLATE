from flask import Blueprint
from src.controllers.dummy_controller import *

dummy_bp = Blueprint("dummy", __name__, url_prefix="/dummy")


@dummy_bp.route("/", methods=["GET"])
def get_dummy():
    return get_dummy_controller()

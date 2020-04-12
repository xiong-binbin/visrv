from flask import Blueprint
from flask_restful import Resource, Api


main = Blueprint('main', __name__)
api = Api(main)

from . import views

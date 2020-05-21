from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with

from db import db
from model import UserModel

app_random = Blueprint('random', __name__)

resource_random = {
    "id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "dob": fields.String,
    "gender": fields.String
}


class Random(Resource):

    @marshal_with(resource_random)
    def get(self, value=None):
        if value:
            return UserModel.query.get_or_404(value)
        return UserModel.query.all()

    def delete(self, value):
        user = UserModel.query.get_or_404(value)
        db.session.delete(user)
        db.session.commit()
        return "User is deleted"


api = Api(app_random)
api.add_resource(Random, '/user', '/user/<value>')

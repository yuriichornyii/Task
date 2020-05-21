from db import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    # may consist more fields

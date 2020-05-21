from flask import Flask
from randomuser import RandomUser

from api import app_random
from db import db
from model import UserModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)
app.register_blueprint(app_random)


@app.before_first_request
def random_users():
    db.drop_all()
    db.create_all(app=app)
    users = RandomUser.generate_users(100, {'gender': 'male'})
    for user in users:
        user = UserModel(
            first_name=user.get_first_name(),
            last_name=user.get_last_name(),
            dob=user.get_dob(),
            gender=user.get_gender()
            # may add more fields(city, number ...)
        )
        db.session.add(user)
        db.session.commit()
    return app


if __name__ == '__main__':
    app.run(debug=True)

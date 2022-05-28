from flask import Flask
from models import *  # import file models.py previously created
 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:hien@localhost:5432/flight"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)  # tie db with flask app


def main():
    db.create_all()


if __name__ == "__main__":
    with app.app_context():  # allow developer interact with flask via command line
        main()

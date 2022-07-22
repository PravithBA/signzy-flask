import os
from flask import Flask, request
from dotenv import load_dotenv
from services.signzy import get_signzy_identity_object, signzy_login
import threading
from shared.models import db

load_dotenv()

# Login Thread - Checks if time passed everytime to login if passed
threading.Thread(target=signzy_login).start()
app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{os.environ['POSTGRES_USERNAME']}:{os.environ['POSTGRES_PASSWORD']}@0.0.0.0:5432/{os.environ['POSTGRES_DATABASE_NAME']}"
db.init_app(app)


class IdentityModel(db.Model):
    __tablename__ = "identity_signzy"

    identity_uuid = db.Column(db.BigInteger, unique=True, primary_key=True)
    identity_access_token = db.Column(db.String(), unique=True, nullable=False)
    identity_id = db.Column(db.String(), unique=True, nullable=False)

    def __init__(self, identity_uuid, identity_access_token, identity_id):
        self.identity_uuid = identity_uuid
        self.identity_access_token = identity_access_token
        self.identity_id = identity_id

    def __repr__(self):
        return f"<Identity {self.identity_id}>"


with app.app_context():
    db.create_all()


@app.get("/")
def main_route():
    try:
        print(os.environ["TIME_TILL_LOGOUT"])
    except:
        print("No env variable")
    return "Welcome"


@app.get("/signzy/verify")
def verification():
    request_query_paramerters = request.args
    request_body = request.data
    try:
        identity_type = request_query_paramerters["identity_type"]
    except:
        return {"msg": "Wrong url parameters"}, 400
    image_array = [
        "https://cdn.discordapp.com/attachments/840656221450010705/999562536854761482/IMG-20220701-WA0002.jpg"
    ]
    identity_object = get_signzy_identity_object(identity_type, "AAAA", images=image_array)
    return identity_object


if __name__ == "__main__":
    app.run(debug="1", host="0.0.0.0", port=7500)

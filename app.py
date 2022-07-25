import os
from flask import Flask, Response, request
from dotenv import load_dotenv
from services.signzy import (
    add_identity_to_database,
    get_signzy_identity_object,
    send_data_to_callback_url,
    signzy_login,
)
import threading
from shared.models import db
from flask_migrate import Migrate

load_dotenv()

# Login Thread - Checks if time passed everytime to login if passed
threading.Thread(target=signzy_login).start()
app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{os.environ['POSTGRES_USERNAME']}:{os.environ['POSTGRES_PASSWORD']}@0.0.0.0:5432/{os.environ['POSTGRES_DATABASE_NAME']}"
db.init_app(app)
Migrate(app, db)
with app.app_context():
    db.create_all()


@app.get("/")
def main_route():
    try:
        print(
            "\n------------------------------------------------------------------\n",
            os.environ["TIME_TILL_LOGOUT"],
            "\n------------------------------------------------------------------\n",
        )
    except:
        print(
            "\n------------------------------------------------------------------\n",
            "No env variable for time till logout",
            "\n------------------------------------------------------------------\n",
        )
    return "Welcome"


@app.post("/signzy/verify")
def verification():
    request_query_paramerters = request.args
    request_body = request.get_json()
    try:
        identity_type = request_query_paramerters["identity_type"]
    except:
        return Response({"msg": "Wrong url parameters"}, 400)
    image_array = request_body["imageArr"]
    identity_object = get_signzy_identity_object(identity_type, images=image_array)
    # 'add_identity_to_database' function returns status codes
    add_to_db_status_code = add_identity_to_database(identity_object)
    send_to_callback_response = send_data_to_callback_url(identity_object)
    print(send_to_callback_response.json())
    return Response(f"response {add_to_db_status_code}", add_to_db_status_code)


@app.post("/signzy/callback")
def call_back():

    return


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7500)

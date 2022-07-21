import os
from flask import Flask, request
from dotenv import load_dotenv
from services.signzy import get_signzy_identity_object, signzy_login
import threading

load_dotenv()

# Login Thread - Checks if time passed everytime to login if passed
threading.Thread(target=signzy_login).start()
app = Flask(__name__)


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

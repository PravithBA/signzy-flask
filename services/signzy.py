import os
from time import sleep, time
from sqlalchemy.exc import SQLAlchemyError
import requests
from utils.signzy import get_signzy_default_header, get_signzy_post_url, get_signzy_identity_body
from shared.models import db
from models.signzy import IdentityModel

SLQALCHEMY_PRIMARY_KEY_CONFLICT_ERROR_CODE = "gkpj"


def signzy_login():

    """Gets the authentication id and patreon id"""

    time_till_logout = -999.0
    while True:
        now = time()
        if time_till_logout > now and time_till_logout > 0:
            # sleep(1000)
            continue
        signzy_login_credentials = {
            "username": os.environ["SIGNZY_USERNAME"],
            "password": os.environ["SIGNZY_PASSWORD"],
        }
        url = get_signzy_post_url("patrons/login")
        login_response = requests.post(url, data=signzy_login_credentials)
        login_object = login_response.json()
        os.environ["SIGNZY_PATREON_ID"] = login_object["userId"]
        os.environ["SIGNZY_AUTHENTICATION_ID"] = login_object["id"]
        time_till_logout = now + login_object["ttl"]
        sleep(1000)


def get_signzy_identity_object(verification_type: str, images: list = []):

    """Gets the identity object from signzy"""

    url = get_signzy_post_url("identities", patreon_id=True)
    headers = get_signzy_default_header()
    request_body = get_signzy_identity_body(verification_type, images=images)
    identity_response = requests.post(url, headers=headers, data=request_body)
    identity_object = identity_response.json()
    return identity_object


def add_identity_to_database(identity_object: dict):

    identity_model = IdentityModel(
        identity_access_token=identity_object["accessToken"], identity_id=identity_object["id"]
    )
    try:
        db.session.add(identity_model)
        db.session.commit()
    except SQLAlchemyError as error:
        if error.code == SLQALCHEMY_PRIMARY_KEY_CONFLICT_ERROR_CODE:
            return 400
        return 500
    return 200


# def get_verification_object():
#     """Gets the verification object from signzy"""
#     return

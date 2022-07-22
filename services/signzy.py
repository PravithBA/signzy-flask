import os
from time import sleep, time
import requests
from utils.signzy import get_signzy_default_header, get_signzy_post_url, get_signzy_identity_body


def signzy_login():

    """Gets the authentication id and patreon id"""

    time_till_logout = -999.0
    while True:
        now = time()
        if time_till_logout > now and time_till_logout > 0:
            sleep(1000)
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


def get_signzy_identity_object(verification_type: str, signzy_uuid: str, images: list = []):

    """Gets the identity object from signzy"""

    url = get_signzy_post_url("identities", patreon_id=True)
    headers = get_signzy_default_header()
    request_body = get_signzy_identity_body(verification_type, signzy_uuid, images=images)
    identity_response = requests.post(url, headers=headers, data=request_body)
    identity_object = identity_response.json()
    return identity_object


# def get_verification_object():
#     """Gets the verification object from signzy"""
#     return

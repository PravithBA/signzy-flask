import json
import os


def get_signzy_default_header():

    """Gets the default header for signzy"""

    auth_id = os.environ["SIGNZY_AUTHENTICATION_ID"]
    return {"Content-Type": "application/json", "Authorization": f"{auth_id}"}


def get_signzy_post_url(url_patameter: str, patreon_id: bool = False):

    """Gets the url for the signzy post request"""

    if patreon_id:
        patreon_id = os.environ["SIGNZY_PATREON_ID"]
        return f"https://preproduction.signzy.tech/api/v2/patrons/{patreon_id}/{url_patameter}"
    return f"https://preproduction.signzy.tech/api/v2/{url_patameter}"


def get_signzy_extraction_request_body(service: str, task: str, item_id: str, access_token: str, essentials: dict = {}):

    """Gets the request body for extraction for signzy"""

    extraction_body = {
        "service": service,
        "itemId": item_id,
        "task": task,
        "accessToken": access_token,
        "essentials": essentials,
    }

    return json.parse(extraction_body)


def get_signzy_identity_body(verification_type: str, signzy_uuid: str, images: list = []):

    """Gets the request body for identity for signzy"""

    identity_body = {
        "type": verification_type,
        "email": os.environ["SIGNZY_EMAIL"],
        "callbackUrl": os.environ["SIGNZY_CALLBACK_URL"] + signzy_uuid,
        "images": images,
    }

    return json.dumps(identity_body)
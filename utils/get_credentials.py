import os
import requests as req


def get_signzy_default_header(auth_id: str):
    """A dummy docstring."""
    return {"Content-Type": "application/json", "Authorization": f"{auth_id}"}


def get_signzy_post_url(url_patameter: str, patreon_id: str = None):
    """Gets the url for the signzy post request"""
    if patreon_id:
        return f"https://preproduction.signzy.tech/api/v2/patrons/{patreon_id}/{url_patameter}"
    return f"https://preproduction.signzy.tech/api/v2/{url_patameter}"


def get_signzy_extraction_request_body(service: str, task: str, item_id: str, access_token: str, essentials: dict):
    """A dummy docstring."""
    return {
        "service": service,
        "itemId": item_id,
        "task": task,
        "accessToken": access_token,
        "essentials": essentials,
    }


def get_signzy_identity_body(verification_type: str, images: list):
    """A dummy docstring."""
    return {
        "type": verification_type,
        "email": os.environ["SIGNZY_EMAIL"],
        "callbackUrl": os.environ["SIGNZY_CALLBACK_URL"],
        "images": images,
    }


def get_identity_object(signzy_patreon_id: str, signzy_auth_id: str, verification_type: str, images: list):
    """A dummy docstring."""
    url = get_signzy_post_url("identities", signzy_patreon_id == signzy_patreon_id)
    headers = get_signzy_default_header(signzy_auth_id)
    request_body = get_signzy_identity_body(verification_type, images=images)
    identity_response = req.post(url, headers=headers, data=request_body)
    identity_object = identity_response.json()
    return identity_object

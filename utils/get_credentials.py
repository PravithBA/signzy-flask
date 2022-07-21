from array import array
import requests as req
import os

def get_signzy_default_header(auth_id:str):
    return {
        'Content-Type': 'application/json',
        'Authorization': f'{auth_id}'
    }

def get_signzy_post_url(url_patameter:str,patreon_id:str=None):
    if patreon_id != None:
        return f"https://preproduction.signzy.tech/api/v2/patrons/{patreon_id}/{url_patameter}"
    return f"https://preproduction.signzy.tech/api/v2/{url_patameter}"

def get_signzy_extraction_request_body(service:str,task:str,item_id:str,access_token:str,essentials:dict={}):
    return {
        'service':service,
        'itemId':item_id,
        'task':task,
        'accessToken':access_token,
        'essentials':essentials,
    }

def get_signzy_identity_body(type:str,images:array=[]):
    return {
        "type":type,
        "email":os.environ["SIGNZY_EMAIL"],
        "email":os.environ["SIGNZY_CALLBACK_URL"],
        "images":images,
    }

def get_identity_object(signzy_patreon_id:str,signzy_auth_id:str,verification_type:str,images:array=[]):
    url = get_signzy_post_url("identities",signzy_patreon_id==signzy_patreon_id)
    headers = get_signzy_default_header(signzy_auth_id)
    req_body = get_identity_object(verification_type,images=images)
    identity_response = req.post(url,headers=headers,data=req_body)
    identity_object = identity_response.json()
    return identity_object
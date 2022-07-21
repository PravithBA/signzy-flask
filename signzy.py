import json
import requests as req

#Login
print("\n----------\nLogin\n----------\n")

cred = {
    'username': 'getfinstack_test',
    'password': 'Zx5Dqp4Y47Yvbphrb7Nd'
}
login_res = req.post("https://preproduction.signzy.tech/api/v2/patrons/login",data=cred)
print(login_res.json())
login_res = login_res.json()
auth_token = login_res['id']
patreon_id = login_res['userId']

#Identity object
print("\n----------\nIdentity Object\n----------\n")

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'{auth_token}'
}

req_data = {
    "type": "aadhaar",
    "email": "pravith@getfinstack.in",
    "callbackUrl": f"https://your-domain.com/your-callback-system/{auth_token}",
    "images": [
        "https://cdn.discordapp.com/attachments/840656221450010705/999562536854761482/IMG-20220701-WA0002.jpg"
    ]
}
req_data = json.dumps(req_data)
identity_res = req.post(f"https://preproduction.signzy.tech/api/v2/patrons/{patreon_id}/identities",data=req_data,headers=headers)
print(identity_res.json())
identity_res = identity_res.json()
access_token = identity_res['accessToken']
identity_id = identity_res['id']

# Aadhar
print("\n----------\nAadhar\n----------\n")

req_data = {
    "service":"Identity",
    "itemId":f"{identity_id}",
    "task":"autoRecognition",
    "accessToken":f"{access_token}",
    "essentials":{}
}
headers = {
    'accept-language': "en-US,en;q=0.8",
    'accept': "*/*"
}
aadhar_res = req.post("https://preproduction.signzy.tech/api/v2/snoops",data=req_data,headers=headers)
print(aadhar_res.json())

# Vehicle registration
print("\n----------\nVehicle Registration\n----------\n")

headers =  {
    'Authorization': f'{auth_token}',
    'Content-type': 'application/json'
}
req_data = {
    "task" : "basicSearch",
    "essentials": {
        "vehicleNumber": "MH12GL3639"
    }
}
req_data = json.dumps(req_data)
vehicle_res = req.post(f"https://preproduction.signzy.tech/api/v2/patrons/{patreon_id}/vehicleregistrations",data=req_data,headers=headers)
print(vehicle_res.json())

#logout
print("\n----------\nLogout\n----------\n")

logout_res = req.post(f"https://preproduction.signzy.tech/api/v2/patrons/logout?access_token={auth_token}",data=cred)
print(logout_res)
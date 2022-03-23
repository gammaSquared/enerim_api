import pandas as pd
import requests
import json


def authenticate(usr, psw):
    """Use this function to retrieve token that is required in order to call the API"""
    url = "https://ems.enerim.com/ExternalData/Users/Authenticate"

    payload = json.dumps({
        "username": usr,
        "password": psw
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()['token']


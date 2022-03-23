import pandas as pd
import requests
import json

pd.read(    )
def authenticate(usr, psw):
    """
    Use this function to retrieve token that is required in order to call the API
    :param usr: str, username.
    :param psw: str, password.
    :return: str, a token that is use din order to make call to the API.
    """
    url = "https://ems.enerim.com/ExternalData/Users/Authenticate"

    payload = json.dumps({
        "username": usr,
        "password": psw
    })

    headers = { 'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()['token']


def get_datagroups(token):
    """
    The function retrieves the available datagroups for the current user.
    :param token: str, the token that is retrieved by authenticate().
    :return: str, list of str.
    """
    url = "https://ems.enerim.com/ExternalData/DataGroups

    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)




import pandas as pd
import requests
import json

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
    url = "https://ems.enerim.com/ExternalData/DataGroups"

    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }

    response = requests.request("GET", url, headers=headers)

    return json.loads(response.text)


def get_data_from_datagroup(datagroup, start, end):
    """
    :param datagroup: str, a datagroup that can be obtained by calling get_datagroups()
    :param start: str, format "2022-02-13T09:12:28Z"
    :param end: str, format "2022-02-14T09:12:28Z"
    :return:
    """
    url = "https://ems.enerim.com/ExternalData/DataGroups/{}?start={}&end={}".format(datagroup, start, end)

    headers = {'Authorization': 'Bearer {}'.format(token)}

    response = requests.request("GET", url, headers=headers)

    return (response.text)


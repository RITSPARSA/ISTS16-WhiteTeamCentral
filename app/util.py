"""
    File to hold utility functions
"""
import requests
from .config import (AUTH_API_URL, BANK_API_URL, AUTH_ENDPOINTS, SLACK_URI, 
                     CHANNEL, SLACK_USERNAME, ICON_EMOJI, BANK_ENDPOINTS,
                     SHIP_API_URL)
from .errors import RequestError, AuthError, APIConnectionError

def validate_session(token):
    """
    Sends token to auth server to validate, should recieve
    associated team number if it is valid

    :param token: the session token to validate

    :return team_id: the id of the team the token is attached to
    """
    post_data = dict()
    post_data['token'] = token
    resp = api_request('validate-session', post_data)
    if 'success' not in resp:
        raise AuthError(resp['error'])

    team_id = resp['success']
    return team_id

def api_request(endpoint, data=None, method='POST', token=None):
    """
    Makes a request to our api and returns the response

    :param endpoint: the api endpoint to hit
    :param data: the data to send in dictionary format

    :returns resp: the api response
    """
    if endpoint in AUTH_ENDPOINTS:
        url = "{}/{}".format(AUTH_API_URL, endpoint)
    elif endpoint in BANK_ENDPOINTS:
        url = "{}/{}".format(BANK_API_URL, endpoint)
    else:
        url = "{}/{}".format(SHIP_API_URL, endpoint)
    print url

    if method == 'POST':
        resp = requests.post(url, data=data)
    else:
        cookies = {'token': token}
        resp = requests.get(url, cookies=cookies)

    if resp.status_code == 400:
        raise RequestError("Bad request sent to API")

    if resp.status_code == 403:
        raise AuthError(resp.json()['error'])

    elif resp.status_code != 200:
        raise APIConnectionError("API returned {} for /{}".format(
            resp.status_code, endpoint))

    resp_data = resp.json()
    return resp_data

def validate_request(params, data):
    """
    Verifies all the required parameters are in the request

    :param params: an array of the required parameters
    :param data: the json data in the post request
    """
    for p in params:
        if p not in data:
            raise RequestError("Missing {}".format(p))

    return True

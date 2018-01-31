"""
    File to hold utility functions
"""
import requests
from .config import AUTH_API_URL, SLACK_URI, CHANNEL, SLACK_USERNAME, ICON_EMOJI
from .errors import RequestError, AuthError, TransactionError

def validate_session(token):
    """
    Sends token to auth server to validate, should recieve
    associated team number if it is valid

    :param token: the session token to validate

    :return team_id: the id of the team the token is attached to
    """
    post_data = dict()
    post_data['token'] = token
    resp = auth_api_request('validate-session', post_data)
    if 'success' not in resp:
        raise AuthError(resp['error'])

    team_id = resp['success']
    return team_id

def auth_api_request(endpoint, data):
    """
    Makes a request to our api and returns the response

    :param endpoint: the api endpoint to hit
    :param data: the data to send in dictionary format
    :param url: the url of the api

    :returns resp: the api response
    """
    print data
    url = "{}/{}".format(AUTH_API_URL, endpoint)

    resp = requests.post(url, data=data)
    if resp.status_code == 400:
        raise RequestError("Bad request sent to API")

    if resp.status_code == 403:
        raise AuthError(resp.json()['error'])

    elif resp.status_code != 200:
        raise RequestError("API returned {} for /{}".format(
            resp.status_code, endpoint))

    resp_data = resp.json()
    return resp_data
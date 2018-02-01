"""
Entry points for API calls
"""
from flask import request, jsonify, abort
from . import app, DB
from . import errors
from .models.planets import Planet
from .models.alerts import Alert
from .util import validate_session, api_request, validate_request
from .config import SECRET_KEY
"""
    Statuses
"""
@app.route("/status/alerts")
def alerts():
    """
    Endpoint to return and alerts we have

    :returns result: dict with array of dicts containing alert data
    """
    result = dict()
    result['alerts'] = []
    alerts = Alert.query.all()
    for alert in alerts:
        alert_dict = dict()
        alert_dict['alert_id'] = alert.uuid
        result['alerts'].append(alert_dict)

    return jsonify(result)

@app.route('/status/koth', methods=['GET'])
def koth():
    """
    Endpoint to return the status of KOTH, who owns what planet

    :returns result: dict with array of dicts containg planet_id and its owner
    """
    result = dict()
    result['planets'] = []
    planets = Planet.query.filter_by(status='started').all()
    for planet in planets:
        planet_dict = dict()
        planet_dict['planet'] = planet.name
        planet_dict['owner'] = planet.owner
        result['planets'].append(planet_dict)

    return jsonify(result)

"""
    Team Functions
"""
@app.route('/credits/<team_id>', methods=['POST'])
def get_credits(team_id):
    """
    Get the credits of a specific team

    :returns result: a dict containing the credits for the team
    """
    result = dict()
    data = request.form
    if data is None:
        data = request.get_json()
        if data is None:
            abort(400)

    # make sure we have all the correct parameters
    params = ['token']
    validate_request(params, data)

    token = data['token']
    # the way we send it is janky, need to trim some stuff
    token = token.replace("token=", "")

    # make request to credits api
    post_data = dict()
    post_data['token'] = token
    resp = api_request("get-balance", post_data)
    session_team_id = resp['team_id']
    # if the passed session is not for the team that was requested, raise error
    if int(session_team_id) != int(team_id):
        raise errors.RequestError("Can only make requests for your team")

    balance = resp['balance']
    result['credits'] = balance
    return jsonify(result)

@app.route('/stats/<team_id>', methods=['POST'])
def get_perks(team_id):
    """
    Get the current perks for a team

    :returns result: a dict containg each perk and its status
    """
    result = dict()
    data = request.form
    if data is None:
        data = request.get_json()
        if data is None:
            abort(400)

    # make sure we have all the correct parameters
    params = ['token']
    validate_request(params, data)

    token = data['token']
    # the way we send it is janky, need to trim some stuff
    token = token.replace("token=", "")

    resp = api_request("teams/{}".format(team_id), method='GET', token=token)
    result['health'] = resp['health']
    result['damage'] = resp['damage']
    result['speed'] = resp['speed']
    return jsonify(result)

@app.route('/ships/<team_id>', methods=['POST'])
def get_ships(team_id):
    """
    Get the current number of ships the team has

    :returns result: a dict containing each ship and its count
    """
    result = dict()
    data = request.form
    if data is None:
        data = request.get_json()
        if data is None:
            abort(400)

    # make sure we have all the correct parameters
    params = ['token']
    validate_request(params, data)

    token = data['token']
    # the way we send it is janky, need to trim some stuff
    token = token.replace("token=", "")

    resp = api_request("teams/{}".format(team_id), method='GET', token=token)
    result['guardian'] = resp['guardian']
    result['striker'] = resp['striker']
    result['bomber'] = resp['bomber']
    return jsonify(result)


"""
    Update endpoints
"""
@app.route('/update/koth', methods=['POST'])
def update_koth():
    """
    Koth API will send updates to this endpoint to show who owns
    what planet, which will then be stored in our database

    param update: dictionary containing each planet and its owner
    """
    data = request.get_json()

    secret_key = data['key']
    if str(secret_key) != str(SECRET_KEY):
        return "Bad key", 200

    planet_name = data['planet']
    planet = Planet.query.filter_by(name=planet_name).first()
    action = data['action']
    if action == 'end':
        planet.status = 'end'

    elif action == 'start':
        planet.status = 'started'

    elif action == 'update':
        owner = data['team']
        planet.owner = owner

    DB.session.commit()
    return 'Success', 200

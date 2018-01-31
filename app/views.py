"""
Entry points for API calls
"""
from flask import request, jsonify
from . import app, DB
from . import errors
from .models.planets import Planet
from .models.alerts import Alert
from .util import validate_session

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
    planets = Planet.query.all()
    for planet in planets:
        planet_dict = dict()
        planet_dict['planet_id'] = planet.uuid
        planet_dict['owner'] = planet.owner
        result['planets'].append(planet_dict)

    return jsonify(result)

"""
    Team Functions
"""
@app.route('/credits/<team_id>')
def get_credits(team_id):
    """
    Get the credits of a specific team

    :returns result: a dict containing the credits for the team
    """
    if 'token' not in request.cookies:
        raise errors.AuthError("No session token")
    token = request.cookies['token']
    validate_session(token)
    return jsonify({'status': 200, 'credits': 50000})

@app.route('/stats/<team_id>')
def get_perks(team_id):
    """
    Get the current perks for a team

    :returns result: a dict containg each perk and its status
    """
    if 'token' not in request.cookies:
        raise errors.AuthError("No session token")
    token = request.cookies['token']
    return jsonify({'status': 200, 'health': '-50%', 'damage': '100%', 'speed': '+100%'})

@app.route('/ships/<team_id>')
def get_ships(team_id):
    """
    Get the current number of ships the team has

    :returns result: a dict containing each ship and its count
    """
    if 'token' not in request.cookies:
        raise errors.AuthError("No session token")
    token = request.cookies['token']
    return jsonify({'status': 200, 'ship1_count': 50, 'ship2_count': 0, 'ship3_count': 1000})


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
    pass
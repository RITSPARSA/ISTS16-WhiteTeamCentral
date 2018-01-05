
from . import app
from flask import request, jsonify

"""
    Statuses
"""
@app.route('/status/koth')
def koth():
    return jsonify({'status': 200, 'planets': {'planet1': 'team4'}})

"""
        Team Functions
"""
@app.route('/credits/<teamID>')
def getCredits(teamID):
    if not validateteamID(teamID):
        return jsonify({'status': 404})
    return jsonify({'status': 200, 'credits': 50000})

@app.route('/perks/<teamID>')
def getPerks(teamID):
    if not validateteamID(teamID):
        return jsonify({'status': 404})
    return jsonify({'status': 200, 'active_perks': ['perk1', 'perk2', 'bonus health']})

@app.route('/ships/<teamID>')
def getShips(teamID):
    if not validateteamID(teamID):
        return jsonify({'status': 404})
    return jsonify({'status': 200, 'ship1_count': 50, 'ship2_count': 0, 'ship3_count': 1000})

"""
        Helpers
"""
def validateteamID(team_id):
    if team_id is None:
        return False
    return True
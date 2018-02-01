"""
Configuration settings.
"""
AUTH_API_URL = "http://lilbite.org:9000"
BANK_API_URL = "http://lilbite.org:5000"
SHIP_API_URL = "http://192.168.1.38:5000"

AUTH_ENDPOINTS = ['validate-session', 'login', 'update-password',
                  'expire-session', 'update-session', 'pub-key']

BANK_ENDPOINTS = ['get-balance', 'buy', 'transfer', 'transactions', 'items']

SQLALCHEMY_DATABASE_URI = 'mysql://root:youwontguess23$@localhost/ists'

SLACK_URI = "https://hooks.slack.com/services/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"
CHANNEL = "#white-team-tool"
SLACK_USERNAME = "White Team"
ICON_EMOJI = ":robot_face:"

PLANET_NAMES = ['Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 
                'Ganymede', 'Callisto', 'Europa', 'Titan', 'Rhea', 'Tethys']

SECRET_KEY = "itshouldhavebeenslackpole"
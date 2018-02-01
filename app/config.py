"""
Configuration settings.
"""
AUTH_API_URL = "http://lilbite.org:9000"
BANK_API_URL = "http://lilbite.org:5000"
SHIP_API_URL = "http://lilbite.org:6000"

AUTH_ENDPOINTS = ['validate-session', 'login', 'update-password',
                  'expire-session', 'update-session', 'pub-key']

BANK_ENDPOINTS = ['get-balance', 'buy', 'transfer', 'transactions', 'items']

SQLALCHEMY_DATABASE_URI = 'mysql://root:youwontguess23$@localhost/ists'

SLACK_URI = "https://hooks.slack.com/services/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"
CHANNEL = "#white-team-tool"
SLACK_USERNAME = "White Team"
ICON_EMOJI = ":robot_face:"

PLANET_NAMES = ['moon', 'mercury', 'venus', 'mars', 'jupiter', 'saturn',
                'ganymede', 'callisto', 'europa', 'titan', 'rhea', 'tethys']

SECRET_KEY = "itshouldhavebeenslackpole"

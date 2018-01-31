"""
Configuration settings.
"""
AUTH_API_URL = "http://lilbite.org:9000"
BANK_API_URL = "http://lilbite.org:5000"

AUTH_ENDPOINTS = ['validate-session', 'login', 'update-password',
                  'expire-session', 'update-session', 'pub-key']

SQLALCHEMY_DATABASE_URI = 'mysql://root:youwontguess23$@localhost/ists'

SLACK_URI = "https://hooks.slack.com/services/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"
CHANNEL = "#white-team-tool"
SLACK_USERNAME = "White Team"
ICON_EMOJI = ":robot_face:"

NUM_PLANETS = 13

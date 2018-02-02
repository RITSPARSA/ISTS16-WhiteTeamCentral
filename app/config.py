"""
Configuration settings.
"""
import logging

class InfoFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.INFO

class ErrorFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.ERROR

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


LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(message)s'
        },
    },
    'filters': {
        'info_filter': {
            '()': InfoFilter,
        },
        'error_filter': {
            '()': ErrorFilter,
        }
    },
    'handlers': {
        'info': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename':  '/home/dosh/ISTS16-WhiteTeamCentral/app/logs/info.log',
            'mode': 'a',
            'backupCount': '16',
            'filters': ['info_filter']
        },
        'error': {
            'level': 'ERROR',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename':  '/home/dosh/ISTS16-WhiteTeamCentral/app/logs/error.log',
            'mode': 'a',
            'backupCount': '16',
            'filters': ['error_filter']
        },
    },
    'loggers': {
        'api_log': {'handlers': ['info', 'error'], 'level': 'DEBUG', 'propagate': False},
    }
}
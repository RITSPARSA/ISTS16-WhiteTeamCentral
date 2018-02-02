import sys
sys.path.append('/var/www/ISTS16-WhiteTeamCentral')
from app import app as application
application.secret_key = "thedoshboi"

"""
    Create our database and fill it with items
"""
from app import DB
from app.models.planets import Planet
from app.models.alerts import Alert
from app.config import PLANET_NAMES
DB.create_all()

print 'Adding planets...'
for planet in range(1, len(PLANET_NAMES)+1):
    print planet
    new_planet = Planet(uuid=planet, name=PLANET_NAMES[planet-1], owner=None, status=None)
    DB.session.add(new_planet)

print 'Done'
DB.session.commit()

"""
    Create our database and fill it with items
"""
from app import DB
from app.models.planets import Planet
from app.models.alerts import Alert
from app.config import NUM_PLANETS
DB.create_all()

print 'Adding planets...'
for planet in range(1, NUM_PLANETS+1):
    print planet
    new_planet = Planet(uuid=planet, owner=None)
    DB.session.add(new_planet)

print 'Done'
DB.session.commit()

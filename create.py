"""
    Create our database and fill it with items
"""
from app import DB
from app.models.planets import Planet
from app.models.perks import Perk
from app.config import NUM_PLANETS, NUM_PERKS
DB.create_all()

print 'Adding planets...'
for planet in range(1, NUM_PLANETS+1):
    print planet
    new_planet = Planet(uuid=planet, owner=None)
    DB.session.add(new_planet)

print 'Done'

print 'Adding perks...'
for perk in range(1, NUM_PERKS+1):
    print perk
    new_perk = Perk(uuid=perk)
    DB.session.add(new_perk)

print 'Done'
DB.session.commit()

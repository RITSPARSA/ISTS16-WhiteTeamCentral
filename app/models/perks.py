"""
    Document to represent a perk
"""
from app import DB

class Perk(DB.Model):
    """
    Represents a perk in our database

    :param uuid: the id of the planet
    """
    __tablename__ = 'perks'
    uuid = DB.Column(DB.Integer, primary_key=True)


    def __init__(self, uuid):
        self.uuid = uuid

    def __repr__(self):
        return '<Planet uuid={}>'.format(self.uuid)

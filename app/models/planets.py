"""
    Document to represent a planet
"""
from app import DB

class Planet(DB.Model):
    """
    Represents a planet in our database

    :param uuid: the id of the planet
    :param owner: the current owner of the planet
    """
    __tablename__ = 'planets'
    uuid = DB.Column(DB.Integer, primary_key=True)
    owner = DB.Column(DB.String(64))


    def __init__(self, uuid, owner):
        self.uuid = uuid
        self.owner = owner

    def __repr__(self):
        return '<Planet uuid={} owner={}>'.format(self.uuid, self.owner)

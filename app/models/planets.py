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
    name = DB.Column(DB.String(64))
    owner = DB.Column(DB.String(64))
    status = DB.Column(DB.String(64))


    def __init__(self, uuid, name, owner, status):
        self.uuid = uuid
        self.owner = owner
        self.name = name
        self.status = status

    def __repr__(self):
        return '<Planet uuid={} name={} owner={} status={}>'.format(self.uuid, self.name, self.owner, self.status)

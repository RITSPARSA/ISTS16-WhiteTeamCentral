"""
    Document to represent a alert
"""
from app import DB

class Alert(DB.Model):
    """
    Represents a alert in our database

    :param uuid: the id of the alert
    """
    __tablename__ = 'alert'
    uuid = DB.Column(DB.Integer, primary_key=True, auto_increment=True)


    def __init__(self, uuid):
        self.uuid = uuid

    def __repr__(self):
        return '<Alert uuid={}>'.format(self.uuid)

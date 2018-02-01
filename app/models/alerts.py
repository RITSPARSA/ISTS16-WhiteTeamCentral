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
    uuid = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    message = DB.Column(DB.String(256))

    def __init__(self, uuid, message):
        self.uuid = uuid
        self.message = message

    def __repr__(self):
        return '<Alert uuid={} message={}>'.format(self.uuid, self.message)

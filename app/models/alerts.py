"""
    Document to represent a alert
"""
from app import DB

class Alert(DB.Model):
    """
    Represents a alert in our database

    :param uuid: the id of the alert
    :param name: the name of the alert
    :param message: the message of the alert
    """
    __tablename__ = 'alert'
    uuid = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.String(64))
    message = DB.Column(DB.String(256))

    def __init__(self, name , message):
        self.name = name
        self.message = message

    def __repr__(self):
        return '<Alert uuid={} name={} message={}>'.format(self.uuid, self.name, self.message)

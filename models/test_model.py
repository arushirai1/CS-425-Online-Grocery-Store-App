from app import db
from sqlalchemy.dialects.postgresql import JSON

class Test(db.Model):
    __tablename__ = 'test'

    test_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    name2 = db.Column(db.String())
    def __init__(self, name, name2):
        self.name = name
        self.name2 = name2

    def __repr__(self):
        return '<id {}>'.format(self.test_id)
    
    #used for JSON formatting    
    def serialize(self):
        return {
            'test_id': self.test_id, 
            'name': self.name,
            'name2': self.name2,
        }
from src import db

class Dummy(db.Model):
    __tablename__ = 'dummies'
    DummyID = db.Column(db.Integer, primary_key=True)
    DummyName = db.Column(db.String(50), nullable=False)
    DeleteStatus = db.Column(db.Boolean, default=True)
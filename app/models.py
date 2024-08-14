from datetime import datetime
from pytz import timezone
from app import db


class Users (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    passwd = db.Column(db.String(20), nullable=False)
    dateCreated = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone('America/Santiago')))
    dateUpdated = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone('America/Santiago')))

    def check_password(self, password):
        if self.passwd == password:
            return True
        return False
    
    def personal_info(self):
        return  {"Nombre":self.fullName,
                 "username": self.username,
                 "email":self.email,
                 "dateCreated":self.dateCreated,
        }
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

#...

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    
    def __repr__(self):
        return f'User {self.username}'
class Picth(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    category= db.Column(db.String(255),unique = True,index = True)
    content= db.Column(db.String(255)) 

    def __repr__(self):
        return f'pitch {self.content}'      
from . import db
class Quote:
    '''
    Quote class to define Quote object
    '''
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote
    
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'User {self.username}'


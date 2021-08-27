from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    role = db.Column(db.String(255))
    blogs = db.relationship('Blog',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comment', backref='user', lazy='dynamic')


    def __repr__(self):
        return f'User {self.username}'


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))    

    def __repr__(self):
        return f'User {self.username}'



class Blog(db.Model):

    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    blog_title = db.Column(db.String)
    blog_post = db.Column(db.String)

    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment', backref='blog', lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()



    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()

        

    def __repr__(self):
        return f'blog{self.blog_post}'  
    

class Comment(db.Model):

    __tablename__='comment'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer,db.ForeignKey("blogs.id"))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        comments = Comment.query.filter_by(blog_id=blog_id).all()
        return comments

    def __repr__(self):
        return f'Comment:{self.comment}'    

class Quote:
    ''' Quote class to define Qouto object'''
    def __init__(self,author,id,quote):
        
        self.author= author
        self.id= id
        slef.quote = quote  




    


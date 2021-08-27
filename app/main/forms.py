from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you.',validators = [Required()])
  submit = SubmitField('Submit')


class SubmitBlog(FlaskForm):
  blog_title = StringField('Title', validators = [Required()])
  
  blog_post = TextAreaField ('Write your blog!!')   
  submit = SubmitField('Submit')  

class postComment(FlaskForm):
  comment   = TextAreaField ('Post a comment',validators = [Required()]) 
  submit = SubmitField('Post')

class updateBlog(FlaskForm):
  blog_post = TextAreaField ('update your blog!!',validators = [Required()])
  submit = SubmitField('Submit')  

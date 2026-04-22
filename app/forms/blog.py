



from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed




class BlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])

    description = TextAreaField('description', validators=[DataRequired()])

    image = FileField('image', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'webp'], 'que des images')])
    
    submit = SubmitField('Save Changes')





from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired




class BlogForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    image = FileField('image')
    submit = SubmitField('Save Changes')

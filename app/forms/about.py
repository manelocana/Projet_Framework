


from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired




class AboutForm(FlaskForm):
    content = TextAreaField('Biography', validators=[DataRequired()])
    submit = SubmitField('Save changes')

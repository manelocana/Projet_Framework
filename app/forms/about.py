


from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired



""" formulaire avec wtforms , et validations de données """
class AboutForm(FlaskForm):
    content = TextAreaField('Biography', 
                            validators=[DataRequired()], 
                            render_kw={'class':'ckeditor'})
    
    save = SubmitField('Save changes')

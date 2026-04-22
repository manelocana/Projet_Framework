


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed



class PortfolioForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])

    description = TextAreaField('Description / Link', validators=[DataRequired()])

    image = FileField("Image", validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'webp'], 'seulement images')])

    submit = SubmitField('Add project')

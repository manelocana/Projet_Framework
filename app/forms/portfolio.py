


from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired




class PortfolioForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description / Link', validators=[DataRequired()])
    image = FileField("Image")
    submit = SubmitField('Add project')

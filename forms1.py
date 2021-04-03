from wtforms import Form, BooleanField, StringField, PasswordField, validators, TextAreaField, IntegerField

from wtforms.validators import DataRequired

class FeedbackForm(Form):
    name = StringField("Parking Area Name", validators=[validators.Length(min=3, max=25),
                                                        validators.DataRequired(message="Please Fill This Field")])

    username = StringField("Username", validators=[validators.Length(min=3, max=25),
                                                   validators.DataRequired(message="Please Fill This Field")])
    email = StringField("Email", validators=[validators.Length(min=7, max=50),
                                             validators.DataRequired(message="Please Fill This Field")])
    password = PasswordField("Password", validators=[

        validators.DataRequired(message="Please Fill This Field"),
    ])

    number = StringField("Mobile Number", validators=[validators.Length(min=7, max=50),
                                                      validators.DataRequired(message="Please Fill This Field")])
    subject = StringField("Subject", validators=[validators.Length(min=7, max=50),
                                                 validators.DataRequired(message="Please Fill This Field")])
    description = StringField("Description", validators=[validators.Length(min=7, max=50),
                                                         validators.DataRequired(message="Please Fill This Field")])
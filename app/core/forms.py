from flask_user.forms import RegisterForm, InviteForm
from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, TextAreaField,\
    SelectField
from . models import Role

Role
# ROLES = [role.label for role in Role.query.all()]
ROLES = ["Patient", "Provider", "Admin"]


class MyInviteForm(InviteForm):
    role = SelectField(
        'Role',
        choices=[(str(idx), role) for idx, role in enumerate(ROLES)],
    )
    next = "#"


class MyRegisterForm(RegisterForm):
    """
    The user registration form, extends the default
    Flask-User provided registration form.
    """
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])


class BetaUserApplicationForm(RegisterForm):
    """
    The user registration form, extends the default
    Flask-User provided registration form.
    """
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])
    about_me = TextAreaField()


# Define the User profile form
class UserProfileForm(Form):
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])
    submit = SubmitField('Save')

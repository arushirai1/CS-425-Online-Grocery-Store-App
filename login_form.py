from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    _state_list = ['FL', 'GA', 'PA', 'RI', 'NC', 'OH', 'NY', 'MI', 'CT', 'MS', 'NC', 'MA']
    username = StringField('username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    state_select = StringField('State: (two letter)', validators=[DataRequired()])
    submit = SubmitField('Sign In')

    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)
from flask import Flask, redirect, url_for, render_template,session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextField,TextAreaField,SelectField,BooleanField,IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = 'key'

class InfoForm(FlaskForm):
    name = StringField("Please enter your full name",validators=[DataRequired()])

    phone = IntegerField("Please enter your phone number",validators=[DataRequired()])

    age = SelectField("Are you above 18 years old?",choices=[('y','Yes'),('n','No')])

    pet = StringField("Which animal are you looking to adopt?",validators=[DataRequired()])

    enq = TextAreaField()

    submit = SubmitField("Submit Application")

@app.route('/',methods=['GET','POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['phone'] = form.phone.data
        session['age'] = form.age.data
        session['pet'] = form.pet.data
        session['enq'] = form.enq.data

        return redirect(url_for('thankyou'))
    return render_template('indexad.html',form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('ty.html')

if __name__ == '__main__':
    app.run(debug=True)

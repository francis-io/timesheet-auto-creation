from flask import Flask, render_template, redirect, url_for, send_file, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import os
#from livereload import Server
from create_timesheet import create_timesheet

# mostly adapted from https://github.com/hackersandslackers/flask-wtform-tutorial
app = Flask(__name__, template_folder='/web/templates')

# Flask-WTF requires an encryption key - the string can be anything
app.secret_key = os.urandom(24)

class TimesheetForm(FlaskForm):
    name = StringField(
        'Your Name',
        [DataRequired()]
    )
    contact_name = SelectField(
        'Computacenter Contacts Name',
        [DataRequired()],
        choices=[
            ('Mark Beresford'), #TODO: store in a file somewhere
            ('person2')
        ]
    )
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def get_timesheet_details():
    form = TimesheetForm()

    if form.validate_on_submit():
        print(request.form.get("name"))
        return redirect(url_for("create_timesheets",
                                name=request.form.get("name"),
                                contact_name=request.form.get("contact_name")))
    return render_template(
        "create_timesheet.jinja2",
        form=form
    )

@app.route('/create_timesheet')
def create_timesheets():
    name = request.args.get("name")
    computercenter_contact_name=request.args.get("contact_name")

    timesheet = create_timesheet(name, computercenter_contact_name)

    # TODO: clean up files
    return send_file(timesheet, as_attachment=True)


if __name__ == '__main__':
    # TODO: find a better way to do this
    # app.debug = True
    # server = Server(app.wsgi_app)
    # server.serve(port=80, host='0.0.0.0')

    app.run(host='0.0.0.0', port=80)
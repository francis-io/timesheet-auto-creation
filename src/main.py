from flask import Flask, render_template, redirect, url_for, send_file, send_from_directory, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import os
from create_timesheet import create_timesheet


app = Flask(__name__, template_folder='templates')

# Flask-WTF requires an encryption key - the string can be anything
app.secret_key = os.urandom(24)
#app.config['SECRET_KEY'] = '239484290583425084350812345'

#Bootstrap(app)

class TimesheetForm(FlaskForm):
    """Contact form."""
    name = StringField(
        'Your Name',
        [DataRequired()]
    )
    contacts_name = SelectField(
        'Computacenter Contacts Name',
        [DataRequired()],
        choices=[
            ('Mark Beresford'),
            ('person2')
        ]
    )
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def get_timesheet_details():
    form = TimesheetForm()

    if form.validate_on_submit():
        print(request.form.get("name"))
        return redirect(url_for("create_timesheet", name=request.form.get("name")))
    return render_template(
        "create_timesheet.jinja2",
        form=form,
        template="form-template",
        title="Create Timesheet"
    )

@app.route('/create_timesheet')
def create_timesheets():
    name = request.args.get("name")
    print(name)
    timesheet = create_timesheet(name)
    print(timesheet)
    # TODO: clean up files
    return send_file(timesheet, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
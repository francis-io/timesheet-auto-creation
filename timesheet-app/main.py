from flask import Flask, render_template, redirect, url_for, send_file, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired
from wtforms.fields import Label
import os
from datetime import datetime, date

from timesheet_app.create_timesheet import create_timesheet, get_start_of_week


# mostly adapted from https://github.com/hackersandslackers/flask-wtform-tutorial
app = Flask(__name__, template_folder="templates")

# Flask-WTF requires an encryption key - the string can be anything
app.secret_key = os.urandom(24)


class TimesheetForm(FlaskForm):
    name = StringField("Name", [DataRequired()])
    contact_name = SelectField(
        "Computacenter Contacts Name",
        [DataRequired()],
        choices=[("Mark Beresford"), ("person2")],  # TODO: store this somewhere else
    )
    confirm = BooleanField(
        validators=[
            DataRequired(),
        ],
    )
    submit = SubmitField("Download")


@app.route("/", methods=["GET", "POST"])
def get_timesheet_details():
    form = TimesheetForm()

    # Forms only get ran on import, so i need to update the label with the current time
    # https://stackoverflow.com/a/59527398
    form.confirm.label = Label(
        field_id="confirm",
        text="As of today, {0}, confirm the timesheet start date of {0}".format(
            datetime.today().strftime("%a %d/%m"),
            get_start_of_week(date.today()),
        ),
    )

    if form.validate_on_submit():
        return redirect(
            url_for(
                "create_timesheets",
                name=request.form.get("name"),
                contact_name=request.form.get("contact_name"),
            )
        )
    return render_template(
        "create_timesheet.jinja2", title="Timesheet Creator", form=form
    )


@app.route("/create_timesheet")
def create_timesheets():
    name = request.args.get("name")
    computercenter_contact_name = request.args.get("contact_name")

    timesheet = create_timesheet(name, computercenter_contact_name)

    # TODO: clean up files
    return send_file(timesheet, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

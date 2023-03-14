from flask import Flask, render_template as rt
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import sqlite3


class NameForm(FlaskForm):
    first_name = StringField("What is your first name?")
    last_name = StringField("What is your last name?")
    submit = SubmitField("Submit")


app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO users VALUES (?, ?)",
                (form.first_name.data, form.last_name.data),
            )
            con.commit()
            msg = "Done"
        return rt("success.html")
    return rt("index.html", form=form)


if __name__ == "__main__":
    app.run()

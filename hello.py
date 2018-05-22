from flask import Flask, g, render_template
import sqlite3
import os

DATABASE = "database.db"

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True


# helper method to get the database since calls are per thread,
# and everything function is a new thread when called
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# helper to close
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    cur = get_db().cursor()
    res = cur.execute("select * from owce")
    return render_template("index.html", owce=res)


if __name__ == "__main__":
	app.run()

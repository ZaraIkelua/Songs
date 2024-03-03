import sqlite3
from flask import Flask, render_template, request

# app = Flask(__name__, instance_relative_config=True) creates the Flask instance.
# __name__ is the name of the current Python module.
app = Flask(__name__)


# App Routing means mapping the URLs to a specific function that will handle the logic for that URL.
# In our application, the URL (“/”) is associated with the root URL.
@app.route('/')
def index():
    # open the connection to the database
    conn = sqlite3.connect('songs.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from artist")
    rows = cur.fetchall()

    conn.close()
    return render_template('index.html', rows=rows)

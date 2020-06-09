import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/teams')
def team_select():
    return render_template("team_select.html")


@app.route('/create-team')
def team_create():
    return render_template("team_create.html")


@app.route('/create-player')
def player_create():
    return render_template("player_create.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


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


@app.route('/submit-player', methods=['POST'])
def submit_player():
    players = mongo.db.players
    players.insert_one(request.form.to_dict())
    return redirect(url_for('player_list'))


@app.route('/players')
def player_list():
    return render_template("player_list.html", players=mongo.db.players.find())


@app.route('/players/<player_id>')
def player_details(player_id):
    player = mongo.db.players.find_one({'_id': ObjectId(player_id)})
    return render_template('player_details.html', player=player)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

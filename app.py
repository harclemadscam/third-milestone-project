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
    return render_template("team_select.html", teams=mongo.db.teams.find())


@app.route('/teams/<team_id>')
def team_home(team_id):
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    return render_template("team_home.html", team=team)


@app.route('/create-team')
def team_create():
    nations = mongo.db.nations.find().collation({'locale': 'en'}).sort('name')
    return render_template("team_create.html", nations=nations)


@app.route('/teams/<team_id>/create-player')
def player_create(team_id):
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    nations = mongo.db.nations.find().collation({'locale': 'en'}).sort('name')
    positions = mongo.db.positions.find()
    return render_template("player_create.html", team=team, nations=nations, positions=positions)


@app.route('/teams/<team_id>/submit-player', methods=['POST'])
def submit_player(team_id):
    players = mongo.db.players
    players.insert_one(request.form.to_dict())
    return redirect(url_for('player_list', team_id=team_id))


@app.route('/submit-team', methods=['POST'])
def submit_team():
    teams = mongo.db.teams
    teams.insert_one(request.form.to_dict())
    return redirect(url_for('team_select'))


@app.route('/teams/<team_id>/players')
def player_list(team_id):
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    players = mongo.db.players.find({'team_id': team_id})
    return render_template("player_list.html", team=team, players=players)


@app.route('/players/<player_id>')
def player_details(player_id):
    player = mongo.db.players.find_one({'_id': ObjectId(player_id)})
    return render_template("player_details.html", player=player)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

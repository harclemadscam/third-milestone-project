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
    formations = mongo.db.formations.find()
    return render_template("team_create.html", nations=nations, formations=formations)


@app.route('/teams/<team_id>/edit-team')
def team_edit(team_id):
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    nations = mongo.db.nations.find().collation({'locale': 'en'}).sort('name')
    formations = mongo.db.formations.find()
    return render_template("team_edit.html", team=team, nations=nations, formations=formations)


@app.route('/teams/<team_id>/update-team', methods=['POST'])
def update_team(team_id):
    teams = mongo.db.teams
    teams.update({'_id': ObjectId(team_id)}, {
        'name': request.form.get('name'),
        'year': request.form.get('year'),
        'nation': request.form.get('nation'),
        'manager': request.form.get('manager'),
        'formation': request.form.get('formation'),
        'emblem': request.form.get('emblem'),
        'first_colour': request.form.get('first_colour'),
        'second_colour': request.form.get('second_colour'),
    })
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    return redirect(url_for('team_home', team_id=team_id, team=team))


@app.route('/teams/<team_id>/delete-team')
def delete_team(team_id):
    mongo.db.players.update_many(
        {'team_id': team_id},
        {
          '$set': {
            'team_id': '',
          }
        })
    mongo.db.teams.delete_one({'_id': ObjectId(team_id)})
    return redirect(url_for('team_select'))


@app.route('/teams/<team_id>/create-player')
def player_create(team_id):
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    nations = mongo.db.nations.find().collation({'locale': 'en'}).sort('name')
    positions = mongo.db.positions.find()
    positions_list = list(positions)
    return render_template("player_create.html", team=team, nations=nations, positions=positions_list)


@app.route('/teams/<team_id>/players/<player_id>/edit-player')
def player_edit(player_id, team_id):
    player = mongo.db.players.find_one({'_id': ObjectId(player_id)})
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    team_id = ObjectId(str(team_id))
    teams = mongo.db.teams.find()
    nations = mongo.db.nations.find().collation({'locale': 'en'}).sort('name')
    positions = mongo.db.positions.find()
    positions_list = list(positions)
    return render_template("player_edit.html", player=player, team=team, team_id=team_id, teams=teams, nations=nations, positions=positions_list)


@app.route('/teams/<team_id>/players/<player_id>/update-player', methods=['POST'])
def update_player(player_id, team_id):
    players = mongo.db.players
    players.update({'_id': ObjectId(player_id)},
    {
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'team_id': request.form.get('team_id'),
        'age': request.form.get('age'),
        'height': request.form.get('height'),
        'weight': request.form.get('weight'),
        'nation': request.form.get('nation'),
        'first_position': request.form.get('first_position'),
        'second_position': request.form.get('second_position'),
        'foot': request.form.get('foot'),
        'shirt_number': request.form.get('shirt_number'),
        'attacking': request.form.get('attacking'),
        'technique': request.form.get('technique'),
        'physical': request.form.get('physical'),
        'defending': request.form.get('defending'),
        'stamina': request.form.get('stamina'),
        'speed': request.form.get('speed'),
        'notes': request.form.get('notes'),
        'image': request.form.get('image'),
        'is_injured': request.form.get('is_injured'),
    })
    return redirect(url_for('player_list', team_id=team_id))


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


@app.route('/teams/<team_id>/players/<player_id>')
def player_details(player_id, team_id):
    player = mongo.db.players.find_one({'_id': ObjectId(player_id)})
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    return render_template("player_details.html", player=player, team=team)


@app.route('/teams/<team_id>/line-up')
def lineup(team_id):
    players = mongo.db.players.find({'team_id': team_id})
    players_list = list(players)
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    return render_template("lineup.html", players=players_list, team=team)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

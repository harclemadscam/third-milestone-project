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

# Home Page
@app.route('/')
@app.route('/index')
def index():
    """Renders index page"""
    return render_template("index.html")

# Teams
@app.route('/teams')
def team_select():
    """Renders team selection page"""
    return render_template("team_select.html", teams=mongo.db.teams.find())


@app.route('/teams/<team_id>')
def team_home(team_id):
    """Renders home page of team with matching team id"""
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    return render_template("team_home.html", team=team)


@app.route('/create-team')
def team_create():
    """Renders the team creation form, gets nation and formation data to populate form"""
    nations = mongo.db.nations.find().collation({'locale': 'en'}).sort('name')
    formations = mongo.db.formations.find()
    return render_template("team_create.html", nations=nations, formations=formations)


@app.route('/submit-team', methods=['POST'])
def submit_team():
    """Creates a team using data from team creation form, redirects to team select page"""
    teams = mongo.db.teams
    teams.insert_one(request.form.to_dict())
    return redirect(url_for('team_select'))


@app.route('/teams/<team_id>/edit-team')
def team_edit(team_id):
    """Renders the edit team form for a team with matching team id,
    gets nation and formation data to populate form
    """
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    nations = mongo.db.nations.find().collation({'locale': 'en'}).sort('name')
    formations = mongo.db.formations.find()
    return render_template("team_edit.html", team=team, nations=nations, formations=formations)


@app.route('/teams/<team_id>/update-team', methods=['POST'])
def update_team(team_id):
    """Updates the team of matching team id with data from edit team form,
    redirects to team home page
    """
    mongo.db.teams.update_one(
        {'_id': ObjectId(team_id)},
        {
          '$set': {
            'name': request.form.get('name'),
            'year': request.form.get('year'),
            'nation': request.form.get('nation'),
            'manager': request.form.get('manager'),
            'formation': request.form.get('formation'),
            'emblem': request.form.get('emblem'),
            'first_colour': request.form.get('first_colour'),
            'second_colour': request.form.get('second_colour'),
          }
        })
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    return redirect(url_for('team_home', team_id=team_id, team=team))


@app.route('/teams/<team_id>/delete-team')
def delete_team(team_id):
    """Deletes a team with matching team id, clears the team id value for players
    whose team id value matches the team id of the deleted team
    """
    # Sets team id for matching players to blank, for them to appear as free agents
    mongo.db.players.update_many(
        {'team_id': team_id},
        {
          '$set': {
            'team_id': '',
          }
        })
    mongo.db.teams.delete_one({'_id': ObjectId(team_id)})
    return redirect(url_for('team_select'))

# Players
@app.route('/teams/<team_id>/players')
def player_list(team_id):
    """Renders player list page, getting players whose team id value matches the team id"""
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    players = mongo.db.players.find({'team_id': team_id})
    return render_template("player_list.html", team=team, players=players)


@app.route('/teams/<team_id>/players/<player_id>')
def player_details(player_id, team_id):
    """Renders the player profile page for the player of matching player id,
    gets team with matching team id
    """
    player = mongo.db.players.find_one({'_id': ObjectId(player_id)})
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    return render_template("player_details.html", player=player, team=team)


@app.route('/teams/<team_id>/create-player')
def player_create(team_id):
    """Renders the player creation form,
    gets team, nation, and position data to populate the form
    """
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    nations = mongo.db.nations.find().collation({'locale': 'en'}).sort('name')
    positions = mongo.db.positions.find()
    # Creates a list of position data so that the data can be used more than once
    positions_list = list(positions)
    return render_template("player_create.html", team=team, nations=nations, positions=positions_list)


@app.route('/teams/<team_id>/submit-player', methods=['POST'])
def submit_player(team_id):
    """Creates a player using data from player creation form, redirects to player list"""
    players = mongo.db.players
    players.insert_one(request.form.to_dict())
    return redirect(url_for('player_list', team_id=team_id))


@app.route('/teams/<team_id>/players/<player_id>/edit-player')
def player_edit(player_id, team_id):
    """Renders the edit player form for a player with matching player id,
    gets team, nation and position data to populate form
    """
    player = mongo.db.players.find_one({'_id': ObjectId(player_id)})
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    # Converts team id into a string so that it can used in the form
    team_id = ObjectId(str(team_id))
    teams = mongo.db.teams.find()
    nations = mongo.db.nations.find().collation({'locale': 'en'}).sort('name')
    positions = mongo.db.positions.find()
    # Creates a list of position data so that the data can be used more than once
    positions_list = list(positions)
    return render_template("player_edit.html", player=player, team=team, team_id=team_id, teams=teams, nations=nations, positions=positions_list)


@app.route('/teams/<team_id>/players/<player_id>/update-player', methods=['POST'])
def update_player(player_id, team_id):
    """Updates the player of matching player id with data from edit player form,
    redirects to player list page
    """
    mongo.db.players.update_one(
        {'_id': ObjectId(player_id)},
        {
          '$set': {
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
          }
        })
    return redirect(url_for('player_list', team_id=team_id))


@app.route('/<player_id>/delete-player')
def delete_player(player_id):
    """Deletes a player with matching player id, checks if team id is blank for the player,
    if not redirect to player list, if so redirect to free agents
    """
    player = mongo.db.players.find_one({'_id': ObjectId(player_id)})
    mongo.db.players.delete_one({'_id': ObjectId(player_id)})
    team_id = player['team_id']
    if team_id == "":
        return redirect(url_for('free_agents'))
    else:
        return redirect(url_for('player_list', team_id=team_id))

# Lineups
@app.route('/teams/<team_id>/line-up')
def lineup(team_id):
    """Renders the lineup creator page,
    gets player, team and formation data to populate the forms on the page
    """
    players = mongo.db.players.find({'team_id': team_id})
    # Creates a list of player data so that the data can be used more than once
    players_list = list(players)
    team = mongo.db.teams.find_one({'_id': ObjectId(team_id)})
    formation = mongo.db.formations.find_one({'name': team['formation']})
    formations = mongo.db.formations.find()
    return render_template("lineup.html", players=players_list, team=team, formation=formation, formations=formations)


@app.route('/teams/<team_id>/line-up/update-formation', methods=['POST'])
def update_formation(team_id):
    """Updates the formation value of the team with matching team id,
    using data from formation form
    """
    mongo.db.teams.update_one(
        {'_id': ObjectId(team_id)},
        {
          '$set': {
            'formation': request.form.get('formation')
          }
        })
    return redirect(url_for('lineup', team_id=team_id))


@app.route('/teams/<team_id>/line-up/submit-team', methods=['POST'])
def submit_lineup(team_id):
    """Updates the team of matching team id with lineup data from the set lineup form,
    then updates players with a matching team id value with a string version of their own player id
    """
    mongo.db.teams.update_one(
        {'_id': ObjectId(team_id)},
        {
          '$set': {
            'eleven': request.form.get('eleven'),
            'ten': request.form.get('ten'),
            'nine': request.form.get('nine'),
            'eight': request.form.get('eight'),
            'seven': request.form.get('seven'),
            'six': request.form.get('six'),
            'five': request.form.get('five'),
            'four': request.form.get('four'),
            'three': request.form.get('three'),
            'two': request.form.get('two'),
            'one': request.form.get('one'),
          }
        })
    # Adding a string player id to each player allows it to be compared to the team lineup data
    players = mongo.db.players.find({'team_id': team_id})
    for player in players:
        player_id = player['_id']
        string_id = str(player_id)
        mongo.db.players.update_one(
            {'_id': ObjectId(player_id)},
            {
              '$set': {
                'string_id': string_id,
              }
            })
    return redirect(url_for('lineup', team_id=team_id))

# Free Agents
@app.route('/free-agents')
def free_agents():
    """Renders the free agents page, getting players whose team id value is blank"""
    players = mongo.db.players.find({'team_id': ''})
    return render_template("free_agents.html", players=players)


@app.route('/free_agents/<player_id>')
def free_agent_details(player_id):
    """Renders the free agent profile page for a free agent with matching player id"""
    player = mongo.db.players.find_one({'_id': ObjectId(player_id)})
    return render_template("free_agent_details.html", player=player)


@app.route('/free_agents/<player_id>/edit-player')
def free_agent_edit(player_id):
    """Renders the edit free agent form for a free agent with matching player id,
    gets team, nation and position data to populate form
    """
    player = mongo.db.players.find_one({'_id': ObjectId(player_id)})
    teams = mongo.db.teams.find()
    nations = mongo.db.nations.find().collation({'locale': 'en'}).sort('name')
    positions = mongo.db.positions.find()
    # Creates a list of position data so that the data can be used more than once
    positions_list = list(positions)
    return render_template("free_agent_edit.html", player=player, teams=teams, nations=nations, positions=positions_list)


@app.route('/free_agents/<player_id>/update-player', methods=['POST'])
def update_free_agent(player_id):
    """Updates the free agent of matching player id with data from edit free agent form,
    redirects to free agents page
    """
    mongo.db.players.update_one(
        {'_id': ObjectId(player_id)},
        {
          '$set': {
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
          }
        })
    return redirect(url_for('free_agents'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

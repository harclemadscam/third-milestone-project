# Football Squad Manager - Practical Python and Data-Centric Development Milestone Project
<http://football-squad-manager.herokuapp.com/>
## Overview
For the third project of my Code Institute Full Stack Web Developer course, I was tasked with building a full stack site that allows users to manage a common dataset.
This stage of the course introduced Python, the Flask framework, and MongoDB - all of which were fundamental requirements for completing the project.
I decided to create a website that allows the user to manage data related to football teams and players. CRUD functionality is fully implemented; users can create, read, update,
and delete football teams and players. As an added bonus, the user can also set the formation and first eleven of the team and see a visual representation. There is no user authentication
in place, so every team and player in the database can be seen and edited by all users.

The site starts on a basic landing page and presents two options for the user - to select an existing team or create a new one. A team can be created using a form and once created appears
on the team selection page. When a team is selected, the user is taken to the team's home page - from this page they can view the list of players that belong to the team, create a new player
that is added to the team, set the team's line-up using a line-up creator, edit the details of the team (or delete it), view players that are not assigned to a team, or go back to team
selection. The list of players is presented in a sortable table, and from this page the user can view each player's personal profile. Each profile allows the user to view and edit player
data, or delete the player entirely. The data that can be stored for teams and players is comprehensive and relevant for football fans.

The Python Flask framework is used extensively to create HTML templates for each page, with routes created in the "app.py" file. The database is MongoDB, storing data for teams, players,
nations, postions and formations (though the user can only manage team and player data). For the frontend, I made use of Bootstrap, custom CSS and JavaScript and the site is fully responsive
across devices. The website is deployed to [Heroku](http://football-squad-manager.herokuapp.com/).

## UX
My full UX documentation can be found in the ux-design folder, which can be found [here](ux-design).
This includes documents detailing my thoughts on the strategy and scope planes of this project, plus the basic structure and my skeleton wireframes.

### User Stories

* As a football fan, I want to create my favourite team in the database - with the correct colours, emblem and players.
* As an imaginative football fan, I want to create a fantasy team in the database with fantasy or even celebrity players.
* As a football coach, I want to be able to use the app to help manage my team. I can do this by storing and comparing player data or setting lineups.
* As someone with an interest in creating football lineups, I want to be able to create a team and players and choose a lineup for it.
* As a member of the football community, I want to be able to see what other users have created.

## Features
### Existing Features

* Team data management. You can create, view, edit and delete teams. The following values can be saved to a team: team name, year established, nation, manager name, formation, team emblem url,
first colour and second colour. You can also save a lineup of 11 players to a team, which can be viewed on the lineup page.
* Player data management. You can also create, view, edit and delete players. Players are initially assigned to a team and viewed from the team specific player list. Each player has a profile
page where their information can be viewed easily. The following values can be saved to a player: first name, last name, shirt number, nation, team, age, height, weight, preferred foot,
best position, second position, injured, attacking, technique, physical, defending, stamina, speed, notes and player image url.
* The navbar allows for access to pages that are relevant to the user depending on the page they are on. More options appear when a team has been selected.
* Modals for data deletion. When you click to delete a player or team, a modal appears asking for confirmation.
* Free agents. When a team is deleted, the players that were on the team are still accessible. They appear on the free agents list and can be assigned to a new team.
* The line-up creator. The line-up creator displays a formation screen that can be customised using the forms on the page. The currently set line-up is saved to the team.
* Sortable tables. Bootstrap Table is used to provide sortable tables to view player data.
### Future Features

* User authentication could be implemented to limit which teams and players a user can view, edit or delete. Teams and players could be made private for certain users.
* More values could be added to players and teams to allow for greater customisation.
* Free Agents cannot currently be edited without assigning them to a team, so a method of editing them without doing so could be created.
* More features related to football could be added, like stadiums and training.
* Currently only one line-up can be saved, so a feature to save more than one could be added.
* The ability to search for players and teams to find data more easily.
* More formations could be added to the database for teams to select. To do so the following is required:
  * The formation must be saved to the formations collection in MongoDB.
  * It must be given a name value, this is displayed to the user.
  * It must have another eleven keys, named one to eleven. The values of each must use the names of the existing position classes in CSS which determine the 
  positioning on the line-up page pitch. Ideally they will be in order of appearance on the pitch, with eleven being a striker and one the goalkeeper.
  * If new positions are needed, these must be created in CSS and given the appropriate values for left and top. The positions.js file should also be updated
  to include the new positions. 

## Technologies Used
* [HTML5](https://www.w3.org/TR/2017/REC-html52-20171214/)

  * Used to create the structure of each page. As a Flask requirement, they are stored in the templates folder.

* [CSS3](https://www.w3.org/Style/CSS/)

  * Custom styling to the HTML - including font, layout and colours.

* [Python3](https://www.python.org/)

  * Used to create the app.py file - primarily for template routing and accessing the MongoDB database. Packages listed in requirements file.

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)

  * Python framework used to route to and render HTML templates.

* [MongoDB](https://www.mongodb.com/)

  * The database of the project, where all user data is stored.

* [Bootstrap](https://getbootstrap.com/)

  * An open source framework focused on responsive, mobile-first development. Used to create a number of components and features on the page, such as forms, the navbar and modals.

* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

  * JavaScript was used to create dynamic visuals for the lineup page.

* [Git](https://git-scm.com/)

  * Version control and committing changes to GitHub.

* [GitHub](https://github.com/)

  * Used to host my project files.

* [Heroku](https://heroku.com/)

  * Used to deploy the final version of the project.

* [Google Chrome/Developer Tools](https://www.google.com/intl/en/chrome/)

  * My internet browser. 
  The Developer Tools were used to troubleshoot, edit the layout, and preview changes, as well as test the responsiveness of the page.

* [GitPod IDE](https://gitpod.io/)

  * The application I used to develop the project.

* [Bootstrap Table](https://bootstrap-table.com/)

  * Bootstrap-inspired framework. Used to create the sortable tables.

* [Font Awesome](https://fontawesome.com/)

  * Used to source the icons shown on buttons.

* [Google Fonts](https://fonts.google.com/)
  
  * Used to provide the Arimo font.

## Testing
My full testing documentation can be found in the testing folder, which can be found [here](testing).

## Deployment
The project was coded in the GitPod IDE. I had previously installed the GitPod browser extension, which allows you to create a GitPod workspace with the click of a button in GitHub.
I first created a new repository in GitHub, using the Code Institute’s full GitPod template, then clicked the GitPod button to launch a GitPod workspace from that repository. I used
Git within GitPod for version control, with all commits being pushed to the linked GitHub repository.

To deploy a live version of the site, I used Heroku. I created a new app in Heroku called football-squad-manager, and linked my newly created GitHub repository to the app from the
“Deploy” section of Heroku.  A Procfile is a requirement for Heroku, so I created one using the “echo web: python app.py > Procfile” command in my workspace terminal. In addition, I had
to set values for IP and PORT as Heroku config vars. Once that was in place, I switched on “Automatic deploys”, meaning that every push to my GitHub repository master branch automatically
deployed to Heroku and updated the live version of the app.  The app is live [here](http://football-squad-manager.herokuapp.com/).

To keep my MongoDB URI and password secret and not accessible from the deployed version, the development version is different to the deployed version. In the deployed version, this
information is stored as Heroku config vars. In the development version, I created a second Python file called “env.py” to store the information as environment variables. The “app.py”
file checks if this “env” file exists and if it does, imports it. The “env.py” file is not pushed to GitHub and only exists in the development workspace.

## Credits
### Content
All static text content was created by myself.

### Media
Images were sourced from: 

<https://www.pexels.com/>
<https://pixabay.com/>

The user can also submit web URLs as player photos or team emblems.

### Acknowledgements
The idea was inspired by computer games such as Football Manager, FIFA and Pro Evolution Soccer.

I made frequent use of [Stack Overflow](https://stackoverflow.com/) and the [Bootstrap Documentation](https://getbootstrap.com/docs/4.5/getting-started/introduction/).
Bootstrap components were copied from the documentation and adapted to suit my own needs. The adjustments to the "card-img-top" class were taken from [this thread](https://stackoverflow.com/questions/37287153/how-to-get-images-in-bootstraps-card-to-be-the-same-height-width).

To create the box shadow effect, I used the tool [Here](https://www.cssmatic.com/box-shadow).
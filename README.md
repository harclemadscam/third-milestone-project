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

* A
* B
* C

### Future Features

* 1
* 2

  * 1
  * 2

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
I first created a new repository in GitHub and then created the GitPod workspace, where I coded the project. 
I used Git within GitPod for version control, with all commits being pushed to the linked GitHub repository. As I was not working on a live website and I was the sole developer, I used only the master branch.

To publish my website in GitHub, I used GitHub Pages from the settings of my repository. After selecting the master branch as the source, my website project can be found here: <https://harclemadscam.github.io/second-milestone-project/>

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

# Njiiri bloggy- Web App

#### This application will allow you to create and share your opinions and other users can read and comment on them. , 30/04/2021

#### By **yvonne Njiiri**

## Description
This web app will allow you to create and share your opinions and other users can read and comment on them.
Additionally, There is a feature that displays random quotes to inspire your users through an api end point


### User stories Specification
- As a user, I would like to view the blog posts on the site
- As a user, I would like to comment on blog posts
- As a user, I would like to view the most recent posts
- As a user, I would like to an email alert when a new post is made by joining a subscription.
- As a user, I would like to see random quotes on the site
- As a writer, I would like to sign in to the blog.
- As a writer, I would also like to create a blog from the application.
- As a writer, I would like to delete comments that I find insulting or degrading.
- As a writer, I would like to update or delete blogs I have created.




## Setup/Installation Requirements
- install Python3.9
- Clone this repository `git clone https://github.com/kagus-code/Kagus-BlogSpot.git`
- Change directory to the project directory using  the `cd` command
- Open project on VSCode
- If you want to use virtualenv: `virtualenv ENV && source ENV/bin/activate`
- Install dependencies with pip: `pip install -r requirements.txt`
- Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app    ('development')
- Edit the export configurations `export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}`
- finally run `./start.sh`


## Technologies Used

- Python3.9
- Flask
- Flask-Bootstrap
- HTML
- CSS
- PostgreSQL


## link to live site on  HEROKU


## Support and contact details

| Njiiri | njerinjiiri@gmail.com|
| ----- | --------------------- |


### Known bugs 
- No known bugs but if any found contact me with details below:

### License

License
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) 2021 Yvonne Njiiri

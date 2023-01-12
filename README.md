# Social Media Backend API
This is the backend API for a social media application that allows users to post messages and "like" other users' messages. The API is built using Flask and PostgreSQL.

## Features
- Post a new message
- View a list of all messages, with the most recent messages first
- Like a message by clicking a button
- View the total number of likes for each message

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
- Python 3.x
- Flask
- Flask-SQLAlchemy
- psycopg2
- PostgreSQL

## Prerequisites
- Python 3.x
- Flask
- Flask-SQLAlchemy
- psycopg2
- PostgreSQL

## Installing
- Create a new virtual environment using the command `python -m venv envname`
- Activate the virtual environment using the command `envname/Scripts/activate`
- Install the required packages using the command `pip install -r requirements.txt`
- Create a new PostgreSQL database and run the SQL code provided in the SQL file to create the messages and likes tables and the trigger.
- Replace 'username','password','host','port','dbname' in the app.config['SQLALCHEMY_DATABASE_URI'] in the code with the appropriate values for your PostgreSQL database.
- Run the application by running the command `flask run` in your terminal.

## API Endpoints
- `POST /messages`: Create a new message
- `GET /messages`: Get a list of all messages
- `POST /messages/<int:message_id>/like`: Like a message
- `DELETE /messages/<int:message_id>/like`: Unlike a message

## Built With
- Flask - The web framework used
- PostgreSQL - The database used




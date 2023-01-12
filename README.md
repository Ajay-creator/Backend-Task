## Instructions for how to set up and run the API:

[-]Make sure you have Flask, Flask-SQLAlchemy, and psycopg2 (for connecting to PostgreSQL) installed.
[-] Create a new PostgreSQL database and run the SQL code provided in step 1 to create the messages and likes tables and the trigger.
[-] Replace 'username','password','host','port','dbname' in the app.config['SQLALCHEMY_DATABASE_URI'] in the code above with the appropriate values for your PostgreSQL database.
[-] Run the application by running the command flask run in your terminal.
[-] You should now be able to test the API by making POST and GET requests to the /messages endpoint to create and retrieve messages, and by making POST and DELETE requests to the /messages/<int:message_id>/like endpoint to like and unlike messages.
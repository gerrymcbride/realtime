# realtime
Real-Time Travel Info Demonstration Application

Built using Flask Micro Framework and Python 3.

In order to run successfully from a local server, this application requires the following modules which can be installed instantaneously using pip installation:

Flask,
flask-wtforms,
flask_bootstrap,
flask-mail
psycopg2

More information on Flask and it's various attributes and modules can be found at http://flask.pocoo.org/

SQLite3 is used in the application, as it is the standard Python database, although PostGreSQL is recommended for a more steadfast and sustainable solution. 

SQLite3 timetable contains 50 entries. For testing purposes, the default departure is "Dublin" with an option of two destinations; "Longford", "Belfast". Any updates can be made through accessing the database through the command line locally, or via Python script.

app.py contains an e-mail server information for clarity, efficiency and ease of demonstration, but on a live application should be stored in a config.py file.

E-mail functionality can be activated by entering in appropriate information, address & password, on line 21-22. Similarly, line 82 designates which e-mail address will receive any queries from contact forms.

Run app.py file through command line 'python app.py' to activate Flask server and view the application on a web-browser.

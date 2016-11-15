# realtime
Real-Time Travel Info Demonstration App

Built using Flask Micro Framework and Python 3.

In order to run successfuly from local server, this app requires the following modules which can be installed immediatley using pip installation:

Flask,
flask-wtforms,
flask_bootstrap,
flask-mail
psycopg2

SQLite3 is utilized in the app, as it is the standard Python database, although PostGres is recomended for a more steadfast and sustainable solution. 

SQLite3 timetable contains 50 entries. For testing purposes, default departure is "Dublin" with option of two destinations; "Longford", "Belfast". Any updates can be made through accessing database through the command line locally, or via Python script.

app.py contains e-mail server information for clarity, efficiency and ease of demonstration, but on a live app should be stored in config.py file.

E-mail can be activated by entering in appropriate information, address & password, on line 21-22. Similarly, line 82 designates which e-mail address wil recieve any queries from contact forms.

Run app.py file through command line 'python app.py' to activate Flask server and view webapp.

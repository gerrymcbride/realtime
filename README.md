# realtime
real-time travel info app

Built using Flask Micro framework.

Requires following modules which can be installed immediatley using pip:

Flask
flask-wtforms
flask_bootstrap
flask-mail

SQLite3 is utilized as the standard Python database, although PostGres is recomended for a more steadfast and sustainable solution.

SQLite3 timetable contains 50 entries. For testing purposes, default departure is "Dublin" with option of two destinations; "Longford", "Belfast". Any updates can be made through accessing database through the command line or Python script.

app.py contains e-mail server information for clarity, but on a live app should be stored in config.py file.
E-mail can be activated by entering in appropriate information, address & password, on line 21-22. Similarly, line 82 designates which e-mail address wil recieve any queries from contact forms.

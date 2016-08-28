from flask import Flask, render_template, request
import time
import datetime
from flask_wtf import Form
from threading import Thread
from flask.ext.mail import Mail, Message
from flask_bootstrap import Bootstrap
# sqlite3 used for testing DBs locally, psycopg2 should be used as a more permenant solition
import sqlite3





app = Flask(__name__)
app.config.update(
	DEBUG=True,
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'test26106@gmail.com',
	MAIL_PASSWORD = 'isthisjustfantasy'
	)
mail = Mail(app)




#home page
@app.route('/')
def index():
	return render_template("about.html")


#contact page
@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/services')
def services():
	return render_template("services.html")


#process request based on users input, default "departure" & DB table is Dublin.
@app.route('/about', methods=['POST'])
def about():

	try:
		departure = request.form['departure']
		arrival = request.form['arrival']

		timenow = (int(time.strftime('%H%M')))
		conn = sqlite3.connect('timetables')
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM Dublin WHERE Departing > ? AND Going_To = ?",(timenow, arrival))
		conn.commit()

		next_bus = cursor.fetchall()

		if next_bus == 0:
			render_template('error.html')

		else:
			return render_template('return.html', departure=departure, arrival=arrival, next_bus=next_bus, timenow=timenow)


	except:
		return ('error.html')


# processesing of contact form & query forwarding via email
@app.route('/submission', methods=['POST'])
def submission():

	name = request.form['name']
	email = request.form['email']
	question = request.form['question']


#subsituite recipient email with one of your choice
	msg = Message("Query", sender=email, recipients=["gerardamcbride@gmail.com"]) 
	msg.body=(question)
	mail.send(msg)

	return render_template("thankyou.html", name=name, email=email)




######################################################################################

#####################################################################################


if __name__ == "__main__":
    app.run(debug=True)
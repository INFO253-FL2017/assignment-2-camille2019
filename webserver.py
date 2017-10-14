"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # Render the template located in "templates/index.html"


@app.route('/about')
def about():

    return render_template('AboutUs.html')

@app.route('/contact',  methods = ['POST'])
def contact():
    return render_template('ContactUs.html')

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxcf68071789ba4d2ab3c5d8a60b43c954.mailgun.org/messages",
        auth=("api", "key-7e17ccf7a06dae27efb47c9024414ae2"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxcf68071789ba4d2ab3c5d8a60b43c954.mailgun.org>",
              "to": "Camille Harris <camilleharris@berkeley.edu>",
              "subject": request.form['subject'] ,
              "text": request.form['message']})


@app.route('/blog/8-experiments-in-motivation')
def motivation():
    return render_template('8ExperimentsInMotivation.html')

@app.route('/blog/a-mindful-shift-of-focus')
def focus():
    return render_template('AMindfulShiftOfFocus.html')

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def direction():
    return render_template('HowToDevelopAnAwesomeSenseOfDirection.html')

@app.route('/blog/training-to-be-a-good-writer')
def writer():
    return render_template('TrainingToBeAGoodWriter.html')

@app.route('/blog/what-productivity-systems-wont-solve')
def productivity():
    return render_template('WhatProductivitySystemsWontSolve.html')

"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/index')
def index():
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route('/about')
def about():
    return render_template('About Us.html')

@app.route('/contact')
def contact():
    return render_template('Contact Us.html')

@app.route('/blog/8-experiments-in-motivation')
def motivation():
    return render_template('8 Experiments in Motivation.html')
s
@app.route('/blog/a-mindful-shift-of-focus')
def focus():
    return render_template('A Mindful Shift of Focus.html')

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def direction():
    return render_template('How to Develop an Awesome Sense of Direction')

@app.route('/blog/training-to-be-a-good-writer')
def writer():
    return render_template('Training to be a Good Writer.html')

@app.route('/blog/what-productivity-systems-wont-solve')
def productivity():
    return render_template('What Productivity Systems Wont Solve')

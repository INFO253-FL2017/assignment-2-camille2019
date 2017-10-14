"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template("index.html") # Render the template located in "templates/index.html"

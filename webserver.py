"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "<h1>Hello World!</h1>"
					

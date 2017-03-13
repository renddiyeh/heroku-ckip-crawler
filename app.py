import os
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response

from src.parser import parse

app = Flask(__name__)
FlaskJSON(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'x5txPHff9PWF38xI41v4MS85JyjcY84r')

###
# Routing for your application.
###

@app.route('/')
def home():
    query = request.args.get('q')
    return json_response(result = parse(query))

if __name__ == '__main__':
    app.run()

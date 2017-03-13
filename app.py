import os
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json

from src.parser import parse

app = Flask(__name__)
FlaskJSON(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

###
# Routing for your application.
###

@app.route('/')
def home():
    query = request.args.get('q')

    return json_response(words = parse(query))

@app.errorhandler(404)
def page_not_found(error):
    return JsonError(error, code=404)

if __name__ == '__main__':
    app.run(debug=True)

from flask import request, jsonify
from app import app
from response_handler import action_handler

@app.route('/signup', methods = ['POST'])
def signup():
    return jsonify(action_handler("signup", request.form)), 201

@app.route('/verify', methods = ['PUT'])
def verify():

    pass


@app.route('/login', methods = ['POST'])
def login():

    pass


@app.route('/logout', methods = ['DELETE'])
def logout():

    pass

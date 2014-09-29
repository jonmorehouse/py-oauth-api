from flask import request
from app import app
from response_handler import action_handler

@app.route('/signup', methods = ['POST'])
def signup():

    action_handler("signup", request.form)
    pass

@app.route('/verify', methods = ['PUT'])
def verify():

    pass



@app.route('/login', methods = ['POST'])
def login():

    pass


@app.route('/logout', methods = ['DELETE'])
def logout():

    pass

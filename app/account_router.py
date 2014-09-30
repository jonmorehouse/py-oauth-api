from flask import request, jsonify, url_for, redirect

from app import app
from response_handler import action_handler

@app.route('/signup', methods=['POST'])
def signup():
    return redirect(url_for('create_account'), code=307)

@app.route('/account', methods=['POST'])
def create_account():
    return jsonify(action_handler("signup", request.form)), 201

@app.route('/account/<account_id>', methods=['GET'])
def retrieve_account(account_id):
    pass

@app.route('/account/<account_id>/activate', methods=['POST'])
def reactivate_account(account_id):

    pass

@app.route('/signup/<account_id>/activate', methods=['PUT'])
def activate_account(account_id):

    pass

@app.route('/account/<account_id>/deactivate', methods=['DELETE'])
def deactivate_account(account_id):

    pass

@app.route('/account/<account_id>/forgotten_password', methods=['POST'])
def forgotten_password(account_id):

    pass

@app.route('/account/<account_id>/change_password', methods=['PUT'])
def change_password(account_id):

    pass




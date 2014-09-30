from flask import request, jsonify, url_for, redirect

from app import app
from response_handler import action_handler

@app.route('/login', methods=['POST'])
def login():
    return redirect(url_for('create_session'), code=307)


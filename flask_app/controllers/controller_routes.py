from flask_app import app
from flask import render_template, redirect, session, request

@app.route('/')
def index():
    return render_template("users_login.html")

# @app.errorhandler(404)
# def server_error(e):
#     print("Running error function...")
#     return render_template("error.html")
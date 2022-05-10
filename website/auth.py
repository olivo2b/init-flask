from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/signin")
def signin():
    return "welcome"

@auth.route("/logout")
def logout():
    return "goodbye"

@auth.route("/login")
def login():
    return "welcomeagain"

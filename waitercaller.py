from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from flask.ext.login import LoginManager
from flask.ext.login import login_required

# from mockdbhelper import MockDBHelper as DBHelper
# from passwordhelper import PasswordHelper
# from user import User


app = Flask(__name__)
login_manager = LoginManager(app)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/account")
@login_required
def account():
	return "You are logged in"

	
if __name__ == '__main__':
	app.run(port=5000, debug=True)


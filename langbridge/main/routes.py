from flask import render_template, url_for, flash, redirect, request, Blueprint
from langbridge import db
from langbridge.main.forms import SignUpForm
from langbridge.models import User

bp_main = Blueprint('main', __name__)


@bp_main.route("/")
@bp_main.route("/index", methods=['POST', 'GET'])
def home():
    return render_template('index.html', title='Index')


@bp_main.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('signup.html', title='Sign Up', form=form)




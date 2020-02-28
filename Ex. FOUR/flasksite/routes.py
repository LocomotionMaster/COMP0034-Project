from flask import render_template, url_for, flash, redirect, request
from flasksite import app, db
from flasksite.forms import SignUpForm
from flasksite.models import User, Forecast

@app.route("/")
@app.route("/index", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        term = request.form['search']
        if term == "":
            flash("Enter a post to search for")
            return redirect('/')
        results = db.session.query(Forecast).filter(Forecast.forecast.contains(term)).all()
        if not results:
            flash("No posts found with that name.")
            return redirect('/')
        return render_template('post.html', posts=results)
    else:
        return render_template('index.html', title='Index')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route("/post")
def post():
    posts = Forecast.query.all()
    return render_template('post.html', title='Posts', posts=posts)
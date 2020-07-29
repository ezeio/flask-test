from datetime import datetime
from app.form.nameform import NameForm

from flask import Flask, request, current_app, make_response, render_template, url_for, session, redirect
from flask_moment import Moment as Moment

from app.form.registration import Registration
from app.model.user import User
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ositadinma'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route("/")
def index():
    # print(url_for('static', filename='css./styles.css', _external=True))
    return render_template('index.html', current_time=datetime.utcnow())


@app.route("/name")
def name():
    response = make_response("<h1>My name is what? check cookie</h1>")
    response.set_cookie('name', 'osy')
    response.status_code = 500
    return response


@app.route("/useragent")
def user_agent():
    user_agent = request.headers.get("User-Agent")
    print(request.method)
    print(request.get_json())
    print(request.blueprint)
    return f"<p>The browser is: {user_agent}</p>"


@app.route("/user/<name>")
def user(name):
    user = User(name, ["Story", "Spanish Harlem", "Little Italy"])
    print("We got here with query string -> {request.query_string()}")
    return render_template('user.html', user=user)


@app.route("/form", methods=['GET', 'POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        for aSession in session:
            print(f"session_value: {aSession}")
        session['name'] = form.name.data
        return redirect(url_for("form"))
    return render_template('formname.html', form=form, name=session.get('name'))


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    form = Registration()
    if form.validate_on_submit():
        session['first_name'] = form.first_name.data
        return redirect(url_for("account"))
    return render_template('registration.html', form=form)


@app.route("/account", methods=['GET'])
def account():
    return render_template("account.html", first_name=session.get('first_name'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

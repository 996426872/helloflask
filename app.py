from flask import Flask, url_for, render_template, flash, redirect
from flask import make_response
from forms import LoginForm
import os
from flask_bootstrap import Bootstrap


app = Flask(__name__)
# csrf
# 为了增强安全性，密钥不应该直接写入代码，而要保存到环境变量中
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
# bootstrap实例
bootstrap = Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404


@app.route('/basic', methods=['GET', 'POST'])
def basic():
    form = LoginForm()
    return render_template('basic.html', form=form)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/user/', defaults={'name': 'Programmers'})
@app.route('/user/<name>')
def user(name):
    name = "Yang Li"
    return render_template("user.html", name=name)


@app.route('/watchlist')
def watchlist():
    user = {
        "username": "Yang Li",
        "bio": "Mama who loves cooking and movies."
    }
    movies = [
        {"name": "My Neighbor Totoro", "year": "1988"},
        {"name": "Three Colours trilogy", "year": "1993"},
        {"name": "Forest Gump", "year": "1994"},
        {"name": "Perfect Blue", "year": "1997"},
        {"name": "The Matrix", "year": "1999"},
        {"name": "Memento", "year": "2000"},
        {"name": "The Bucket list", "year": "2007"},
        {"name": "MBlack Swan", "year": "2010"},
        {"name": "MGone Girl", "year": "2014"},
        {"name": "CoCo", "year": "2017"}
    ]
    return render_template("watchlist.html", user=user, movies=movies)




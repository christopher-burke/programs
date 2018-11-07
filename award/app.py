#!/usr/bin/env python3

"""Award application."""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/start")
def start():
    return render_template('timer.html')


@app.route("/begin")
def begin():
    award = request.args.get('award')
    task = request.args.get('task')
    return render_template('timer.html', **{'award': award, 'task': task})

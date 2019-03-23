import sqlite3
from flask import Flask, g, render_template
from . import config

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)


@app.before_request
def before_request():
    g.db = connect_db()


@app.route('/')
def Ai_world():
    cursor = g.db.execute('SELECT id, name FROM member;')
    members = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    return render_template('database/members_template_engine.html', members=members)

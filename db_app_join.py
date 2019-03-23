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
def AI_world():
    cursor = g.db.execute("""
        SELECT a.id, a.name, c.name
        FROM author a INNER JOIN country c ON a.country_id = c.id;
    """)
    members = [dict(id=row[0], name=row[1], country=row[2])
               for row in cursor.fetchall()]
    return render_template('database/members_with_join.html', members=members)

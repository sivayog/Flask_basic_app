from flask import Flask
from flask import render_template  # !Important

app = Flask(__name__)


@app.route('/')
def AI_world():
    member_name = "siva"
    return render_template('ai.html', member_name= member_name)

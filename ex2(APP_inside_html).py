from flask import Flask

app = Flask(__name__)


@app.route('/')
def AI_world():
    html = """
        <html>
            <h1>Welcome to our AI WORLD!</h1>
        </html>
    """
    members = ["siva", "ram", "ragav"]
    # build an <ul> with members
    return html

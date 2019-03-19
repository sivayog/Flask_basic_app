from flask import Flask
from flask import render_template_string  #!Important

app = Flask(__name__)


@app.route('/')
def AI_world():
    member_name = "ram"
    html = """
        <html>
            <h1>HELLO {{member_name}} members!</h1>
        </html>
    """
    rendered_html = render_template_string(html, library_name=library_name)
    members = ["siva", "ram", "ragav"]
    # Using an <ul> tag add the members using the template engine
    return rendered_html

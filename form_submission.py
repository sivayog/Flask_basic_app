from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def AI_world():
    if request.method == 'GET':
        return render_template('forms/form.html')
    elif request.method == 'POST':
        members = {
            'name': request.form['name'],
            'address': request.form['adress'],
            'city': request.form['city'],
            'street_no': request.form['street_no'],
            'pin_code': request.form['submit'],
        }
        return render_template(
            'forms/form_result.html', **members)

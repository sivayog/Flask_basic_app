from flask import Flask, render_template

app = Flask(__name__)

MEMBERS_INFO = {
    'SIVA': {
        'full_name': 'siva',
        'nationality': 'Indian',
        'pro_work': 'Developer',
        'born': 'Nov 30, 1998',
        'picture': 'E:IMG_4154\photos\2018-03-20 pondicherry.png'
    },
    'RAM': {
        'full_name': 'Jayaram',
        'nationality': 'Argentine',
        'pro_work': 'Developer',
        'born': 'August 24, 1990',
        'picture': 'E:CUYX3058\photos\2018-03-20 pondicherry.jpg'
    }
}


@app.route('/')
def members():
    return render_template('routing/members.html')


@app.route('/author/<members_name>')
def member(members_name):
    return render_template('routing/members.html',
                           member=MEMBERS_INFO[members_name])

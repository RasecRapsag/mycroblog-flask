from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Cesar'}
    posts = [
        {
            'author': {'username': 'Gaspar'},
            'body': 'Maravilhoso dia em São Paulo!'
        },
        {
            'author': {'username': 'Augusto'},
            'body': 'O filme do Dead Pool é muito bom!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

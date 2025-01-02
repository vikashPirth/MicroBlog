from flask import render_template
from app import app 



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vikash'}
    posts = [
        {
            'author':{'username':'John'},
            'body':'Beautiful day in Germany'
        },
        {
            'author':{'username':'Bob'},
            'body':'First day in Pakistan was Awesome'
        }
    ]
    return render_template('index.html', user=user, posts=posts)

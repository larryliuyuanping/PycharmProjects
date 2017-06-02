from flask import Flask,render_template,request
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self,url_map,items):
        super(RegexConverter,self)
        self.regex=items[0]
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html',title='welcome!')
@app.route('/services')
def services():
    return 'Services'

@app.route('/about')
def about():
    return 'About'

# @app.route('/user/<regex("[a-z]{3}"):username>')
# def user(username):
#     return 'User %s' %username

@app.route('/about')
def about():
    return 'About'
@app.route('/projects')
@app.route('/our-works')
def projects():
    return 'The project page'


def login():
    return render_template('login.html', method=request.mehthod)

if __name__ == '__main__':
    app.run(debug=True)

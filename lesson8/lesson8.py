from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('todolist.html')
@app.route('/Service')
def service():
    return 'Service'
@app.route('/About')
def about():
    return 'About'
@app.route('/user/<int:user_id>')
def user(user_id):
    return 'user%d'% user_id
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        return render_template('login,html',method=request.method)
    else:
         username=request.args['username']
    return  render_template('login.html',method=request.method)

def upload():
    if request.method=='POST':
        f = request.files['flie']
        basepath = path.join(basepath,'static/upload')
@app.route('/')
def index():
    response =make_response(render_template(index.html))
    res




if __name__ == '__main__':
    app.run(debug=True)

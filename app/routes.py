from app import app
from flask import render_template



@app.route('/home', methods=['POST','GET'])
@app.route('/', methods=['POST', 'GET'])
def home():
    title = 'HOME'
    return render_template('home.html', title=title)

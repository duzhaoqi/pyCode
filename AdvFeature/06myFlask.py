from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="http://www.w3school.com.cn">w3school</a>'

@app.route('/info')
def myinfo():
    return render_template('pay.html',name = "杜肇启")

app.run()
import sys
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/etc')
def etc():
    return render_template('etc.html')
@app.route('/etc/goldbach')
def goldbach():
    return render_template('goldbach.html')
@app.route('/etc/collatz')
def collatz():
    return render_template('collatz.html')



if __name__=="__main__":
    app.run()
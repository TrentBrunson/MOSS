import pickle
from joblib import dump, load
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# start home page
@app.route('/')
def index():
    return render_template('index.html')


# create modules
@app.route('/headcount', methods=['POST'])
def headcount():
    return render_template('headcount.html')


@app.route('/financials', methods=['POST'])
def financials():
    return render_template('financials.html')


@app.route('/platform', methods=['POST'])
def platform():
    return render_template('platform.html')


@app.route('/calcs', methods=['POST'])
def calcs():
    return render_template('calcs.html')

if __name__=="__main__":
    app.run()



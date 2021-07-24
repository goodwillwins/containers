from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello() :
    return '<p>Test</p>'
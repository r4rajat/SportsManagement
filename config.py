from flask import Flask

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', "*")
    response.headers.add('Access-Control-Allow-Methods', 'DELETE')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization, X-Access-Token, data')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Content-Type', 'application/json')
    return response

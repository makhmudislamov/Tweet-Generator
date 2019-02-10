from flask import Flask
from stoc_sample import test_iteration
app = Flask(__name__)


@app.route('/')
def hello_world():
    return test_iteration(histogram, 10000)


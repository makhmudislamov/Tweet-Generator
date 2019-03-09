from flask import Flask
from markov_chain import *
import cleaner
from cleaner import file_cleaner



app = Flask(__name__)

@app.route('/')
def index():
    txt = file_cleaner(cleaner.file)
    m_chain = Second_Order_Markov_Chain(txt)
    return m_chain.random_sentence(10)

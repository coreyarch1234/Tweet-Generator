from flask import Flask
from histogram import Hashtogram
app = Flask(__name__)

@app.route('/')
def hello_world():
    histogram = Hashtogram()
    sentence = histogram.generate_random_sentence(5)
    return sentence

if __name__ == '__main__':
    app.run()

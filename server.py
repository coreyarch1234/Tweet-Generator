from flask import Flask
from histogram import Hashtogram
app = Flask(__name__)

@app.route('/')
def hello_world():
    return histogram.generate_random_sentence(5)

if __name__ == '__main__':
    app.run()

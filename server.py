from flask import Flask
from histogram import Hashtogram
app = Flask(__name__)

@app.route('/')
def hello_world():
    histogram = Hashtogram()
    print(histogram.generate_random_sentence(3))

if __name__ == '__main__':
    app.run()

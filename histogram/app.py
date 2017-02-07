import stochastic
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return stochastic.random_word_weighted('stochastic_random.txt')

if __name__ == '__main__':
    app.run(debug=True)

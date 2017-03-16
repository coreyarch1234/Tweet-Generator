from flask import Flask
# from histogram import Hashtogram
app = Flask(__name__)

@app.route('/')
def generate_sentence():
    from histogram import Hashtogram
    histogram = Hashtogram()
    histogram.generate_triple()
    histogram.create_markov_chain()
    sentence = histogram.generate_random_sentence(2)
    return sentence

if __name__ == '__main__':
    app.run()

# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

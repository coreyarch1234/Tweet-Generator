from flask import Flask
app = Flask(__name__)

@app.route('/')
def generate_sentence():
    from histogram import Hashtogram
    histogram = Hashtogram()
    histogram.generate_triple()
    histogram.create_markov_chain()
    sentence = histogram.generate_random_sentence(50)
    return sentence

if __name__ == '__main__':
    app.run()

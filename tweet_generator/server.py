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

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run()

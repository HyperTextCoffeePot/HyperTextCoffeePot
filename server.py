from flask import Flask

from pot import Pot


app = Flask(__name__)
pot = Pot('teapot')


@app.route('/teapot', methods=['GET'])
def get():
    return pot.get()


@app.route('/teapot', methods=['BREW', 'POST'])
def brew():
    return pot.brew()


@app.route('/teapot', methods=['WHEN'])
def when():
    return pot.when()


if __name__ == '__main__':
    app.run(port=8081)

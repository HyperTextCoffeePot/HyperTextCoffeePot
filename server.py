from flask import Flask

import pots


app = Flask(__name__)
pot = pots.RaspCoffeePot('coffee', 10, 24)


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

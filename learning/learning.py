#!/usr/bin/python




from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'


@app.route('/user/<username>')
def profile(username):
    pass


if __name__ == '__main__':
    app.debug = True

    with app.test_request_context():
        print url_for('index')
        print url_for('profile', username='John Doe')


    app.run()


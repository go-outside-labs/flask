from flask import Flask, request, render_template, url_for, redirect
from hash_function import hashFunction




app = Flask(__name__)
URL_TABLE = {}




@app.route('/', methods = ['GET'])
@app.route('/index', methods=['GET'])
def homepage():
    return render_template('index.html')



@app.route('/short', methods = ['POST'])
def find_short_url():
    long_url = request.form['url']
    key = hashFunction(long_url)
    URL_TABLE[key] = long_url
    short_url = HOST + key
    return render_template('shorturl.html', new_url=short_url)





@app.route('/<key>', methods=['GET'])
def redirect_short_url(key):
    try:
        long_url = URL_TABLE[key]
        return redirect(long_url, code=302)
    except:
        return redirect(url_for('error404'))





@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    HOST = 'localhost:5000/'
    app.run()

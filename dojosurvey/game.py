import random
from flask import Flask, render_template, request, redirect,session  # added request


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def create_user():
    name = request.form['name']
    location =request.form['dojolocation']
    lang = request.form['lang']
    comment = request.form['comment']
    return render_template('result.html', name=name, location=location, lang=lang, comment=comment,)


if __name__=="__main__":
    app.run(debug=True)


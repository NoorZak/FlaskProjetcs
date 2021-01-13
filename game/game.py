import random
from flask import Flask, render_template, request, redirect,session  # added request


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

def gm(p1, p2):
    sen = {
        'rock': {'rock': 'tie', 'paper': 'lose', 'scissors': 'win'},
        'paper': {'rock': 'win', 'paper': 'tie', 'scissors': 'lose'},
        'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'tie'}
    }
    return sen[p1][p2]


@app.route('/')
def index():
    session["win"]=0
    session["lose"]=0
    session["tie"]=0
    return render_template("game.html")


@app.route('/game', methods=['POST'])
def create_user():
    x = request.form['game']
    arr = ["rock", "paper", "scissors"]
    z = random.randint(0, 2)
    y = random.choice(arr)
    if gm(x, y)=="win":
        session["win"] += 1
    if gm(x, y)=="lose":
        session["lose"] += 1
    if gm(x, y)=="tie":
        session["tie"] += 1

    return render_template('game.html', you=x, win=session['win'], lose=session['lose'], tie=session['tie'],result=gm(x, y))

if __name__=="__main__":
    app.run(debug=True)


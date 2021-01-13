import random
from flask import Flask, render_template, request, redirect,session  # added request


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1

    return render_template("game.html",count=session["count"])

@app.route("/destroy_session")
def destroy_session():
    session.pop("count")
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)


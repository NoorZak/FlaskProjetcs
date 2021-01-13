from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')


def index(num =3 ,col ="blue"):
    return render_template("index.html", phrase="Welcome",times=int(num),color=col)	# notice the 2 new named arguments!

if __name__=="__main__":
    app.run(debug=True)



from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index():
    return render_template("index.html",rows=8,cols=8,color1 ="red",color2="black")	# notice the 2 new named arguments!


@app.route('/play/<rows>')
def index1(rows):
    return render_template("index.html",rows=int(rows),cols=8,color1 ="red",color2="black")	# notice the 2 new named arguments!

@app.route('/play/<rows>/<cols>')
def index2(rows,cols):
    return render_template("index.html",rows=int(rows),cols=int(cols),color1 ="red",color2="black")	# notice the 2 new named arguments!

@app.route('/play/<rows>/<cols>/<color1>/<color2>')
def index3(rows,cols,color1,color2):
    return render_template("index.html",rows=int(rows),cols=int(cols),color1 =color1,color2=color2)	# notice the 2 new named arguments!


if __name__=="__main__":
    app.run(debug=True)



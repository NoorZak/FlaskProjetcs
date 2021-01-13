from flask import Flask, render_template, request, redirect,session
from mysqlconnection import connectToMySQL  # import the function that will return an instance of a connection

app = Flask(__name__)


@app.route("/")
def index():

    mysql = connectToMySQL('books')  # call the function, passing in the name of our db
    books = mysql.query_db('SELECT * FROM book;')  # call the query_db function, pass in the query as a string

    return render_template("index.html", books=books)

@app.route("/delete/",methods=['POST'])
def index1():
   print(request.form)
   return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

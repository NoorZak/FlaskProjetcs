from flask import Flask, render_template, redirect, request, session, flash,url_for
from mysqlconnection import connectToMySQL  # import the function that will return an instance of a connection
import re
import datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

# @app.route('/addBook')
# def bookForm():
#     return render_template ("add_book.html")

# @app.route('/insertBook', methods=['POST'])
# def insertBook():
#     mysql = connectToMySQL('book_store')
#     mysql.query_db(f'INSERT INTO book (book_name,book_author) VALUES("{request.form["bookName"]}","{request.form["bookAuthor"]}");')
#     return redirect ("/")

@app.route('/delete/<emailId>')
def deleteMethod(emailId):
    mysql = connectToMySQL('emails')
    mysql.query_db(f'DELETE FROM emails WHERE id={int(emailId)};')
    return redirect ("/success")

@app.route('/check', methods=['POST'])
def checkEmail():
    mysql = connectToMySQL('emails')
    email=request.form['email']
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
    if not EMAIL_REGEX.match(email):
        flash("Invalid email address!")
        return redirect ("/")
    elif len(mysql.query_db(f'SELECT * FROM emails WHERE email = "{email}";'))>0:
        flash("email already exists!")
        return redirect ("/")
    else:
        mysql = connectToMySQL('emails')
        mysql.query_db(f'INSERT INTO emails (email) VALUES("{request.form["email"]}");')
        flash(f"The email address you entered {request.form['email']} is a VALID email address! Thank You!")
        return redirect("/success")

@app.route('/success')
def showTableOfEmails():
    mysql = connectToMySQL('emails')
    emails = mysql.query_db('SELECT * FROM emails;')
    return render_template("success.html",emails=emails)

@app.route('/')
def index():
    return render_template ("index.html")
    
if __name__=="__main__":
    app.run(debug=True)

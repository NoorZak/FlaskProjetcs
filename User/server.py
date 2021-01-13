from flask import Flask, render_template,redirect,request
from mysqlconnection import connectToMySQL  # import the function that will return an instance of a connection
app = Flask(__name__)


@app.route("/")
def index():
    mysql=connectToMySQL("users")
    query="SELECT * FROM user;"
    informationUser=mysql.query_db(query)

    return render_template("index.html",allInfo=informationUser)


@app.route("/adduser" ,methods=["POST"])
def adduser():
    mysql=connectToMySQL("users")
    query = "INSERT INTO user (first_name,last_name,email) VALUES (%(fn)s,%(ln)s,%(email)s);"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "email": request.form["email"]
    }
    result=mysql.query_db(query, data)
    mysql=connectToMySQL("users")
    queryInfo=f"select * from user where id ={result};"
    userInfo=mysql.query_db(queryInfo)
    return render_template("showInfoUser.html",userInfo=userInfo)

@app.route("/add_a_new_user")
def addAnewUser():
    return render_template("add_a_new_user.html")

@app.route("/show/<id>")
def showUserInfo(id):
    mysql = connectToMySQL("users")
    queryInfo = f"select * from user where id ={id};"
    userInfo = mysql.query_db(queryInfo)
    return render_template("showInfoUser.html",userInfo=userInfo)


@app.route("/edit/<id>")
def edit(id):
    return render_template("editUserInfo.html",id=id)


@app.route("/editUserInfo/<id>",methods=["POST"])
def editUserInfo(id):
    mysql = connectToMySQL("users")
    query=f"UPDATE `user` SET `first_name` = %(fn)s, `last_name` = %(ln)s, `email` = %(email)s WHERE (`id` = {id});"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "email": request.form["email"]
    }

    res=mysql.query_db(query, data)
    print(res)
    return  redirect("/")



@app.route("/delete/<id>")
def delete(id):
    mysql=connectToMySQL("users")
    query=f"delete from user where id ={id}"
    mysql.query_db(query)
    return redirect("/")





if __name__ == "__main__":
    app.run(debug=True)

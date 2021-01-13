from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    return 'Dojo'



@app.route('/say/<name>')          # The "@" decorator associates this route with the function immediately following
def say(name):
    return f"Hello {name}"


@app.route('/repeat/<n>/<name>')          # The "@" decorator associates this route with the function immediately following
def repreat(n,name):
    str=""
    for i in range(int(n)):
        str+=f"{name}"
        str+="<br>"
    return str


    # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)
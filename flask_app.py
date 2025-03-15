from flask import Flask

app= Flask(__name__)  #Create a Flask app instance

@app.route("/")  #Define a route for the home page
def home():
    return "Hello, Rafiki! Welcome to your Flask App!"

if __name__ == '__main__':  #Run app
    app.run(debug=True)

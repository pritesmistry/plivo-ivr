from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/answer", methods=["GET", "POST"])
def answer():
    return "PLIVO TEST WORKING"

if __name__ == "__main__":
    app.run()

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/answer", methods=["GET","POST"])
def answer():

    xml = """
<Response>
<Dial callerId="+912269988681">
    <Number>+918087153266</Number>
</Dial>
</Response>
"""

    return xml, 200, {'Content-Type': 'text/xml'}

if __name__ == "__main__":
    app.run()

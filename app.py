from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"


@app.route("/answer", methods=["GET", "POST"])
def answer():

    xml = """
<Response>
<GetInput action="https://plivo-ivr-qskz.onrender.com/ivr" method="POST" numDigits="1">
    <Speak>Welcome to Bio Leather. Press 1 for sales. Press 2 for support.</Speak>
</GetInput>
</Response>
"""

    return xml, 200, {'Content-Type': 'text/xml'}


@app.route("/ivr", methods=["GET", "POST"])
def ivr():

    digit = request.form.get("Digits")

    if digit == "1":

        xml = """
<Response>
<Dial>+918087153266</Dial>
</Response>
"""

    elif digit == "2":

        xml = """
<Response>
<Speak>Please email support at bioleather dot in</Speak>
</Response>
"""

    else:

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

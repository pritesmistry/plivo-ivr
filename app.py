from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Server running"


@app.route("/answer", methods=["GET", "POST"])
def answer():

    xml = """
<Response>
<GetInput action="https://plivo-ivr-qskz.onrender.com/ivr" method="POST" numDigits="1" timeout="10">
    <Speak>Welcome to Bio Violet. Press 1 for sales. Press 2 for support.</Speak>
</GetInput>

<Speak>No input received. Goodbye.</Speak>
</Response>
"""

    return xml, 200, {'Content-Type': 'text/xml'}


@app.route("/ivr", methods=["GET", "POST"])
def ivr():

    digit = request.form.get("Digits")

    print("Digit:", digit)

    if digit == "1":

        xml = """
<Response>
<Dial>
    <Number>+918087153266</Number>
</Dial>
</Response>
"""

    elif digit == "2":

        xml = """
<Response>
<Speak>Please email support at bioviolet dot in</Speak>
</Response>
"""

    else:

        xml = """
<Response>
<Speak>Invalid input</Speak>
</Response>
"""

    return xml, 200, {'Content-Type': 'text/xml'}


if __name__ == "__main__":
    app.run()

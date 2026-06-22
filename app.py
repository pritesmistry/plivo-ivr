from flask import Flask, request

app = Flask(__name__)


# Home route
@app.route("/")
def home():
    return "Hello - Server Working"


# Incoming call route
@app.route("/answer", methods=["GET", "POST"])
def answer():

    print("CALL HIT /answer")
    print("FORM DATA:", request.form)

    xml = """
<Response>
<GetInput action="https://plivo-ivr-qskz.onrender.com/ivr" method="POST" numDigits="1">
    <Speak>Welcome to Bio Violet. Press 1 for sales. Press 2 for support.</Speak>
</GetInput>
</Response>
"""

    return xml, 200, {'Content-Type': 'text/xml'}


# After user presses a digit
@app.route("/ivr", methods=["GET", "POST"])
def ivr():

    print("CALL HIT /ivr")
    print("FORM DATA:", request.form)

    digit = request.form.get("Digits")

    print("DIGIT RECEIVED:", digit)

    # Debug mode: just speak back what was pressed
    if digit == "1":

        xml = """
<Response>
<Speak>You pressed 1. Sales selected.</Speak>
</Response>
"""

    elif digit == "2":

        xml = """
<Response>
<Speak>You pressed 2. Please email support at bioviolet dot in.</Speak>
</Response>
"""

    else:

        xml = f"""
<Response>
<Speak>I did not receive a valid input. Received {digit}</Speak>
</Response>
"""

    return xml, 200, {'Content-Type': 'text/xml'}


if __name__ == "__main__":
    app.run()

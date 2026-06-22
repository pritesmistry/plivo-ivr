from flask import Flask, request
from plivo import plivoxml

app = Flask(__name__)

@app.route("/answer", methods=["GET", "POST"])
def answer():

    response = plivoxml.ResponseElement()

    get_input = plivoxml.GetInputElement(
        action="/ivr",
        method="POST",
        num_digits=1
    )

    get_input.add(
        plivoxml.SpeakElement(
            "Welcome to Bio Violet. Press 1 for sales. Press 2 for support."
        )
    )

    response.add(get_input)

    return str(response)


@app.route("/ivr", methods=["GET", "POST"])
def ivr():

    digit = request.form.get("Digits")

    response = plivoxml.ResponseElement()

    if digit == "1":

        dial = plivoxml.DialElement()
        dial.addNumber("+918087153266")
        response.add(dial)

    elif digit == "2":

        response.add(
            plivoxml.SpeakElement(
                "Please email support at bioleather dot in"
            )
        )

    return str(response)


if __name__ == "__main__":
    app.run()

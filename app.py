from flask import Flask
from flask import render_template
from flask import request

from src.adaptive_rag import adaptive_medical_chat


app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot():

    question = request.form["msg"]

    response = adaptive_medical_chat(
        question
    )

    return response


if __name__ == "__main__":

    app.run(debug=True)
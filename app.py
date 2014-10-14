#!/usr/bin/python
from flask import Flask, render_template
from collections import Counter

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/results")
def results():
    #question = THE QUESTION
    #answer = THE RESULTS
    return render_template("results.html", question=question, answer=answer)

if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0", port=1900)
    app.run()

#!/usr/bin/python
from flask import Flask, render_template, request
from collections import Counter
import getResults

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def main():
    
    if request.method == "POST":
        question = request.form["question"]
        if question != None:
            answer = getResults.get_results(question)
            return render_template("results.html", question=question, answer=answer)
    return render_template("home.html")

if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0", port=1900)
    app.run()

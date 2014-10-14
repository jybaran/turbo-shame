#!/usr/bin/python
from flask import Flask, render_template, request
from collections import Counter
import getResults

app = Flask(__name__)


@app.route("/")
def main():
    question = request.args.get("question",None)
    if question != None:
        answer = getResults.everything(question)
        return render_template("results.html", question=question, answer=answer)
    #
    #else:
     #   return render_template("home.html")
    return render_template("home.html")

if __name__ == "__main__":
    app.debug=True
    #app.run(host="0.0.0.0", port=1900)
    app.run()

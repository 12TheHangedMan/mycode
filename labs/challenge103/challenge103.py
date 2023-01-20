#!/usr/bin/env python3

from flask import Flask, redirect, request, render_template, abort, url_for
import requests
import random
import json

app = Flask(__name__)
app.template_folder = "./"


fakeurl = "https://opentdb.com/api.php?amount=1"

correct_answer = ""


def generate_question():
    response = requests.get(fakeurl).json()
    results = response.get("results")
    result = {}

    if len(results) > 0:
        result = results[0]

    return result


def generate_html():
    result = generate_question()

    if len(result) > 0:
        question = result.get("question")

        global correct_answer
        correct_answer = result.get("correct_answer")
        answer_list = result.get("incorrect_answers")

        answer_list.append(correct_answer)
        answer_list = randomize(answer_list)

        html_content = f'<html>\
                <head><title>challenge 103</title></head>\
                <body>\
                <form action = "/post_answer" method = "POST">\
                    <p><h3>{question}</h3></p>'

        option = ["A", "B", "C", "D", "E", "F", "G"]
        index = 0

        html_content_middle = ""
        for answer in answer_list:
            html_content_middle += f'<p><input type="radio" name="answer" value="{answer}"/>{option[index]}. {answer}</p>'
            index += 1

        html_content_end = '<p><input type = "submit"/></p>\
            </form></body></html>'

        html_content = html_content + html_content_middle + html_content_end

    return html_content


def randomize(lists):
    for i in range(len(lists)):
        random_index = random.randint(0, len(lists)-1)

        temp = lists[i]
        lists[i] = lists[random_index]
        lists[random_index] = temp

    return lists


@app.route("/")
def get_question():
    contents = generate_html()
    if (contents == "" or contents == None):
        abort(404)
    else:
        return render_template("/challenge103_index.html", content=contents)


@app.route("/post_answer", methods=["POST"])
def post_answers():
    if request.method == "POST":
        if request.form["answer"] == correct_answer:
            return redirect("/correct")
        else:
            return redirect("/incorrect")


@app.route("/correct")
def get_correct():
    return "correct"


@app.route("/incorrect")
def get_incorrect():
    return "incorrect"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)


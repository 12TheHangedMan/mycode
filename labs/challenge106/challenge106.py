#!/usr/bin/env python3
from flask import Flask, redirect, request, render_template, abort, session, make_response
import random
import challenge106appendix

app = Flask(__name__)
app.template_folder = "./templates_lab106"
app.secret_key = "serial9"

# load question library
questions_list = challenge106appendix.generate_question()


def player_session_generate():
    player = getcookie()
    random_question_obj = random.choice(questions_list)
    question = random_question_obj.get("question")
    answers_list = random_question_obj.get("answers_list")
    answers_list = challenge106appendix.randomize(answers_list)
    correct_answer = random_question_obj.get("correct_answer")

    # initialize the player information
    session[player] = {"player_name": player,
                       "question": question,
                       "answers_list": answers_list,
                       "correct_answer": correct_answer}


@app.route("/trivia_game", methods=["POST", "GET"])
def load_trivia_game():
    # load player name from cookie
    player = getcookie()
    # if player doesn't have cookie, meaning initialization failed
    if player is None:
        return render_template("./challenge106_login.html", err="falied to validate")

    if request.method == "POST":
        # here cannot make comparasion directly because the safe html content issue
        player_answer = request.form.get("answer")
        correct_answer = session.get(player).get("correct_answer")

        return render_template("./challenge106_response.html",
                               player=player,
                               correct_answer=correct_answer,
                               player_answer=player_answer)

    if request.method == "GET":
        # --- load player information from session, to avoid user go to the page without login
        player_session_generate()

        if player not in session or len(questions_list) == 0:
            return redirect("./", err="something is not right, try again")

        question = session.get(player).get("question")
        answers_list = session.get(player).get("answers_list")
        correct_answer = session.get("correct_answer")

        return render_template("./challenge106_trivia_index.html",
                               player=player,
                               question=question,
                               answers_list=answers_list,
                               correct_answer=correct_answer)


@app.route("/")
@app.route("/login", methods=["GET"])
def player_login():
    session.clear()  # just for debugging, because session's data structure may be modified and can cause serious bug
    if request.method == "GET":
        return render_template("./challenge106_login.html")


@app.route("/setcookie", methods=["POST"])
def setcookie():
    if request.method == "POST":
        if request.form.get("player_name"):
            playername = request.form.get("player_name")
            # set cookies for player
            resp = make_response(redirect("/trivia_game"))
            resp.set_cookie("player_name", playername)

            return resp
        else:
            return render_template("./challenge106_login.html", error="User Name Cannot Be EMPTY")


def getcookie():
    return request.cookies.get("player_name")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

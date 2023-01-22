#!/usr/bin/env python3
from flask import Flask, redirect, request, render_template, session, make_response
import random
import math

app = Flask(__name__)
app.template_folder = "./templates_lab106"
app.secret_key = "serial9"


def player_session_generate(player):
    random_pow = random.randint(1, 2)
    random_number = random.randint(1, 10**random_pow)

    hp = math.floor(math.log2(random_number))
    # initialize the player information
    session[player] = {"player_name": player,
                       "random_number": random_number,
                       "upper_limit": math.floor(10**random_pow),
                       "hp": hp}


@app.route("/guess_number", methods=["POST", "GET"])
def load_game():
    player = getcookie()
    # if player doesn't have cookie, meaning initialization failed
    if player is None:
        return render_template("./challenge106_login.html", err="falied to validate")

    player_answer = "n/a"
    if request.method == "POST":
        try:
            player_answer = request.form.get("answer")
            player_answer = int(player_answer)
        except:
            player_answer = "invalid"

        if session.get(player).get("hp") > 0:
            hp = session[player]["hp"] - 1
            number = session[player]["random_number"]
            limit = session[player]["upper_limit"]

            session[player] = {"player_name": player,
                               "random_number": number,
                               "upper_limit": limit,
                               "hp": hp}
            return render_template("./challenge106_guess_number.html", p1=session.get(player), player_answer=player_answer)
        else:
            return render_template("./challenge106_GAMEOVER.html")
    if request.method == "GET":
        return render_template("./challenge106_guess_number.html", p1=session.get(player), player_answer=player_answer)


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
            resp = make_response(redirect("/guess_number"))
            resp.set_cookie("player_name", playername)

            player_session_generate(playername)

            return resp
        else:
            return render_template("./challenge106_login.html", err="User Name Cannot Be EMPTY")


def getcookie():
    return request.cookies.get("player_name")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

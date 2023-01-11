#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


def print_challenge_func():
    print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")

def print_trial_func():
    print(f"My {trial[2]['goggles']}! The {trial[2]['eyes']} do {trial[3]}!")

def print_nightmare_func():
    print(f"My {nightmare[0]['user']['name']['first']}! The {nightmare[0]['kumquat']} do {nightmare[0]['d']}")

print_challenge_func()

print_trial_func()

print_nightmare_func()



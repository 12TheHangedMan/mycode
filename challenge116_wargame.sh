#!/bin/bash

echo "Good morning, Professor Falken."

echo "
Would you like to play a game?"

read -p "Enter 'yes' or 'no': " RESPONSE

if [ "$RESPONSE" = "yes" ]; then
  echo "
Let's play Global Thermonuclear War"
  echo "
Launching missiles..."
  sleep 2
  echo "
Missiles launched."
  sleep 2
  echo "
Missiles detonating..."
  sleep 2
  echo "
The world is destroyed."
  sleep 2
  echo "
A strange game.
The only winning move is not to play.
How about a nice game of chess?"
else
  echo "
Very well. Goodbye."
fi


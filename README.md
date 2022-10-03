# Jumper


# Gameplay

"A game of Hangman in the sky"

A secret word is chosen randomly from a list.

The player makes guesses as to what letters are in the secret word. The success or failure of those guesses are represented by a plane jumper with a parachute.


Each time a correct letter is picked, any place that letter is found in the secret word, it becomes revealed.

Each time the player's guess is incorrect, the jumper's parachute has a cord snap.
When all four parachute cords have snapped due to incorrect guesses, the jumper falls to the ground.

The game ends either, when all letters in the word are correctly guessed, or the jumper falls to his doom.


## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
python3 Hilo Spec 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- Jumper                (folder containing game)
  +-- game              (source code for game)
      - director
      - jumper
      - secret_word
      - terminal_service
+-- README.md           (general info)
  -- __main__
```

## Required Technologies
---
* Python 3.8.0

## Authors
---
* Andrew Nash (atn22@byui.edu)

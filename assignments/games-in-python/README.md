
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game using Python. In this assignment, you will practice using strings, loops, conditionals, and random word selection to create a complete interactive game.

## 📝 Tasks

### 🛠️ Build the Core Hangman Loop

#### Description
Create the main game flow where a player guesses one letter at a time to reveal a hidden word before running out of attempts.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list of words.
- Prompt the player to enter a single-letter guess each turn.
- Display current progress in the word using underscores for unknown letters (for example: `_ a _ _ m a _`).
- Track and display the number of incorrect guesses remaining.
- End the game with a clear win message when the word is fully guessed.
- End the game with a clear lose message when attempts reach zero, and show the correct word.


### 🛠️ Improve Input Handling and Feedback

#### Description
Add validation and user feedback so the game is reliable and easy to play.

#### Requirements
Completed program should:

- Reject invalid input (empty input, multiple characters, non-letter characters) and ask again.
- Prevent duplicate guesses from reducing remaining attempts.
- Show guessed letters so the player can track their progress.
- Keep game output readable and updated after each guess.
- Use meaningful variable names and clear program structure.

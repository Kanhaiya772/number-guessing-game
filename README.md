# Number Guessing Game 🎉

## Overview

The Number Guessing Game is a web-based game developed using Flask and Bootstrap. Players are tasked with guessing a randomly generated 4-digit number within a limited number of attempts. The game provides feedback on each guess, indicating how many digits match the target number and how many are in the correct position. 

When the player successfully guesses the number, they can enter their name to save their score. The game keeps track of high scores and displays them at the bottom of the game interface.

## Features

- User-friendly web interface built with Bootstrap.
- Generates a random 4-digit target number with unique digits (cannot start with zero).
- Feedback on guesses includes:
  - Number of matching digits.
  - Number of digits in the correct position.
- Option to display the target number after exhausting attempts.
- High score tracking with player names.
- Restart option to play again without refreshing the page.
- Fun and engaging comments throughout the game.

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Bootstrap
- **Random Number Generation**: Python's built-in `random` module

## Installation

### Prerequisites

- Python 3.x
- Flask
- Bootstrap

### Steps to Install

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/number-guessing-game.git

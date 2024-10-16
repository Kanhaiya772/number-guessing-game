from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Global variables
target_number = ""
guess_history = []
max_guesses = 10  # Set maximum number of guesses
high_scores = []  # Store high scores as a list of tuples (name, score)

def generate_target_number():
    while True:
        number = str(random.randint(1000, 9999))
        if len(set(number)) == 4:  # Ensure all digits are unique
            return number

def get_match_info(guess, target):
    match_count = sum(1 for i in range(len(guess)) if guess[i] in target)
    position_match_count = sum(1 for i in range(len(guess)) if guess[i] == target[i])
    return match_count, position_match_count

@app.route("/", methods=["GET", "POST"])
def index():
    global target_number, guess_history, high_scores

    if request.method == "POST":
        if "restart" in request.form:
            # Restart the game
            target_number = generate_target_number()
            guess_history = []
            return redirect(url_for("index"))

        guess = request.form.get("guess")
        if guess and len(guess) == 4 and guess.isdigit() and guess[0] != '0':
            match_count, position_match_count = get_match_info(guess, target_number)

            # Determine score
            score = len(guess_history) + 1  # Increment score by the number of guesses made
            guess_history.append({
                "guess": guess,
                "match_count": match_count,
                "position_match_count": position_match_count,
                "score": score,
                "comment": "Keep trying! 🤔"  # Default comment
            })

            if position_match_count == 4:  # User guessed correctly
                # Ask for player name when they win
                player_name = request.form.get("player_name")
                if player_name:
                    # Add new score to the high scores list
                    high_scores.append((player_name, score))

                # Display winning message
                guess_history[-1]["comment"] = "Congratulations! 🎉 You guessed it right!"

                return redirect(url_for("index"))

    return render_template("index.html", target_number=None,
                           guess_history=guess_history, max_guesses=max_guesses,
                           high_scores=high_scores)

@app.route("/show_target_number")
def show_target_number():
    global target_number
    return render_template("show_target_number.html", target_number=target_number)

@app.route("/rules")
def rules():
    return render_template("rules.html")

if __name__ == "__main__":
    target_number = generate_target_number()
    app.run(debug=True)

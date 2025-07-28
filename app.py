# Author: Margaret Seymour
# GitHub username: seydev27
# Description:
# Flask app for Troll Riddle Race — a web-based logic and riddle puzzle game.
# Handles user input via a simple interface and returns game progression step by step.

from flask import Flask, request, render_template_string
from game import run_game  # Main game loop logic

app = Flask(__name__)

GAME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>🧌 Troll Riddle Race</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f9f9f9;
            padding: 2em;
            max-width: 600px;
            margin: auto;
        }
        h1 {
            color: #3b3b3b;
        }
        input[type="text"] {
            width: 80%;
            padding: 0.6em;
            margin-top: 1em;
            font-size: 1em;
        }
        input[type="submit"] {
            padding: 0.5em 1em;
            margin-top: 1em;
            font-size: 1em;
        }
        p {
            font-size: 1.1em;
        }
    </style>
</head>
<body>
    <h1>🧌 Troll Riddle Race</h1>
    <p>
        Welcome! Solve riddles or move toward the treasure.<br>
        ✅ Correct answer? You move. ❌ Wrong one? The troll does.<br>
        Can you reach the 💰 before the troll finds you?
    </p>

    {% if result %}
    <p><strong>🧭 Game Update:</strong><br>{{ result }}</p>
    {% endif %}

    <form method="post">
        <input type="text" name="user_input" placeholder="Type your move (N, S, E, W) or riddle answer..." required>
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def game():
    result = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        try:
            result = run_game(user_input)
        except Exception as e:
            result = f"⚠️ Oops! Something went wrong: {str(e)}"
    return render_template_string(GAME_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)

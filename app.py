# Author: Margaret Seymour
# GitHub username: seydev27
# Description: Flask-based entry point for Troll Riddle Race web app.
# Hosts the game logic and connects it to web routing and request handling.

from flask import Flask, request, render_template_string, redirect, url_for
from game import run_game  # This would be your core logic function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Here you'd capture and process user input
        user_input = request.form.get("user_input", "")
        result = run_game(user_input)  # This function will handle game progression
        return render_template_string(GAME_TEMPLATE, result=result)

    return render_template_string(GAME_TEMPLATE, result="")

# Simple inline HTML for now
GAME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Troll Riddle Race</title>
</head>
<body style="font-family: sans-serif; background-color: #fafafa; padding: 2em;">
    <h1>🧌 Troll Riddle Race</h1>
    <p>{{ result }}</p>
    <form method="post">
        <input type="text" name="user_input" placeholder="Your answer or move..." required>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)

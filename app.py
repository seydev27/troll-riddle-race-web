# Author: Margaret Seymour
# GitHub username: seydev27
# Flask web app for Troll Riddle Race – converts terminal gameplay into a web-playable experience.

from flask import Flask, render_template, request, redirect, url_for, session
import random
from board import create_board, display_board, move_entity, get_random_empty_position, distance
from riddles import RIDDLES, final_riddle_challenge

app = Flask(__name__)
app.secret_key = 'troll_secret_game_key'

BOARD_SIZE = 7


def init_game():
    board = create_board(BOARD_SIZE)
    player_pos = get_random_empty_position(board)
    troll_pos = get_random_empty_position(board)
    treasure_pos = get_random_empty_position(board)

    while troll_pos == player_pos or treasure_pos == player_pos or treasure_pos == troll_pos:
        troll_pos = get_random_empty_position(board)
        treasure_pos = get_random_empty_position(board)

    session['player'] = player_pos
    session['troll'] = troll_pos
    session['treasure'] = treasure_pos
    session['message'] = "🎮 Welcome to Troll Riddle Race!"
    session['riddle'] = random.choice(RIDDLES)

@app.route('/')
def index():
    if 'player' not in session:
        init_game()

    board = create_board(BOARD_SIZE)
    return render_template(
        'index.html',
        board=board,
        player=session['player'],
        troll=session['troll'],
        treasure=session['treasure'],
        riddle=session['riddle'][0],
        message=session['message']
    )

@app.route('/answer', methods=['POST'])
def answer():
    user_answer = request.form.get('answer', '').strip().lower()
    correct_answer = session['riddle'][1].lower()

    if user_answer == correct_answer:
        session['message'] = "✅ Correct! Move one step."
        return redirect(url_for('move_prompt'))
    else:
        session['message'] = "❌ Incorrect! The troll moves..."
        # Troll moves closer
        troll_row, troll_col = session['troll']
        player_row, player_col = session['player']

        if troll_row < player_row:
            troll_row += 1
        elif troll_row > player_row:
            troll_row -= 1

        if troll_col < player_col:
            troll_col += 1
        elif troll_col > player_col:
            troll_col -= 1

        session['troll'] = (troll_row, troll_col)
        session['riddle'] = random.choice(RIDDLES)
        return redirect(url_for('index'))

@app.route('/move', methods=['GET', 'POST'])
def move_prompt():
    if request.method == 'POST':
        direction = request.form.get('direction')
        new_pos = move_entity(session['player'], direction, BOARD_SIZE)
        session['player'] = new_pos

        if new_pos == session['troll']:
            session.clear()
            return render_template('end.html', result="💀 You were caught by the troll!")

        if new_pos == session['treasure']:
            return redirect(url_for('final_riddle'))

        session['riddle'] = random.choice(RIDDLES)
        return redirect(url_for('index'))

    return render_template('move.html')

@app.route('/final', methods=['GET', 'POST'])
def final_riddle():
    if request.method == 'POST':
        guess = request.form.get('answer', '').strip().lower()
        if guess == "echo":
            session.clear()
            return render_template('end.html', result="🏆 You solved the final riddle and won the treasure!")
        else:
            session['attempts'] = session.get('attempts', 3) - 1
            if session['attempts'] <= 0:
                session.clear()
                return render_template('end.html', result="❌ You failed the final riddle. The treasure is lost.")
            return render_template('final.html', attempts=session['attempts'])

    session['attempts'] = 3
    return render_template('final.html', attempts=3)

@app.route('/restart')
def restart():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)


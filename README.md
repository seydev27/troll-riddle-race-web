# 🧌 Troll Riddle Race – Web Edition

**Troll Riddle Race** is a retro-style puzzle game where you race a troll across a virtual grid — one riddle at a time.

In this web version, the game logic is powered by Python and Flask, with lightweight visual output in the browser. Built to sharpen your Python and recursion skills while providing an old-school riddle challenge.

---

## 🎯 Project Objective

This project was designed to practice and demonstrate skills in:

- 🔁 **Recursion** — especially in riddle logic and multi-try challenges  
- 🧠 **Logic and problem-solving** — progress is based on correctly solving riddles  
- 🗺️ **Grid navigation** — move on a 7×7 board tracked with 2D positions  
- 🧩 **Modular, maintainable code** — separate files handle board, troll, riddles, player logic  
- 🌐 **Web deployment** — using Flask to move from terminal to browser

---

## 🕹️ How to Play

1. The player, troll, and treasure are randomly placed on a 7×7 grid.
2. Each turn, you're presented with a riddle.
3. ✅ If you answer correctly, you get to move (N/S/E/W).
4. ❌ If you miss the riddle, the troll moves instead.
5. ⚠️ You’ll get clues about the troll’s behavior each turn:
   - “You hear heavy footsteps… are they coming for you?” 😬  
   - “The troll bellows in the distance — maybe it’s after the treasure?” 💰
6. Reach the treasure before the troll catches you.
7. Once at the treasure: solve a **final recursive riddle challenge** in 3 tries or less to win.  
   Miss all three? The troll catches up. Game over.

---

## 🚀 Live Demo

> Coming soon via [Render](https://render.com) or PythonAnywhere!

---

## 💻 Run Locally

### 🧱 Requirements

- Python 3.8+
- Flask  
- colorama (for console styling)

### 🧰 Setup

```bash
# Clone the repository
git clone https://github.com/seydev27/troll-riddle-race-web.git
cd troll-riddle-race-web

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Open in your browser:
# http://localhost:5000

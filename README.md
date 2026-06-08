# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
This is a number guessing game where the player tries to guess a secret 
  number within a limited number of attempts. The game gives hints after each guess and tracks a score that decreases with wrong guesses.


- [x] Detail which bugs you found.
  - **Flipped hints**: On even-numbered attempts, the secret was converted to a string causing lexicographic comparison instead of numeric, which made hints like "Too High" and "Too Low" unreliable.
  - **Score bug**: Wrong guesses on even attempts incorrectly rewarded +5 points instead of deducting points.
  - **Attempts initialization**: Attempts started at 1 instead of 0, consuming a free attempt before the player guessed anything.
  - **Hard difficulty range**: Hard mode used range 1–50, which is actually easier than Normal's 1–100. Fixed to 1–200.

- [x] Explain what fixes you applied.
  - Moved all core logic into `logic_utils.py` and imported it in `app.py`.
  - Fixed `check_guess` to always convert both guess and secret to integers 
    before comparing.
  - Fixed `update_score` to never reward points for wrong guesses.
  - Fixed attempts initialization to start at 0.
  - Fixed Hard difficulty range to 1–200.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects Normal difficulty (range 1–100, 8 attempts allowed)
2. User enters a guess of 40 → Game returns "📉 Go LOWER!" 
3. User enters a guess of 70 → Game returns "📈 Go HIGHER!"
4. User enters a guess of 55 → Game returns "📉 Go LOWER!"
5. User enters a guess of 63 → Game returns "📈 Go HIGHER!"
6. User enters a guess of 58 → Game returns "📉 Go LOWER!"
7. User enters a guess of 61 → Game returns "🎉 Correct!"
8. Score updates correctly after each guess, decreasing by 5 per wrong guess
9. Game ends, balloons appear, and final score is displayed

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

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

- 1. Game Purpose: It's a number-guessing game built with Streamlit. The computer picks a secret number within a range that depends on the difficulty (Easy 1–20, Normal 1–100, Hard 1–50), and the player tries to guess it within a limited number of attempts. After each guess the game gives a "go higher / go lower" hint and tracks a score, ending when you guess correctly or run out of attempts. 
- 2. Bug list: 
1. New Game button does not actually restart the game 
2. The hints are backward, it should say lower but it said higher 
3. The difficulty and the secret number was not match the range 
4. The history stored was wrong, it count from 0 so it show a little bit in confusion
5. Score system is weird, it goes negative  
- 3. My solutions
1. New Game button does not actually restart the game
The New Game code reset the secret and attempts but never set status back to "playing", so the app stayed stuck on the "game over" screen. Fixed by adding st.session_state.status = "playing" (plus clearing history) in the New Game block 

2. The hints are backward (said higher when it should say lower)
In check_guess the messages were swapped. Fixed so a guess that's too high now says "📉 Go LOWER!" and too low says "📈 Go HIGHER!" 

3. The difficulty and the secret number did not match the range
New Game generated the secret with a hardcoded random.randint(1, 100), ignoring difficulty. Fixed to random.randint(low, high) so the secret always matches the chosen difficulty's range 

4. The attempt/history count started from a confusing number
The counter started at 1 on the first game but 0 after New Game, so "attempts left" looked off. Fixed by starting at 0 everywhere so it's consistent 

5. Score system is weird — it goes negative
Every wrong guess subtracted 5 points with no lower limit. Fixed by clamping with max(0, current_score - 5) so the score can never drop below 0 


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User choose the difficulty level, let say choose hard 
2. The system will only generate secret number from 1 to 50 
3. The user accidentally input 0 
4. System warning and said the input is out of range 
5. The user accidentally input 20 (secret is 40)
6. System will said please go lower 
7. Score updates correctly after each guess but never go below 0 
8. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
platform darwin -- Python 3.11.7, pytest-7.4.0, pluggy-1.0.0
collected 3 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 33%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 66%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [100%]

============================== 3 passed in 0.01s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

# FIX: Refactored the four logic functions out of app.py into logic_utils.py with
# Claude (agent mode); I reviewed each one against the original app.py behavior.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str, low: int = None, high: int = None):
    """
    Parse user input into an int guess.

    If low and high are given, the guess must fall within [low, high].

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    # FIX (Challenge 1 - Edge Cases): Handle out-of-range input (e.g. guessing 50
    # on Easy 1-20). I asked Claude in agent mode to warn on bad input without
    # counting it as an attempt (but still record it in history, handled in app.py);
    # Claude added these optional low/high bounds and I verified it by playing.
    if low is not None and high is not None and not (low <= value <= high):
        return False, None, f"Out of range. Pick a number between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome is one of: "Win", "Too High", "Too Low"
    """
    guess = int(guess)
    secret = int(secret)

    # FIX: The hints were backwards (too high said "go higher"). I spotted the bug
    # while playing; Claude and I rewrote the comparison so the messages match.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        # Guess is bigger than the secret -> the player must go LOWER.
        return "Too High", "📉 Go LOWER!"
    # Guess is smaller than the secret -> the player must go HIGHER.
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        # FIX: Score used to go negative on wrong guesses. I reported the weird
        # behavior and Claude suggested clamping with max(0, ...) so it floors at 0.
        return max(0, current_score - 5)

    return current_score

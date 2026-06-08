from logic_utils import check_guess, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# Added 3 more tests
def test_no_flipped_hint_on_even_attempt():
    result = check_guess(60, 40)
    assert result == "Too High"

def test_wrong_guess_never_increases_score():
    new_score = update_score(100, "Too High", 2)
    assert new_score < 100

def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok == False
from logic_utils import check_guess

def test_winning_guess():
    status, hint = check_guess(50, 50)
    assert status == "Win"
    assert "Correct" in hint  # Matches "🎉 Correct!"

def test_guess_too_high():
    status, hint = check_guess(60, 50)
    assert status == "Too High"
    assert "LOWER" in hint    # Matches "📉 Go LOWER!"

def test_guess_too_low():
    status, hint = check_guess(40, 50)
    assert status == "Too Low"
    assert "HIGHER" in hint   # Matches "📈 Go HIGHER!"

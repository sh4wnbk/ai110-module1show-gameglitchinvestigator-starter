from logic_utils import check_guess, parse_guess # Import the parse_guess function to be tested

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


# Edge Cases

def test_very_large_number():
    """Edge Case: Ensure logic handles numbers way outside the 1-100 range."""
    status, hint = check_guess(10**10, 50)
    assert status == "Too High"
    assert "LOWER" in hint

def test_decimal_string_flow():
    """Edge Case: Ensure string decimals are converted to integers correctly."""
    ok, value, err = parse_guess("42.5")
    assert ok is True
    # Your logic uses int(float(raw)), so 42.5 becomes 42
    status, hint = check_guess(value, 50)
    assert status == "Too Low"
    assert "HIGHER" in hint

def test_non_numeric_string_flow():
    """Edge Case: Ensure non-numeric junk is caught by the parser."""
    ok, value, err = parse_guess("notanumber")
    assert ok is False
    assert err == "That is not a number."


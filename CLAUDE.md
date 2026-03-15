# CLAUDE.md — Project Context for Claude Code

This file is written for Claude Code on any machine. Read it fully before assisting.

---

## 1. Project Overview

**Name:** Game Glitch Investigator — The Impossible Guesser
**Course:** CodePath AI Engineering (ai110), Module 1
**Stack:** Python, Streamlit, pytest
**Repo:** https://github.com/sh4wnbk/ai110-module1show-gameglitchinvestigator-starter
**Run command:** `python -m streamlit run app.py`
**Test command:** `pytest` (from project root)
**Install:** `pip install -r requirements.txt`
**Virtual environment:** `codepath-ai110`

The project is a Streamlit number-guessing game that was intentionally shipped broken. The student's task is to identify and fix the bugs, refactor logic into `logic_utils.py`, pass all tests, and complete documentation.

---

## 2. File Structure

| File | Purpose |
|---|---|
| `app.py` | Streamlit UI — handles session state, input, display |
| `logic_utils.py` | Game logic — `check_guess`, `parse_guess`, `get_range_for_difficulty`, `update_score` |
| `tests/test_game_logic.py` | pytest tests for logic functions |
| `reflection.md` | Student reflection — 5 questions about the debugging process |
| `README.md` | Project overview, setup, demo, and experience documentation |
| `requirements.txt` | `streamlit>=1.21.0`, `altair<5`, `pytest` |

---

## 3. What Is Complete

- `check_guess(guess, secret)` implemented in `logic_utils.py`, imported into `app.py`. Returns `(outcome, message)` tuple where outcome is `"Win"`, `"Too High"`, or `"Too Low"`.
- `app.py` no longer defines its own `check_guess`.
- All 3 pytest tests in `tests/test_game_logic.py` pass.
- `reflection.md` sections 1 and 2 are fully answered.
- Code comments (`# FIX:`, `# FIXME:`) are in place near changes.

---

## 4. What Is Incomplete

Work should resume here. Complete in order.

### Phase 2, Step 4 (partially done)
- [ ] `reflection.md` **Section 3: "Debugging and testing your fixes"** — blank, needs answers

### Phase 3, Step 1
- [ ] `README.md` **"Demo" section** — screenshot placeholder not filled in
- [ ] `README.md` **"Document Your Experience" checkboxes** — all unchecked

### Phase 3, Step 2
- [ ] `reflection.md` **Section 4: "What did you learn about Streamlit and state?"** — blank
- [ ] `reflection.md` **Section 5: "Looking ahead: your developer habits"** — blank

### Phase 3, Step 4
- [ ] Final commit and push after all documentation is complete

### Unfinished refactor in `logic_utils.py`
These three functions still raise `NotImplementedError` — they were NOT moved from `app.py`:
- `get_range_for_difficulty(difficulty)`
- `parse_guess(raw)`
- `update_score(current_score, outcome, attempt_number)`

The working versions of all three exist in `app.py` and need to be moved into `logic_utils.py`.

### Known bug (marked in code)
- `app.py` line ~122: `# FIXME: This reset is incomplete; it does not update the game 'status' variable`
  The "New Game" button resets `attempts` and `secret` but not `st.session_state.status`, so a finished game cannot be restarted without a browser refresh.

---

## 5. User Preferences

- **Ask before pushing to GitHub.** Never push automatically.
- **Be direct and concise.** No trailing summaries, no over-explaining, no unnecessary confirmation prompts.
- **Do not infer or confabulate.** Only state what is known from the code or this file.

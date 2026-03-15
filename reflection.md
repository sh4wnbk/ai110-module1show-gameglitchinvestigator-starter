# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- The first time I ran the game, the numbers immediately felt disconnected from the instructions. The side-banner claimed 8 attempts were allowed, yet the counter showed only 7 remained before I had even made my first guess. 

- One concrete bug I noticed was that the hints were fundamentally backwards; when I guessed -199 for a secret number of 27, the AI told me to "go lower." Another major issue was the game's state management. The "Start a New Game" button failed to reset the board or the secret number. To clear the previous "Game Over" screen and try a new round, I had to manually refresh my browser - as the session state was effectively frozen.

- Another major bug was the behavior of the difficulty and range settings. Even though I selected "Easy" mode ( which indicates a Range of 1 to 20), the game Developer Debug Info labeled the difficulty as "Normal" and allowed me to enter numbers like 1000 and 10,000 without any validation. In one instance, guessing 1000 for range of 1–20 resulted in the game telling me to "go higher," proving that the underlying secret number was not staying within the boundaries noted in the sidebar.


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

*I used Gemini as a high-level "Mission Control" for environment strategy and GitHub Copilot Agent as a debugging teammate, mostly for root-cause analysis, refactoring support, and quick test targeting.*

==========================================================

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

*The Agent helped me trace the check_guess bug to a type mismatch where the secret became a string and comparisons turned into lexicographical (string) comparisons instead of numeric. i.e.,"-199" was treated as less than "27"—rather than numeric.* 

*That suggestion was correct, and I used it to move and simplify check_guess in logic_utils.py so it always compares numbers and returns the correct High/Low hints*

==========================================================

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).


*One suggestion was misleading, though: I was advised to use a different return shape for `check_guess` (a tuple format that didn’t match what the Streamlit UI expected), which would have broken the app* 

*I caught this by checking how `outcome, message` is consumed in app.py. app.py expects two separate items — a Result and a Message. The Agent, however, suggsted one single Tuple (a "box" containing both items).*

*I verified everything two ways: with `pytest` in `test_game_logic.py` for independent logic checks, and with manual boundary tests in the UI using guesses like 1, -1, 100, and 101 to confirm the hints stayed accurate.*

--- 


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

*A fix didn't count as done until it passed two checks: the automated tests and a manual run in the browser. If `pytest` passed but the UI still behaved oddly, I kept digging. If the UI looked right but a test failed, I hadn't actually solved the root problem — I'd just hidden it. Both had to agree before I moved on.*

==========================================================

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

*The clearest example was `test_guess_too_high` in `test_game_logic.py`. It calls `check_guess(60, 50)` and asserts the outcome is `"Too High"` and the hint contains `"LOWER"`. Before the fix, that test failed — the function returned `"Go HIGHER!"` when the guess was already too high. Seeing the test fail in red made the bug undeniable. Once I corrected the hint logic in `logic_utils.py`, the test went green and the UI matched.*

*I also ran manual boundary tests directly in the app — guesses like 1, -1, 100, and 101 — to confirm the hints stayed accurate at the edges of the range, not just at the midpoint.*

==========================================================

- Did AI help you design or understand any tests? How?

*GitHub Copilot Agent helped me understand what the tests were actually checking. When I first read the assert statements, I wasn't sure why the tests checked for `"LOWER"` in the hint string rather than the full message. The Agent explained that partial string matching (`"LOWER" in hint`) is more resilient than checking for an exact emoji-and-text match — a small implementation change wouldn't break the test unnecessarily. That made the test design click for me.*

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

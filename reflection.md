# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, it looked functional on the surface, the UI loaded, the guess input worked, and the score displayed, but the behavior was immediately suspicious. The hints were unreliable, sometimes telling me to go higher when I should go lower, and the score would increase even when I guessed wrong. The hard difficulty also had a range of 1–50, which is actually easier than Normal 1–100, which is the opposite of what you would expect

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 60 | Too High hint | Too low hint shown| none|
| Select Hard Difficulty | Range is harder than normal| Range is only 1-50| none|
| 75| Score decreases or stays same| Score increases by 5| none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 

I used Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One example where the claude AI was correct was when identifying the flipped hint bug it correctly explained that converting the secret to a string on even attempts causes Python to do lexicographic comparison instead of numeric comparison, which I verified by manually tracing through the check_guess function with a specific example

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One area where AI could be misleading is the score bug the broken scoring logic looks intentional at a first glance, and an AI might explain it as a "bonus system" rather than flagging it as a bug unless you specifically ask whether rewarding wrong guesses makes sense for a guessing game.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed by forming a specific expectation first, then 
testing that exact scenario in the running app to confirm the behavior 
matched. For the flipped hints fix, I tested on attempt #2 with a guess 
higher than the secret to confirm the hint now correctly said "Too High" 
instead of "Too Low." I ran pytest on test_game_logic.py which showed all 
six tests passing, including a specific test for the even-attempt flipped 
hint scenario. AI helped me think through which edge cases to cover in 
tests, though I verified each test case made sense for the intended behavior 
before keeping it.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the entire Python script from top to bottom every time a 
user interacts with the app, like clicking a button or typing in a text box. 
Session state is how Streamlit remembers values between those reruns 
without it, variables like the secret number and attempt count would reset 
to their initial values on every interaction. I would explain it to a friend 
like this: imagine every button click refreshes the whole page, and session 
state is like a sticky note that survives each refresh. This is why the bug 
of initializing attempts to 1 instead of 0 mattered the initialization 
only runs once on the first load, but that wrong starting value affects 
every rerun after that.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is forming a specific expectation before testing saying "this input should produce this output" before running anything 
makes bugs much easier to spot and explain. Next time I work with AI on a 
coding task, I would ask it to explain edge cases earlier rather than just 
asking what the code does, since the most subtle bugs in this project only 
appeared under specific conditions like even-numbered attempts. This project 
changed the way I think about AI-generated code because it showed me that 
code can look completely reasonable and still be systematically wrong in 
ways that only appear during actual use.
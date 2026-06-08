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

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

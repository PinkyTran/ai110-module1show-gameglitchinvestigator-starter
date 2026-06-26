# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
-> It looks totally fine to me, everything is running and did not indicate that there's a problem 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. New Game button does not actually restart the game 
2. The hints are backward, it should say lower but it said higher 
3. The difficulty and the secret number was not match the range 
4. The history stored was wrong, it count from 0 so it show a little bit in confusion
5. Score system is wierd, it goes negative 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|Click new game button|New game started|The game was not start only the secret number change|It was not output error there|
|Guessing number is higher|Should say lower |It said please guess higher |It output as guess higher please |
|Change the difficulty to hard |The secret number range should from 0 -> 50 |The secret number was range from 0 -> 100 |The output for secret number is wrong |


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
-> Claude 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
-> One example is when I give a clear directions about what is the bug and where to look at it and what to fix like "look at app.py, there's a bug about sending wrong messages about guessing numbers when it should be go higher but the output was go lower, find where is it and fixed the bug within app.py" The result was sweet, it solved that case. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
-> One AI suggestions was incorrect is I told it to fixed the case about new game button but maybe because of my isntruction was not clear and it was misleading by creating another file to run the method so I need to restate my instruction with better clarification and directions so Claude can understand what I want 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
-> When I run the game again and test to see whether the bug is fixed, besides that I also ask claude to run the game and test edge cases to see whether that bug is fixed in general or not 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
-> Yes, claude pull out where is the logic break instead of me manually scrolling and finding that method among hundred lines of code so it really useful. Beside it also help me in design the solution for the bug when it give me multiple options/solutions to solve for 1 problem that I have described and also note which directions is easier. 


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
-> Every time you click a button or type something in a Streamlit app, it re-reads your whole code file from the very top, like starting the recipe over from step one. This means any normal variable gets wiped and made fresh each time — which is why our game's secret number kept changing and you could never win. To fix that, st.session_state works like a little memory box that holds onto things (the secret, your score, your attempts) so they stay the same between clicks instead of resetting.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
-> First, run the game and test it yourself. Then document the bugs, and then tell AI Agents to told where are the bugs and then check whethers those bugs we have and those that AI agents suggest is match then start to solve the bug one by one 
  
- What is one thing you would do differently next time you work with AI on a coding task?
-> I will give a better instruction, show it where to look at, which logic break is wrong in my head, my solution, where I want to solve. I would be basic with the first or two command and then start to tacle the edge case later when the logic bug is already solve instead of tell AI to solve everything in 1 time it would create a bigger mess 

- In one or two sentences, describe how this project changed the way you think about AI generated code.
-> It much better and stronger than I belived. I work and use AI almost everyday but have not implemented in coding basis and now I can see how strong it is but I also keep in mind that I also need to improve my foundation otherwise I would get blinded by AI hallucination 
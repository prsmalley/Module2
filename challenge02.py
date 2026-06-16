#Name:
#Module 2 - Challenge Problems (not graded — for if you finish early or want more!)
'''
These are harder than the assignment on purpose. Some of them may use ideas we
haven't covered in class yet (like if/else or f-strings) — that's intentional.
Part of being a programmer is looking things up and trying. Have fun!
'''

'''
####Challenge 01: Bill Splitter
Ask the user for:
  - the total bill amount
  - a tip percentage (e.g. 18 for 18%)
  - the number of people splitting the bill
Then print:
  - the tip amount
  - the total including tip
  - how much EACH person pays
'''

print('Challenge 01')
#write your code below




'''
####Challenge 02: Two-Way Temperature Converter
Ask the user for a temperature, then ask whether it is in Fahrenheit or Celsius.
Convert it to the other unit and print the result.
  F to C:  C = (F - 32) * 5/9
  C to F:  F = (C * 9/5) + 32
(Hint: you'll need a way to make a decision — look up "if / else" in Python.)
'''

print('\nChallenge 02')
#write your code below




'''
####Challenge 03: f-strings
There's a cleaner way to build sentences than gluing pieces together with + or commas.
It's called an f-string. Example:
    name = "Ada"
    print(f"Hello {name}, welcome!")
Rewrite your Task 04 "year you turn 100" sentence using an f-string instead.
'''

print('\nChallenge 03')
#write your code below




'''
####Challenge 04: Break the Grader  (a puzzle about how grading works)
Open tests/test_assignment02.py and read it slowly.

Your challenge: write a program that PASSES every check in the autograder
WITHOUT actually solving the tasks correctly — no real math, and maybe without
even reading the user's input at all.

Think about:
  - How does the autograder give the program its "answers"? Where do they come from?
  - Is each test checking that your MATH is correct, or just that certain WORDS appear?
  - If you were the teacher, how would you rewrite the tests so this trick stops working?

To try it: save a copy of your real assignment02.py first(!), then experiment in
assignment02.py and run:  python tests/test_assignment02.py
When you're done playing, put your real assignment02.py back.

(There's no "right" answer to hand in — this one is about understanding how tests
can be fooled, and why good tests are hard to write.)
'''

print('\nChallenge 04 — see the comments above')

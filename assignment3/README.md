# Assignment 3 — More Python Skills

[← Course index](../README.md)

Practice with decorators, list comprehensions, closures, and custom classes (Code the Dream Python 100, Week 3).

## Submission hub — everything for this week

This README is the single link I submit for Week 3. Every deliverable is linked below, and the mindset response is at the bottom of this page.

| Deliverable | Link |
|---|---|
| **Pull request** (code + review) | [#3](https://github.com/ba-00001/brian-bazurto-python-v2/pull/3) |
| Folder on branch `assignment3` | [assignment3/](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment3/assignment3) |
| `decorator.log` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment3/assignment3/decorator.log) |
| `extend-point-to-vector.py` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment3/assignment3/extend-point-to-vector.py) |
| `hangman-closure.py` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment3/assignment3/hangman-closure.py) |
| `list-comprehensions.py` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment3/assignment3/list-comprehensions.py) |
| `log-decorator.py` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment3/assignment3/log-decorator.py) |
| `tictactoe.py` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment3/assignment3/tictactoe.py) |
| `type-decorator.py` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment3/assignment3/type-decorator.py) |
| Mindset response | [Motivation and Mindset](#mindset-response--motivation-and-mindset) |
| Lesson page (CTD Learns) | [Week 3](https://classes.codethedream.org/course/python-100-v2/python-for-data-analysis-26.4?week=3&lesson=More%20Python%20Skills) |

## Files

| File | What it does | Task |
|------|--------------|------|
| [`log-decorator.py`](log-decorator.py) | `logger_decorator` logs each call's function name, positional params, keyword params and return value to `./decorator.log`; three decorated functions are called from the mainline | 1 |
| [`decorator.log`](decorator.log) | Log file produced by running `log-decorator.py` | 1 |
| [`type-decorator.py`](type-decorator.py) | `type_converter(type_of_output)` decorator factory; `return_int()` converted to `str`, `return_string()` converted to `int` (raises `ValueError`, caught in the mainline) | 2 |
| [`list-comprehensions.py`](list-comprehensions.py) | Reads `../csv/employees.csv` with the csv module, builds the full-name list and the names-containing-"e" list with list comprehensions | 3 |
| [`hangman-closure.py`](hangman-closure.py) | `make_hangman(secret_word)` returns the `hangman_closure(letter)` closure that keeps `guesses`; playable hangman game using `input()` | 4 |
| [`extend-point-to-vector.py`](extend-point-to-vector.py) | `Point` class (equality, string, Euclidean distance) and `Vector(Point)` subclass (own string, `+` returns a new `Vector`), with a demo | 5 |
| [`tictactoe.py`](tictactoe.py) | `TictactoeException`, `Board` class (`valid_moves`, `__str__`, `move()`, `whats_next()`) and a two-player game loop | 6 |

## How to run

From inside `assignment3/`:

```bash
python3 log-decorator.py          # then: cat decorator.log
python3 type-decorator.py
python3 list-comprehensions.py
python3 hangman-closure.py        # interactive
python3 extend-point-to-vector.py
python3 tictactoe.py              # interactive
```

## Sample output

**Task 1** — `decorator.log`

```
function: say_hello
positional parameters: none
keyword parameters: none
return: None
function: takes_positional
positional parameters: [1, 'two', 3.0]
keyword parameters: none
return: True
function: takes_keywords
positional parameters: none
keyword parameters: {'name': 'Brian', 'course': 'Python 100', 'week': 3}
return: <function logger_decorator at 0x7f085f7976a0>
```

**Task 2**

```
str
can't convert that string to an integer!
```

**Task 3** (20 names, then 15 with an "e")

```
['Cindy Wade', 'David Thornton', 'Lauren Martinez', 'Kenneth White', 'James Torres', 'Tracy Foster', 'Miranda Harris', 'Destiny Nguyen', 'Phillip Williams', 'Kelli Bowman', 'Gregory Pittman', 'Natasha Hoover', 'Gregory Jackson', 'David Clark', 'Sarah Shepherd', 'Michael Quinn', 'Logan Lopez', 'Donald Hunt', 'Matthew Meyers', 'Thomas Calderon']
['Cindy Wade', 'Lauren Martinez', 'Kenneth White', 'James Torres', 'Tracy Foster', 'Destiny Nguyen', 'Kelli Bowman', 'Gregory Pittman', 'Natasha Hoover', 'Gregory Jackson', 'Sarah Shepherd', 'Michael Quinn', 'Logan Lopez', 'Matthew Meyers', 'Thomas Calderon']
```

**Task 4** (secret word "apple"; blank lines that hide the word are left out here)

```
Enter the secret word: apple
Guess a letter: a
a____
Guess a letter: 1
Please enter a single letter.
Guess a letter: p
app__
Guess a letter: l
appl_
Guess a letter: x
appl_
Guess a letter: e
apple
You got it! The word was apple. It took 5 guesses.
```

Check with the example from the spec: `make_hangman("alphabet")` after guessing `a` then `h` prints `a__ha___` and returns `False`.

**Task 5**

```
p1: Point(1, 2)
p2: Point(4, 6)
p1 == p3: True
p1 == p2: False
distance p1 to p2: 5.0
v1: Vector<3, 4>
v2: Vector<-1, 2>
v1 + v2: Vector<2, 6>
v1 + v2 is a Vector: True
v1 == Vector(3, 4): True
distance v1 to v2: 4.47213595499958
distance v1 to origin: 5.0
```

**Task 6** (end of a game, including both error messages along the way)

```
O's turn. Enter your move: center
That spot is taken. Try again.
O's turn. Enter your move: foo
That's not a valid move. Try again.
...
X's turn. Enter your move: lower center
 O | X |   
-----------
   | X |   
-----------
 O | X |   

X wins!
```

A full-board game with no winner ends with `Cat's Game.`

## Requirements checklist

- [x] All files are in `assignment3/` with the exact required names, and each task is marked with a `# Task N` comment
- [x] Task 1: `logger_decorator` logs function name, positional params (or "none"), keyword params (or "none") and return value to `./decorator.log`
- [x] Task 1: three decorated functions (no args/no return, `*args` returning `True`, `**kwargs` returning `logger_decorator`) called from the mainline; `decorator.log` is produced
- [x] Task 2: `type_converter(type_of_output)` with three levels (factory, decorator, wrapper)
- [x] Task 2: `return_int()` decorated with `str`, `return_string()` decorated with `int`; mainline verification block used exactly as written and catches the `ValueError`
- [x] Task 3: `../csv/employees.csv` read into a list of lists with the csv module
- [x] Task 3: full names built with a list comprehension, header skipped (20 names), then names containing "e" with a second list comprehension (15 names); both printed
- [x] Task 4: `make_hangman(secret_word)` keeps `guesses` in the enclosing scope and returns the `hangman_closure` function object
- [x] Task 4: each call appends the letter, prints the word with underscores, returns `True` only when fully guessed ("alphabet" + a, h prints `a__ha___`)
- [x] Task 4: playable game using `input()` for the secret word and each guess
- [x] Task 5: `Point` with `__init__(x, y)`, `__eq__`, `__str__` and `distance()`
- [x] Task 5: `Vector(Point)` reuses the parent `__init__`, overrides `__str__`, and `__add__` returns a new `Vector`; mainline demonstrates every method
- [x] Task 6: `TictactoeException(Exception)` stores `self.message` and calls `super().__init__()`
- [x] Task 6: `Board` with class variable `valid_moves` (exactly as given), `__init__` building a 3x3 `board_array` of `" "` and `turn = "X"`, plus `__str__`, `move()` and `whats_next()`
- [x] Task 6: game loop prompts with whose turn it is, calls `board.move()` inside `try`/`except TictactoeException`, and shows the error message or the result
- [x] Work on the `assignment3` branch, pushed, with a pull request into `main`

## Mindset Response — Motivation and Mindset

> “Becoming is better than being.” — Carol Dweck

**1. Why do you want to be a software developer/data engineer?**

Last class my answer was that I build things but didn't really understand how they work when they break. That's still true, but now it's more specific: data. I'm at FIU with minors in business analytics and supply chain, and almost every real problem I run into there is a messy spreadsheet or a CSV that someone needs cleaned, joined, and summarized. Data engineering is the part that makes analytics actually possible, and I want to be the person who can build that pipeline instead of waiting on someone else.

**2. What do you plan to do with your skills after the class ends?**

Use pandas and SQL on real data for the student programs I work with (events, sign-ups, attendance), finish the Kaggle capstone as a portfolio piece, and keep going into the more advanced CTD classes. Longer term I want this to be part of my job, on the analytics/supply chain side.

**3. Can you think of a time when a growth mindset helped you learn or achieve something new?**

Same story as last class still fits: guitar. I plateaued for months and decided I'd hit my ceiling. Slowing down with a metronome until it was boring fixed changes I'd been missing for a year. The new example is this course. Python Intro felt hard at first and I almost treated the late weeks as proof I wasn't a "programmer". Getting all 11 assignments written showed me "I can't do this" usually means "not yet, not this way", and that's why I signed up for the next level.


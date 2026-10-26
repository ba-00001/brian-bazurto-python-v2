# Assignment 1 — Intro to Python

[← Course index](../README.md)

Functions, f-strings, type conversion, error handling, loops, `*args`/`**kwargs` and string manipulation (Code the Dream Python 100 v2, Week 1).

## Submission links

| # | Item | Link |
|---|------|------|
| URL1 | Pull request | https://github.com/ba-00001/brian-bazurto-python-v2/pull/1 |

## Files

| File | What it does | Task |
|------|--------------|------|
| `assignment1.py` | All ten functions, each marked with a `# Task N` comment: `hello`, `greet`, `calc`, `data_type_conversion`, `grade`, `repeat`, `student_scores`, `titleize`, `hangman`, `pig_latin` | 1–10 |
| `assignment1-test.py` | PyTest suite provided by CTD (unchanged) | — |

## How to run

From inside `assignment1/`:

```bash
python assignment1.py
pytest -v -x assignment1-test.py
```

## Sample output

```
$ python assignment1.py
Hello!
Hello, Brian!
You can't divide by 0!
256
You can't convert nonsense into a float.
B
hahaha
Leo
The Lord of the Rings
a___ab__
ethay ickquay ownbray oxfay
```

## Test results

```
assignment1-test.py::test_hello PASSED
assignment1-test.py::test_greet PASSED
assignment1-test.py::test_calc PASSED
assignment1-test.py::test_data_type_conversion PASSED
assignment1-test.py::test_grade PASSED
assignment1-test.py::test_repeat PASSED
assignment1-test.py::test_student_scores PASSED
assignment1-test.py::test_titleize PASSED
assignment1-test.py::test_hangman PASSED
assignment1-test.py::test_pig_latin PASSED
============================== 10 passed ==============================
```

## Notes

- `calc` uses `match`/`case`, catches `ZeroDivisionError` and `TypeError`.
- `grade` catches `TypeError` (and an empty call) and returns `"Invalid data was provided."`.
- `repeat` builds the string with a `for` loop over `range(count)` instead of `string * count`.
- `pig_latin` treats `qu` as one consonant, including after other consonants (`square` → `aresquay`).

## Requirements checklist

- [x] Task 1 — `hello()` returns `Hello!`
- [x] Task 2 — `greet(name)` uses an f-string
- [x] Task 3 — `calc` with default `multiply`, all seven operations, both error messages
- [x] Task 4 — `data_type_conversion` for `int`/`float`/`str` with the formatted error message
- [x] Task 5 — `grade(*args)` with the A–F scale and invalid-data handling
- [x] Task 6 — `repeat` uses a `for` loop and `range`
- [x] Task 7 — `student_scores` with `best` / `mean` using `**kwargs`
- [x] Task 8 — `titleize` with the little-words rule, first/last word always capitalized
- [x] Task 9 — `hangman(secret, guess)`
- [x] Task 10 — `pig_latin` including the `qu` rule
- [x] All 10 PyTest tests pass
- [x] Mindset response written

## Mindset Response — Asking for Help

> “Smart questions are a stimulus and a gift.” — Eric S. Raymond

**1. What’s your rule of thumb for when to ask for help and when was a time when you wish you would have asked for help sooner?**

Returning student, so this is an update on what I said in Python Intro. My rule is still about 30 minutes, but the real test is whether I've learned anything new in that time. If I'm still testing ideas I keep going. If I'm rereading the same error or re-running code I didn't change, that's my cue to ask.

What changed: last class I lost days on the Week 2 setup because I assumed the work went in the repo I made myself instead of the fork. I never asked one simple question. This time I checked the repo setup in the README before writing any code, and when the pig_latin "square" test failed (the "qu" after the "s"), I gave myself a limit before reaching out instead of grinding on it for hours.

**2. What information have you found crucial to include in your questions so that mentors or peers can help answer your questions quicker?**

Same list as before, it still holds: (1) what I'm trying to do, not just what broke, (2) the full error pasted, not retyped, (3) the smallest piece of code that still breaks, (4) what I already tried and what happened, and (5) my setup (Python version, OS, which branch). The one I added this class is the exact test that's failing. With pytest, "test_calc fails on 12.6 - 4.4" gets an answer way faster than "my calculator is broken.


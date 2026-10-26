# Assignment 2 — Data Structures and File Handling

[← Course index](../README.md)

`input()` and file writing, reading CSVs into dicts/lists, `filter`/`lambda`/`sort`, dicts of dicts, `os.getenv`, a custom module, sets, `map` and `datetime` (Code the Dream Python 100 v2, Week 2).

## Submission hub — everything for this week

This README is the single link I submit for Week 2. Every deliverable is linked below, and the mindset response is at the bottom of this page.

| Deliverable | Link |
|---|---|
| **Pull request** (code + review) | [#2](https://github.com/ba-00001/brian-bazurto-python-v2/pull/2) |
| Folder on branch `assignment2` | [assignment2/](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment2/assignment2) |
| `assignment2.py` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment2/assignment2/assignment2.py) |
| `custom_module.py` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment2/assignment2/custom_module.py) |
| `diary.py` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment2/assignment2/diary.py) |
| `diary.txt` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment2/assignment2/diary.txt) |
| `minutes.csv` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment2/assignment2/minutes.csv) |
| Test results | [14 passed](#test-results) |
| Mindset response | [AI for Learning](#mindset-response--ai-for-learning) |
| Lesson page (CTD Learns) | [Week 2](https://classes.codethedream.org/course/python-100-v2/python-for-data-analysis-26.4?week=2&lesson=Data%20Structures%20and%20File%20Handling) |

## Files

| File | What it does | Task |
|------|--------------|------|
| [`diary.py`](diary.py) | Appends lines to `diary.txt` until `done for now`; prompts `What happened today? ` then `What else? `; `try`/`except Exception` with the traceback report | 1 |
| [`diary.txt`](diary.txt) | Output of two test runs (the second was ended with Ctrl-D to trigger the exception) | 1 |
| [`assignment2.py`](assignment2.py) | Tasks 2–15, each marked with a `# Task N` comment | 2–15 |
| [`custom_module.py`](custom_module.py) | `secret = "shazam!"` and `set_secret()`, exactly as given | 11 |
| [`minutes.csv`](minutes.csv) | Written by `write_sorted_list()`: chairpersons with duplicates removed, sorted by date | 15 |
| `assignment2-test.py` | PyTest suite provided by CTD (unchanged) | — |

## How to run

From inside `assignment2/`:

```bash
python diary.py
export THISVALUE=ABC
python assignment2.py
pytest -v -x assignment2-test.py
```

## Sample output

```
$ python diary.py
What happened today? Went to the library and finished the Python lesson
What else? Tried the diary program for the first time
What else? done for now

$ python diary.py          # Ctrl-D at the second prompt
What happened today? Fixed a bug in my calc function
What else? An exception occurred.
Exception type: EOFError
Exception message: EOF when reading a line
Stack trace: ['File : .../assignment2/diary.py , Line : 8, Func.Name : <module>, Message : line = input(prompt)']
```

First lines of `minutes.csv`:

```
Name,Date
Jason Tucker,"September 20, 1980"
Austin Hester,"March 8, 1981"
```

## Test results

```
$ THISVALUE=ABC pytest -x assignment2-test.py
assignment2-test.py ..............                                       [100%]
============================== 14 passed ==============================
```

## Notes

- `read_minutes()` uses one helper, `read_csv_as_tuples()`, for both files (DRY), storing each row as a tuple so the rows are hashable for the set in Task 13.
- `employee_dict()` uses `zip()` (the optional extra in Task 8) and skips `employee_id`.
- `minutes_list` is sorted on the `datetime` values, then converted back to strings before writing, so the dates sort by time and not alphabetically.

## Requirements checklist

- [x] Task 1 — `diary.py` with `with open("diary.txt", "a")` inside `try`, exact prompts and sentinel
- [x] Task 2 — `read_employees()` → `fields`/`rows`, global `employees`
- [x] Task 3 — `column_index()` and global `employee_id_column`
- [x] Task 4 — `first_name(row_number)` via `column_index`
- [x] Task 5 — `employee_find()` with the inner `employee_match` and `filter`
- [x] Task 6 — `employee_find_2()` with a lambda
- [x] Task 7 — `sort_by_last_name()` sorts in place with `key=lambda`
- [x] Task 8 — `employee_dict(row)` without `employee_id`
- [x] Task 9 — `all_employees_dict()`
- [x] Task 10 — `get_this_value()` with `os.getenv("THISVALUE")`
- [x] Task 11 — `custom_module.py` + `set_that_secret()`
- [x] Task 12 — `read_minutes()` with rows as tuples
- [x] Task 13 — `create_minutes_set()` (union)
- [x] Task 14 — `create_minutes_list()` with `map` and `strptime`
- [x] Task 15 — `write_sorted_list()` writes `./minutes.csv`
- [x] All 14 PyTest tests pass
- [x] Mindset response written

## Mindset Response — AI for Learning

> “Artificial intelligence is not a substitute for human intelligence; it is a tool to amplify human creativity and ingenuity.” — Fei-Fei Li

**1. Have you ever used any AI tools (ex. chatGPT, Grammerly, Dall-E, etc.)? If yes, what did you use it for? If no, did you choose not to use AI, or you just haven't explored it/aren't aware of how to use it?**

Yes, every day. I use AI coding assistants on my own projects and for the student orgs I help run, plus summarizing long docs and figuring out what an error actually means. Since last class I use it even more, so the main change is I've gotten stricter about checking it. It has told me about functions and flags that don't exist with total confidence, so I treat what it says as a lead and verify it by running the code or checking the real docs.

**2. What are ways you think AI can help you as you learn content throughout this class?**

Explaining the "why" in plain English when a traceback makes no sense to me, making extra practice problems on stuff I'm shaky on (this week: filter() vs. a loop, and why the rows had to be tuples before going into a set), and reviewing code I already wrote. The CTD lessons now have AI Learning Prompts built in, like predict-then-check, which is basically the way I want to use it: I commit to an answer first, then it checks me.

**3. What are ways that AI can cause frustration or negatively impact your learning?**

The risk isn't wrong answers, it's right answers too early. Being stuck is where I learn, and a working answer skips that part. It also tends to answer above the level of the class, using patterns we haven't covered, so it works but I can't explain it. My rule is the same as last class: I don't turn in code I can't explain line by line, and I use AI to explain, not to replace the thinking.


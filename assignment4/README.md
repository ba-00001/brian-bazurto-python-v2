# Assignment 4 — Intro to Data Engineering

[← Course index](../README.md)

Creating, loading, inspecting and cleaning data with pandas DataFrames.

## Submission links

| # | Item | Link |
|---|------|------|
| URL1 | Pull request | https://github.com/ba-00001/brian-bazurto-python-v2/pull/4 |

## Files

| File | What it does | Tasks |
|------|--------------|-------|
| `assignment4.py` | All the code: builds DataFrames, reads/writes CSV and JSON, inspects and cleans data | 1–4 |
| `employees.csv` | Written by the script from `task1_older` (no index), then read back in | 1.4, 2.1 |
| `additional_employees.json` | Hand-made file with Eve and Frank, loaded into `json_employees` | 2.2 |
| `dirty_data.csv` | Provided messy data that gets cleaned into `clean_data` | 4 |
| `assignment4-test.py` | Provided unit tests | all |

## How to run

From inside `assignment4/`:

```
python3 assignment4.py
python3 -m pytest -v -x assignment4-test.py
```

## Test results

```
collected 18 items
...
============================== 18 passed in 0.28s ==============================
```

## Requirements checklist

- [x] Task 1.1 — `task1_data_frame` from the Name/Age/City dictionary
- [x] Task 1.2 — `task1_with_salary` is a `.copy()` with `Salary` = 70000, 80000, 90000
- [x] Task 1.3 — `task1_older` is a `.copy()` with `Age` + 1
- [x] Task 1.4 — `employees.csv` saved with `index=False`
- [x] Task 2.1 — `task2_employees` read from `employees.csv`
- [x] Task 2.2 — `additional_employees.json` (Eve, Frank) loaded into `json_employees`
- [x] Task 2.3 — `more_employees` combined with `pd.concat(..., ignore_index=True)`, shape (5, 4)
- [x] Task 3.1 — `first_three` with `head(3)`
- [x] Task 3.2 — `last_two` with `tail(2)`
- [x] Task 3.3 — `employee_shape` = (5, 4)
- [x] Task 3.4 — `more_employees.info()` called
- [x] Task 4.1 — `dirty_data` read raw from `dirty_data.csv`, `clean_data` is a `.copy()`
- [x] Task 4.2 — duplicate rows dropped (6 rows left)
- [x] Task 4.3 — `Age` converted to numeric, bad values coerced to NaN
- [x] Task 4.4 — `unknown` / `n/a` replaced with NaN, `Salary` converted to numeric
- [x] Task 4.5 — `Age` filled with mean, `Salary` filled with median, no nulls left
- [x] Task 4.6 — `Hire Date` converted with `format='mixed'`, no NaT values
- [x] Task 4.7 — `Name` and `Department` stripped and uppercased

## Mindset Response — Curiosity to Learn

> “Stay hungry. Stay foolish.” — Steve Jobs

**1. What’s one thing that you were curious to learn more about recently (this doesn't need to be coding-related)? How did you learn more about it?**

How hackathon organizers decide what makes an event actually go well. I staff hackathons as an MLH coach, and after each one we fill out a post-event questionnaire. I got curious about which things in those surveys actually line up with a good event versus just feeling good. I learned by comparing notes across events I worked, asking other coaches, and reading what MLH publishes for organizers. Kind of a data question in disguise, which is probably why it stuck with me this week.

**2. What’s one best practice you’ve learned in your first few weeks at CTD that you don’t know “the why” behind? How can you find out “the why”?**

Last class it was branches + PRs; I get that one now. This time: writing CSVs with index=False and the "avoid inplace=True" advice. I know what they do, not why they're the default advice. To find out: read the pandas docs on to_csv and the discussion about inplace being deprecated, then break it on purpose (write a CSV with the index, read it back, and see the extra "Unnamed: 0" column show up). Asking a mentor what goes wrong in a real pipeline when you skip it is the other way.


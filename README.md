# Brian Bazurto — Python 100 v2 (Python for Data Analysis 26.4)

Coursework for **Code the Dream — Python 100 v2, Python for Data Analysis 26.4** (Sep 23 – Dec 15, 2026).

This repository is my copy of [Code-the-Dream-School/python_homework](https://github.com/Code-the-Dream-School/python_homework)
(the original setup instructions are in [CTD-SETUP.md](CTD-SETUP.md)). Each assignment has its **own branch, its own
folder, and its own pull request into `main`**, so everything a reviewer needs for a week is in one place:
the code, the tests, a README with sample output, a requirements checklist and my mindset response.

## Assignment index

| Week | Lesson | Due | Branch | Folder | Pull request | Submitted as |
| :-: | --- | --- | --- | --- | :-: | --- |
| 0 | Learning to Learn | Sep 29 | — | — | — | Week 0 form (no code) |
| 1 | Intro to Python | Oct 6 | [`assignment1`](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment1) | [assignment1/](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment1/assignment1) | [#1](https://github.com/ba-00001/brian-bazurto-python-v2/pull/1) | PR |
| 2 | Data Structures and File Handling | Oct 13 | [`assignment2`](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment2) | [assignment2/](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment2/assignment2) | [#2](https://github.com/ba-00001/brian-bazurto-python-v2/pull/2) | PR |
| 3 | More Python Skills | Oct 20 | [`assignment3`](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment3) | [assignment3/](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment3/assignment3) | [#3](https://github.com/ba-00001/brian-bazurto-python-v2/pull/3) | PR |
| 4 | Intro to Data Engineering | Oct 27 | [`assignment4`](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment4) | [assignment4/](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment4/assignment4) | [#4](https://github.com/ba-00001/brian-bazurto-python-v2/pull/4) | PR |
| 5 | Data Cleaning and Validation | Nov 3 | [`assignment5`](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment5) | [assignment5/](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment5/assignment5) | [#5](https://github.com/ba-00001/brian-bazurto-python-v2/pull/5) | Kaggle notebook + PR |
| 6 | Data Wrangling and Aggregation | Nov 10 | [`assignment6`](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment6) | [assignment6/](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment6/assignment6) | [#6](https://github.com/ba-00001/brian-bazurto-python-v2/pull/6) | Kaggle notebook + PR |
| 7–11 | Visualization, web scraping, SQL | Nov 17 – Dec 15 | — | — | — | not started |

Pull requests stay **open** until the reviewer approves them; merging is done after approval.

## Final project (capstone)

The Kaggle data pipeline capstone uses the **Global Superstore** dataset. It starts in Week 5 and grows every week.
The notebook source is in [`final-project/`](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment6/final-project) (Week 5 version on the
`assignment5` branch, Week 6 version on `assignment6`); the live version is the Kaggle notebook linked in its README.

## Running locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows Git Bash: source .venv/Scripts/activate
pip install -r requirements.txt
cd assignment1 && pytest -v -x assignment1-test.py
```

Assignments 1, 2 and 4 have PyTest suites; 3 is checked by running the scripts; 5 and 6 are Kaggle notebooks.

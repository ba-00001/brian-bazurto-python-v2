# Assignment 6 — Data Wrangling and Aggregation

[← Course index](../README.md)

Kaggle notebook `CTD_Assignment_6`: selection, groupby aggregation, pivot tables, `apply()`, merge/join, filtering, sorting, renaming, concatenation, and reshaping the international football results.

## Submission links

| # | Item | Link |
|---|------|------|
| URL1 | Kaggle notebook (`CTD_Assignment_6`) | https://www.kaggle.com/code/acerpc/ctd-assignment-6 |
| URL2 | Capstone Kaggle notebook | https://www.kaggle.com/code/acerpc/ctd-python-data-pipeline |
| — | Pull request | https://github.com/ba-00001/brian-bazurto-python-v2/pull/6 |

Task 13 (final project) is in [`final-project/`](../final-project/README.md) and in its own Kaggle notebook, which goes in the second link on the submission form: https://www.kaggle.com/code/acerpc/ctd-python-data-pipeline

## Files

| File | What it is | Tasks |
|------|------------|-------|
| `CTD_Assignment_6.ipynb` | Notebook source imported into Kaggle. Outputs are cleared here; the run against the real Kaggle inputs is in the shared Kaggle notebook (URL1) | 1–12 |
| [`../final-project/`](../final-project/README.md) | Capstone notebook (Global Superstore), Week 6 progress | 13 |

The notebook reads its datasets from `/kaggle/input` (it falls back to a local `./data/` folder, which is git-ignored, for offline runs).

## Kaggle setup

1. Kaggle → **Create** → **Notebook** → **File** → **Import Notebook** → upload `CTD_Assignment_6.ipynb`. Rename it `CTD_Assignment_6` if needed.
2. Right sidebar → **Add Input** → **Datasets**, search and add:
   - `Ecommerce Consumer Behavior` — by **Salahuddin Ahmed** (Task 3)
   - `AI-Powered Job Recommendations` — by **Samay Ashar** (Task 4)
   - `international football results` — by **Mart Jürisoo** (Task 11)
3. **Run All**. The first cell lists every file under `/kaggle/input`; `find_csvs()` picks each file (by columns, by name, or `results.csv`), so no paths need editing.
4. **Save Version** (quick save, defaults).
5. **Share** → **Public**, make sure **Allow comments** is on, copy the URL into URL1 above and the submission form. The capstone notebook URL goes in the second field of the form.

## Task summary

- **Task 1** — `df1`, `df2`, `df3` built and printed; `Name`, `[['Name','Salary']]` and `iloc[0:3]` selections from `df1`.
- **Task 2** — `df1.groupby('Age')['Salary'].agg(['mean','sum','count'])`.
- **Task 3** — `ecommerce` loaded, `Purchase_Amount` converted with `str.replace('$', '', regex=False)` to float, `buying_patterns` and `demographics` pivot tables.
- **Task 4** — `jobs` loaded, `apply(axis=1)` adds `Check These Out` (Yes/No), `my_jobs` holds the Yes rows.
- **Task 5** — Outer merge into `df_1_3_merged` with `_left`/`_right` suffixes, fills (15000, `'yellow'`), `Age` via `np.where`, drop old ages; `join()` on `Name` index with `lsuffix`/`rsuffix`.
- **Task 6** — `df1` rows with `Age > 30`.
- **Task 7** — `df1` sorted by `Salary` descending.
- **Task 8** — Renamed copy with `Employee Age` / `Employee Salary` (no `inplace`).
- **Task 9** — `df1` salaries raised 10%.
- **Task 10** — `pd.concat([df1, df2], ignore_index=True)`, 10 rows.
- **Task 11** — `football_results` → `results_1` → home (`results_2`) and away (`results_3`) views → concatenated back into `football_results`; `points_against` mean per team sorted descending, top 10.
- **Task 12** — Tunisia's 10 most recent games sorted by date, newest first.

## Requirements checklist

- [x] Notebook named `CTD_Assignment_6`, default Kaggle first cell kept, each task introduced by a markdown cell
- [x] Task 1 — `df1`/`df2`/`df3` with columns `Name`, `Age`, `Salary`, `Favorite Color`, printed
- [x] Task 1 — `Name` column, `Name` + `Salary` (double brackets), first three rows with `iloc`
- [x] Task 2 — `df1` grouped by `Age`, `Salary` mean, sum and count shown
- [x] Task 3 — `ecommerce` read (Salahuddin Ahmed dataset), first 5 rows printed
- [x] Task 3 — `Purchase_Amount` converted to float with `str.replace('$', '', regex=False)` before summing
- [x] Task 3 — `buying_patterns`: index `Purchase_Category`, columns `Gender` + `Income_Level`, sum of `Purchase_Amount`, printed
- [x] Task 3 — `demographics`: index `Income_Level` + `Education_Level`, columns `Marital_Status`, count of `Customer_ID`, printed
- [x] Task 4 — `jobs` read (Samay Ashar dataset), first 10 rows printed
- [x] Task 4 — `apply(..., axis=1)` adds `Check These Out` = `"Yes"` for entry level, salary ≥ 70000, SQL and Python, else `"No"`
- [x] Task 4 — `my_jobs` = rows with `Yes`, first 10 printed
- [x] Task 5 — `df_1_3_merged` outer merge on `Name`, `suffixes=['_left','_right']`, printed
- [x] Task 5 — `Salary` NaN → 15000, `Favorite Color` NaN → `'yellow'`, printed
- [x] Task 5 — `Age` built with the given `np.where` line, printed; `Age_left`/`Age_right` dropped, printed
- [x] Task 5 — `df1_b`/`df3_b` with `Name` index, outer `join` with `lsuffix`/`rsuffix`, no `inplace=True`
- [x] Task 6 — `df1[df1['Age'] > 30]`
- [x] Task 7 — `sort_values('Salary', ascending=False)`
- [x] Task 8 — rename to `Employee Age` / `Employee Salary` without `inplace=True`
- [x] Task 9 — `df1` salary × 1.1
- [x] Task 10 — `concat` of `df1` and `df2` with `ignore_index=True` (index 0–9)
- [x] Task 11 — `results.csv` (Mart Jürisoo) into `football_results`, first 5 printed
- [x] Task 11 — `results_1`, `results_2`, `results_3` with the specified columns and renames, each printed
- [x] Task 11 — concat with `ignore_index=True` reassigned to `football_results`
- [x] Task 11 — `points_against = groupby('team')['points_against'].mean()`, sorted descending, top 10
- [x] Task 12 — Tunisia filtered, sorted by `date` descending, 10 most recent stored in a new DataFrame and printed
- [x] Task 13 — capstone Week 6 work in `final-project/` + its own Kaggle notebook
- [ ] Notebook saved and shared Public with comments on (done on Kaggle)

## Mindset Response — Problem Solving

> “The most dangerous phrase is: ‘We’ve always done it this way.’” — Grace Hopper

**1. Do you already have a problem solving process in place that you’ve found effective? If so, tell us about it!**

Yes, and it's mostly the same as last class: reproduce it, write down expected vs. actual in two sentences, cut it down, change one thing at a time. For data problems I added a step at the front: look at the data before writing anything (head, info, value_counts). In the capstone I was about to group customers by Customer ID until I looked and saw 4,873 IDs but only 795 names, because the same person gets a different ID in each market. That changed the plan to grouping by Customer Name.

**2. Have you observed others in the class solving problems differently than you do? What have you learned from their problem solving techniques?**

Yes. Some people read the whole task and talk through what the output should look like before touching the keyboard. I tend to start typing right away. Their way ends up faster because they're not discovering the requirements by running into them. I've also noticed people chain small pandas steps and check the shape after each one instead of writing one big line, which makes it obvious where things go wrong. I'm trying to do both.


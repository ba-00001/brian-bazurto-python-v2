# Assignment 5 — Data Cleaning and Validation

[← Course index](../README.md)

Kaggle notebook `CTD_Assignment_5`: handling missing data, type conversion, range checks, duplicates, text standardization, encoding, fuzzy-matching cleanup of messy files, and regex examples.

## Submission hub — everything for this week

This README is the single link I submit for Week 5. Every deliverable is linked below, and the mindset response is at the bottom of this page.

| Deliverable | Link |
|---|---|
| **Pull request** (code + review) | [#5](https://github.com/ba-00001/brian-bazurto-python-v2/pull/5) |
| Folder on branch `assignment5` | [assignment5/](https://github.com/ba-00001/brian-bazurto-python-v2/tree/assignment5/assignment5) |
| **Kaggle notebook** (public, run with outputs) | [ctd-assignment-5](https://www.kaggle.com/code/acerpc/ctd-assignment-5) |
| Colab copy (same code, public) | [Open in Colab](https://colab.research.google.com/drive/1PAs1W7DB7ep7DRKyOY92Vw0IbsX1PQan) |
| **Capstone / final project** — Kaggle (public) | [ctd-python-data-pipeline](https://www.kaggle.com/code/acerpc/ctd-python-data-pipeline) |
| Capstone — Colab copy (public) | [Open in Colab](https://colab.research.google.com/drive/1hlMLzbSWdUzTomWZooXEYugzOq-i0iLn) |
| Capstone — notebook source + README | [final-project/](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment5/final-project/README.md) |
| `CTD_Assignment_5.ipynb` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment5/assignment5/CTD_Assignment_5.ipynb) |
| `CTD_Assignment_5_Colab.ipynb` | [view](https://github.com/ba-00001/brian-bazurto-python-v2/blob/assignment5/assignment5/CTD_Assignment_5_Colab.ipynb) |
| Mindset response | [Debugging](#mindset-response--debugging) |
| Lesson page (CTD Learns) | [Week 5](https://classes.codethedream.org/course/python-100-v2/python-for-data-analysis-26.4?week=5&lesson=Data%20Cleaning%20and%20Validation) |

## Files

| File | What it is | Tasks |
|------|------------|-------|
| [`CTD_Assignment_5.ipynb`](CTD_Assignment_5.ipynb) | Notebook source imported into Kaggle. Outputs are cleared here; the run with outputs is in the public Kaggle notebook linked above (Colab copy too) | 1–9 |
| [`CTD_Assignment_5_Colab.ipynb`](CTD_Assignment_5_Colab.ipynb) | Same notebook for Google Colab: the first cell downloads the Kaggle datasets with `kagglehub`. Public Colab copy linked above | all |
| [`../final-project/`](../final-project/README.md) | Capstone notebook (Global Superstore), Week 5 progress | 10 |

The notebook reads its datasets from `/kaggle/input` (it falls back to a local `./data/` folder, which is git-ignored, for offline runs).

## Kaggle setup

> Note: my Kaggle account doesn't have Internet enabled yet (it needs phone verification), so `pip install thefuzz` can't run there. Task 7 falls back to the same `extractOne` idea built on `difflib` from the standard library; with Internet on, it uses `thefuzz` as written.

1. Kaggle → **Create** → **Notebook** → **File** → **Import Notebook** → upload `CTD_Assignment_5.ipynb`. Rename it `CTD_Assignment_5` if needed.
2. Right sidebar → **Input** → **Add Input** → **Datasets**, search and add each of these (the assignment gives search terms only, no author):
   - `code the dream lesson 5` (Task 1)
   - `Code The Dream Eclipses` (Task 2)
   - `Code The Dream Assignment 6` (Task 7, 4 CSV files)
3. **Settings** → turn **Internet** on, so `!pip install thefuzz` works in Task 7 if it is not already installed.
4. **Run All**. The first cell lists every file under `/kaggle/input`; the `find_csvs()` helper picks each file by its column names, so no paths need editing.
5. **Save Version** (quick save, defaults).
6. **Share** → **Public**, make sure **Allow comments** is on, copy the URL into URL1 above and the submission form.

## Task summary

- **Task 1** — Read lesson 5 data into `df`, `df1 = df.dropna()` with `info()` on both, `fillna` (Name `'Unknown'`, Age mean, Salary median, Join Date `'2020-01-01'`), `df2` = dropna + reset index, Age to int.
- **Task 2** — Read eclipses into `df3` with `sep="|"`, show `info()`/`head()`, show the failing `to_datetime`, then convert with `errors='coerce'` and print 20 rows.
- **Task 3** — Ages under 18 or over 65 in `df2` set to `np.nan`, then filled with the median.
- **Task 4** — `duplicate_series = df3.duplicated()`, show duplicates and counts, `drop_duplicates()`; replace `df2` ages over 100 or under 0 with the median.
- **Task 5** — `Name` lowercased and stripped; city variants (NYC, LA, ...) mapped to New York / Los Angeles.
- **Task 6** — `df_color` with `map()` label encoding and `pd.get_dummies(prefix="Color")`.
- **Task 7** — Four files concatenated into `df_all`, fuzzy fixes for Name and Address with `thefuzz`, mode fix for Zip and Phone, duplicates dropped to about 400 records, remaining nulls shown.
- **Task 8** — The four regex examples run with output.
- **Task 9** — Markdown reflection on issues found, best techniques and automation.

## Requirements checklist

- [x] Notebook named `CTD_Assignment_5`, default Kaggle first cell kept, each task introduced by a markdown cell
- [x] Inputs added by the given search terms; paths resolved from `/kaggle/input`
- [x] Task 1 — `df` read from the "code the dream lesson 5" CSV and printed
- [x] Task 1 — `df1 = df.dropna()`, `df.info()` and `df1.info()` called (not printed)
- [x] Task 1 — `fillna`: Name `'Unknown'`, Age **mean**, Salary **median**, Join Date `'2020-01-01'`
- [x] Task 1 — `df2 = df.dropna().reset_index(drop=True)`, `df2['Age'].astype(int)`, printed
- [x] Task 2 — `df3` read with `sep="|"`, `info()` and first 5 rows shown
- [x] Task 2 — plain `pd.to_datetime` error shown, then `errors='coerce'`, first 20 rows printed (bad dates become `NaT`)
- [x] Task 3 — ages `< 18` or `> 65` set to `np.nan` (not the string), printed, filled with the **median**, printed
- [x] Task 4 — `df3.info()`, `duplicate_series = df3.duplicated()`, `df3[duplicate_series == True].head(10)`, `value_counts()`, `drop_duplicates()`, `info()` again
- [x] Task 4 — `df2` ages `> 100` or `< 0` replaced with the **median**, printed
- [x] Task 5 — `Name` → `str.lower().str.strip()`, printed
- [x] Task 5 — `groupby('City')` diagnostic, `NYC` → `New York`, `LA` → `Los Angeles`, printed
- [x] Task 6 — `df_color` with `Color` = Red, Blue, Green, Blue; `Color_Label` via `map`; `df_encoded` via `get_dummies(prefix="Color")`; displayed
- [x] Task 7 — 4 CSVs concatenated with `ignore_index=True` into `df_all` (~1600 rows)
- [x] Task 7 — `thefuzz` try/except install and import
- [x] Task 7 — fuzzy fix for **both** `Name` and `Address` (one helper function)
- [x] Task 7 — `fix_anomaly` with `groupby(["Name","Address"]).transform()` for `Zip` and `Phone`
- [x] Task 7 — `drop_duplicates()` to about 400 records, `info()` and remaining nulls shown
- [x] Task 8 — all four regex examples run with output
- [x] Task 9 — reflection markdown covering common issues, best techniques, automation
- [x] Task 10 — capstone Week 5 work in `final-project/` + its own Kaggle notebook
- [ ] Notebook saved and shared Public with comments on (done on Kaggle)

## Mindset Response — Debugging

> “Debugging is twice as hard as writing the code in the first place.” — Brian Kernighan

**1. When asked to think about debugging, what are the first 3 adjectives that jump to mind?**

Humbling, repetitive, clarifying. Same three as last class. Humbling because the bug is almost always mine. Repetitive because it's usually wrong type, wrong path, or wrong assumption about the data. Clarifying because a bug is the only time the code shows me what it's really doing. In pandas I'd add "sneaky": in Week 4 the Salary and Hire Date columns had stray spaces, so values that looked fine weren't matching.

**2. What are some debugging practices you've already found helpful and one or two you would like to try when you next encounter bugs in your code?**

Helpful: reading the whole traceback bottom line first, printing the type and not just the value, and shrinking the problem until it's the only thing left. For data work: df.info(), df.head(), and checking .unique() on a column before trusting it.

Last class I said I wanted to try a real debugger and writing my hypothesis down before testing. I did start writing the hypothesis down and it helped. I still mostly use print(), so this class I want to actually use breakpoint()/the VS Code debugger, and in Kaggle run cells one at a time instead of Run All when something is off.


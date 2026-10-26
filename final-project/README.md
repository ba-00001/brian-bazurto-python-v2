# CTD Python Data Pipeline — Global Superstore

**Goal:** find out what drives profit (not just sales) at a global retailer: discounts, product categories, markets/regions and shipping.

Code the Dream, Python 100 final project (capstone) by Brian Bazurto ([ba-00001](https://github.com/ba-00001)).

**Kaggle notebook:** https://www.kaggle.com/code/acerpc/ctd-python-data-pipeline

## Dataset

- **Title:** Global Superstore
- **Author:** anandaramg
- **URL:** https://www.kaggle.com/datasets/anandaramg/global-superstore/data
- **File:** `Global Superstore.txt`: tab-separated, UTF-8, 15.6 MB, 51,290 rows x 27 columns
- **Kaggle path (as attached on my run):** `/kaggle/input/datasets/anandaramg/global-superstore/Global Superstore.txt`

The notebook does not hard-code that path. It searches `/kaggle/input` for any `.txt`/`.csv`/`.xlsx` file with "superstore" in the name and reads `.txt` with `sep="\t"`. Outside Kaggle it falls back to `./data/`.

*Local-test note:* `data/Global Superstore.txt` is a stand-in I built for running the notebook offline. I converted a public GitHub copy of the same data (`Global_Superstore2.csv`) into the Kaggle file's format: same 27 columns and order, tab-separated, same helper columns. It is close to the Kaggle file but not byte-identical, so the Kaggle run is the one to submit.

## Kaggle setup

1. On Kaggle, go to **Code > New Notebook**, then **File > Import Notebook** and upload `CTD_Python_Data_Pipeline.ipynb`.
2. In the right panel, click **Add Input**, search for **"Global Superstore"** and add the dataset by **anandaramg** (https://www.kaggle.com/datasets/anandaramg/global-superstore).
3. Click **Run All**. The first cell lists the files under `/kaggle/input`, and the loader finds `Global Superstore.txt` automatically.
4. Click **Save Version** (quick save, accept the defaults).
5. Click **Share**, set it to **Public**, turn on **Allow comments**, and copy the URL into the submission form (second link field). Replace `https://www.kaggle.com/code/acerpc/ctd-python-data-pipeline` above with it.

## Progress

| Week | Section | Status |
|---|---|---|
| 5 | Loading, inspection, data cleaning | Done |
| 6 | Wrangling, aggregation, feature engineering | Next week |
| 7+ | Visualization, analysis, conclusions | Pending |

## Checklist

### Week 5: capstone goals

- [x] Kaggle notebook created for the final project
- [x] Dataset chosen from the four curated options (Global Superstore)
- [x] Data loaded with the right delimiter (`read_csv(sep="\t")`) and a robust recursive path search
- [x] Inspected with `head()`, `tail()`, `info()`, `describe()`
- [x] Constant / redundant columns: `记录数` (always 1) and `Market2` (duplicates `Market`) dropped; `Year` and `weeknum` validated against `Order Date`, then dropped
- [x] Incorrect types: date strings converted with `to_datetime` (explicit format, 0 `NaT`); category dtypes and an ordered `Order Priority`
- [x] Missing values: none in the file; pipeline guard with `dropna` on key fields and `fillna` on text fields
- [x] Duplicates: 0 exact; 9 key-based near-duplicates inspected and kept (split shipments); `drop_duplicates()` in the pipeline
- [x] ID issues: 4,873 Customer IDs vs 795 names (per-market IDs); 457 Product IDs with multiple names, both shown in code and documented
- [x] Discount artifacts (0.002 / 0.202 / 0.402 / 0.602) found and handled in the binning
- [x] Range checks (1 zero-sales row noted) and IQR outlier check, with a written decision to keep outliers
- [x] Markdown cells explaining each issue and fix
- [x] Cleaning steps organized into functions (`clean_superstore()` pipeline)

### Coming in Week 7+

- [ ] 3+ visualizations with explanations
- [ ] At least 3 conclusions backed by charts and text
- [ ] Limitations and final summary

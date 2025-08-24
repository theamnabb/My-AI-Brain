# 📌 Introduction to Pandas

Pandas is a **Python library** for **data manipulation and analysis**.

The name comes from **“Panel Data”** (a term used in econometrics) and also hints at “Python Data Analysis.”

It lets you work with **tabular data** (like rows and columns in a spreadsheet) in a very fast and flexible way.

### The two core data structures are:

- **Series** → a 1-dimensional labeled array (like a single column).

- **DataFrame** → a 2-dimensional labeled data table (like an Excel sheet).

#  When and Why Pandas Was Created

Created in **2008 by Wes McKinney** while working at a hedge fund called **AQR Capital**.

At that time, Python already had NumPy for numerical computations, but NumPy wasn’t great for:

- Handling labeled data (row/column names instead of just numbers).

- Missing data handling.

- Time series data manipulation (very important in finance).

Wes needed a tool for finance data analysis that was:

- Fast (built on top of NumPy’s C-optimized arrays).

- Convenient (Excel-like but programmable).

- Flexible (could handle messy, real-world data).

So he created Pandas → which quickly became the standard for data analysis in Python.
Later, it became open source and the community made it much bigger than finance (now used in science, business, AI, everywhere).

# How to get started with Pandas 
- Install Pandas

```bash
pip install pandas
```
- Import Pandas

```bash
import pandas as pd
```

---

# Key Concept of Pandas

- Series: A Series is like one column of data.
- DataFrame: A DataFrame is like a full Excel sheet (rows + columns).
- [How to create Series & DataFrame](./Series_DataFrame.ipynb)
- Basic attributes: .shape, .columns, .index, .dtypes

# Common Issues When Reading Data with Pandas 
- Encoding Problems (UTF-8, Latin-1, etc.)
- Large data → break down in to small chunks
- Data Stored in Cloud (Google Cloud, AWS, etc.) then use (gcsfs library) for read data from google cloud
> These are real-world issues that make Pandas more than just “toy examples.”

# How to save & use data afer Data Manipulation 
- how to create dataFrame and then save
- [save.py](./Basic/save.py)

# Why we need to Explore the data
- To understand th DataSet (Datatype, which kind of data)
- identitfy the problems
- plan the next steps

> For explore the data we need to load the data first and check the data to organize the data

In Python Pandas,

## [Viewing data:](./Basic/Series_DataFrame.ipynb) 
> .head(), .tail(), .info(), .describe()

**head()** → shows the first few rows of a DataFrame (default = 5).

**tail()** → shows the last few rows of a DataFrame (default = 5).

**Info()** → The info() method in pandas is used to quickly get a summary of a DataFrame. (data health report)
```bash
df.info()
```
It gives:

- Index Range → e.g. RangeIndex: 100 entries, 0 to 99

- Column Names

- Number of Non-Null (non-missing) values per column

- Data Types (int64, float64, object, bool, etc.)

- Memory Usage of the DataFrame

**describe()** → The info() method in pandas is used to quickly get a summary of a DataFrame. (data health report)
```bash
df.describe()
```
Gives statistical summary of your data.

Focuses on:

- Count (non-null values)

- Mean

- Standard deviation

- Min, 25%, 50%, 75%, Max (percentiles)

- 👉 Think of it as a "**data statistics report**".

# Adding, dropping, and Renaming columns/rows
- Adding (Column, insert()),Add column on condition
- Dropping: drop()


# Selecting Data: 

> .loc[], .iloc[], filtering rows and columns

# Handling missing data: 

> .isnull(), .dropna(), .fillna()

- ## .isnull()
    👉 **What it does:**

    - Checks if each value in the DataFrame (or Series) is missing (NaN).

    - Returns **True** if missing, **False** if not missing.

    - It does not change the data, only shows where the missing values are.

    👉 **Why we use it:**

    - To detect missing values before cleaning the dataset.

    - Helpful for analysis before dropping or filling missing values.

- ## .dropna()
    👉 **What it does:**

    Removes rows or columns that contain missing values.

    By default, it drops rows (axis=0).

    👉 Why we use it:

    When missing data is small and not important, we can safely remove it.

    Useful if we want a clean dataset without NaN values.

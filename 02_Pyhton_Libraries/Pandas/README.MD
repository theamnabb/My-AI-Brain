# 📌 Introduction to Pandas

Pandas is a **Python library** for **data manipulation and analysis**.

The name comes from **“Panel Data”** (a term used in econometrics) and also hints at “Python Data Analysis.”

It lets you work with **tabular data** (like rows and columns in a spreadsheet) in a very fast and flexible way.

### The two core data structures are:

- **Series** → a 1-dimensional labeled array (like a single column).

- **DataFrame** → a 2-dimensional labeled data table (like an Excel sheet).

##  When and Why Pandas Was Created

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
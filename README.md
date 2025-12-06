# statistical-tests-python
 
📊 **Statistical Tests in Python**

This repository contains Python programs that perform important statistical hypothesis tests such as:

F-Test (to compare variances of two datasets)

Z-Test (to compare means when population variance is known / large sample)

T-Test (to compare means when population variance is unknown)

These programs are useful for students, researchers, and data analysts who want to quickly perform statistical tests on CSV or Excel datasets using Python.

📊 **Project Flow **
| Step No. | Process                | Description                                                                                     |
| -------- | ---------------------- | ----------------------------------------------------------------------------------------------- |
| **1**    | **Load Dataset**       | Reads CSV or Excel files using file paths defined inside `tests.py`.                            |
| **2**    | **Data Preprocessing** | Extracts required columns, handles missing values, and prepares arrays for statistical testing. |
| **3**    | **Perform F-Test**     | Compares variances of two datasets and determines if population variances are equal.            |
| **4**    | **Perform T-Test**     | Compares means of two independent samples when population variance is unknown.                  |
| **5**    | **Perform Z-Test**     | Compares means when population variance is known or sample size is large.                       |

📁 **Project Files**
| File Name                            | Type          | Description                                                                                                                           |
| ------------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **deliveries.xlsx**                  | Excel File    | Sample dataset containing numeric values used for hypothesis testing.                                                                 |
| **matches (1) - Google Sheets.xlsx** | Excel File    | Another sample dataset that can be used for F-Test, T-Test, or Z-Test.                                                                |
| **tests.py**                         | Python Script | Contains code to load datasets, perform all statistical tests, and display results. Users can modify file paths to load new datasets. |
| **README.md**                        | Documentation | Contains the project description, features, instructions, test explanations, and project flow.                                        |



🧪 **Features of This Project**

✔ **Performs three major hypothesis tests:**

**F-Test:** Checks whether two populations have equal variance.

**Two-Sample T-Test:** Compares the means of two samples.

**Z-Test:** Used when sample size is large or population variance is known.

✔ **Accepts data from CSV or Excel**

You can load your own dataset by editing the file path inside tests.py.

✔ **Uses standard Python libraries**

**Code uses:**

pandas

numpy

scipy.stats

These are widely used in academic and industry statistical analysis.

🚀 **How to Run the Project**
1. Clone the repository
git clone 
2. Install required libraries
pip install pandas numpy scipy

Run the file
python test.py

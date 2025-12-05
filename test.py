import pandas as pd
import numpy as np
from scipy import stats

# ------------------------------
# Load CSV files
# ------------------------------

df1 = pd.read_csv("heart-disease.csv")
df2 = pd.read_csv("heart failure.csv")

# ------------------------------
# Select a numeric column for testing
# CHANGE this column name according to your data
# ------------------------------
column_name = "age"   # Example; set to a numeric column present in BOTH datasets

data1 = df1[column_name].dropna()
data2 = df2[column_name].dropna()

# ===========================================================
# 1️⃣ F-TEST (Test for equality of variances)
# ===========================================================
var1 = np.var(data1, ddof=1)
var2 = np.var(data2, ddof=1)

F_statistic = var1 / var2
dfn = len(data1) - 1
dfd = len(data2) - 1

p_value_f = 1 - stats.f.cdf(F_statistic, dfn, dfd)
p_value_f = p_value_f * 2  # two-tailed

print("=== F TEST ===")
print("F statistic:", F_statistic)
print("p-value:", p_value_f)

# ===========================================================
# 2️⃣ T-TEST (Two-sample independent t-test)
# ===========================================================
t_stat, p_value_t = stats.ttest_ind(data1, data2, equal_var=False)

print("\n=== T TEST ===")
print("t statistic:", t_stat)
print("p-value:", p_value_t)

# ===========================================================
# 3️⃣ Z-TEST (Two-sample)
# ===========================================================
mean1, mean2 = np.mean(data1), np.mean(data2)
std1, std2 = np.std(data1, ddof=1), np.std(data2, ddof=1)
n1, n2 = len(data1), len(data2)

# Standard error for Z
se = np.sqrt((std1**2)/n1 + (std2**2)/n2)

z_statistic = (mean1 - mean2) / se
p_value_z = 2 * (1 - stats.norm.cdf(abs(z_statistic)))

print("\n=== Z TEST ===")
print("z statistic:", z_statistic)
print("p-value:", p_value_z)

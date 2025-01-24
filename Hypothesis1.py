import pandas as pd
import numpy as np
import scipy
from scipy import stats
from statsmodels.stats import descriptivestats as sd
from statsmodels.stats.weightstats import ztest

# 1. One-sample Sign Test
mark = pd.read_csv("E:/Honars(DS)/Data Science/18-Hypothesis Testing/Signtest.csv")

# Normal QQ plot
import pylab
stats.probplot(mark.Scores, dist='norm', plot=pylab)

# Shapiro-Wilk Test for normality
shapiro_test = stats.shapiro(mark.Scores)
print('Shapiro Test: ', shapiro_test)

# p-value is 0.024 < 0.05, data is not normal

# Descriptive Statistics
print(mark.Scores.describe())

# 1-sample sign test
sign_test_result = sd.sign_test(mark.Scores, mu0=mark.Scores.mean())
print("Sign test result:", sign_test_result)

# Result: p-value = 0.82
# Interpretation: Since the p-value (0.82) is greater than 0.05, we fail to reject the null hypothesis
# Conclusion: The median and mean of scores are statistically not similar.

# 2. One-sample Z-test
fabric = pd.read_csv("E:/Honars(DS)/Data Science/18-Hypothesis Testing/Fabric_data.csv")

# Normality Test
fabric_normality = stats.shapiro(fabric)
print('Fabric Normality Test:', fabric_normality)

# Z-test for fabric length
fabric_mean = np.mean(fabric)
z_test_result, p_val = ztest(fabric["Fabric_length"], value=150)
print("Z-test result:", z_test_result, 'p-value:', p_val)

# Interpretation: p-value = 7.75 * 10^-6, reject null hypothesis
# Conclusion: The mean fabric length significantly differs from 150.

# 3. Mann-Whitney U Test (Non-parametric Test)
fuel = pd.read_csv("E:/Honars(DS)/Data Science/18-Hypothesis Testing/mann_whitney_additive.csv")
fuel.columns = ["Without_additive", "With_additive"]

# Normality Tests
print("Without Additive Normality:", stats.shapiro(fuel.Without_additive))
print("With Additive Normality:", stats.shapiro(fuel.With_additive))

# Mann-Whitney U Test
mannwhitney_result = stats.mannwhitneyu(fuel.Without_additive, fuel.With_additive)
print("Mann-Whitney test result:", mannwhitney_result)

# Interpretation: p-value = 0.445, fail to reject null hypothesis
# Conclusion: Adding fuel additive does not significantly impact performance.

# 4. Paired T-Test
sup = pd.read_csv("E:/Honars(DS)/Data Science/18-Hypothesis Testing/paired2.csv")

# Normality Test
print("Supplier A Normality Test:", stats.shapiro(sup.SupplierA))
print("Supplier B Normality Test:", stats.shapiro(sup.SupplierB))

# Paired T-Test
t_test_result, p_val = stats.ttest_rel(sup['SupplierA'], sup['SupplierB'])
print("Paired T-Test Result:", t_test_result, "P-Value:", p_val)

# Interpretation: p-value = 0.00, reject null hypothesis
# Conclusion: There is a significant difference in transaction times between Supplier A and Supplier B.

# 5. Two-Sample T-Test
offers = pd.read_excel("E:/Honars(DS)/Data Science/18-Hypothesis Testing/Promotion.xlsx")
offers.columns = ["InterestRateWaiver", "StandardPromotion"]

# Normality Test
print("InterestRateWaiver Normality:", stats.shapiro(offers.InterestRateWaiver))
print("StandardPromotion Normality:", stats.shapiro(offers.StandardPromotion))

# Variance Test (Levene's Test)
levene_test = scipy.stats.levene(offers.InterestRateWaiver, offers.StandardPromotion)
print("Levene Test (Variance):", levene_test)

# Two-Sample T-Test
ttest_result = scipy.stats.ttest_ind(offers.InterestRateWaiver, offers.StandardPromotion)
print("Two-Sample T-Test:", ttest_result)

# Interpretation: p-value = 0.0242, reject null hypothesis
# Conclusion: There is a significant difference between the two promotional offers.

# 6. Mood's Median Test
animals = pd.read_csv("E:/Honars(DS)/Data Science/18-Hypothesis Testing/animals.csv")

# Normality Tests
print("Pooh Normality:", stats.shapiro(animals.Pooh))
print("Piglet Normality:", stats.shapiro(animals.Piglet))
print("Tigger Normality:", stats.shapiro(animals.Tigger))

# Median Test
median_test_result = stats.median_test(animals.Pooh, animals.Piglet, animals.Tigger)
print("Mood Median Test:", median_test_result)

# Interpretation: p-value = 0.189, fail to reject null hypothesis
# Conclusion: The median of Pooh, Piglet, and Tigger are statistically equal.

# 7. One-Way ANOVA Test
contract = pd.read_excel("E:/Honars(DS)/Data Science/18-Hypothesis Testing/ContractRenewal_Data(unstacked).xlsx")
contract.columns = ["Supp_A", "Supp_B", "Supp_C"]

# Normality Test
print("Supp_A Normality:", stats.shapiro(contract.Supp_A))
print("Supp_B Normality:", stats.shapiro(contract.Supp_B))
print("Supp_C Normality:", stats.shapiro(contract.Supp_C))

# Variance Test (Levene's Test)
levene_test = scipy.stats.levene(contract.Supp_A, contract.Supp_B, contract.Supp_C)
print("Levene Test (Variance):", levene_test)

# One-Way ANOVA Test
anova_result = stats.f_oneway(contract.Supp_A, contract.Supp_B, contract.Supp_C)
print("One-Way ANOVA:", anova_result)

# Interpretation: p-value = 0.104, fail to reject null hypothesis
# Conclusion: The transaction times for the three suppliers are not significantly different.

# 8. Two-Proportion Z-Test
soft_drink = pd.read_excel("E:/Honars(DS)/Data Science/18-Hypothesis Testing/JohnnyTalkers.xlsx")

from statsmodels.stats.proportion import proportions_ztest

# Data Preparation
count = np.array([58, 152])  # Example counts for adults and children
nobs = np.array([480, 480])  # Total number of adults and children surveyed

# Two-Proportion Z-Test
z_test_result, p_val = proportions_ztest(count, nobs)
print("Two-Proportion Z-Test result:", z_test_result, "p-value:", p_val)

# Interpretation: p-value = (result), conclusion based on p-value

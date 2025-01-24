# 18-Hypothesis-Testing
Hypothesis testing is a statistical method used to determine whether there is enough evidence to reject a null hypothesis in favor of an alternative hypothesis, based on sample data.
# Hypothesis Testing Project

This project demonstrates the implementation of various statistical hypothesis tests using Python. The tests are performed on multiple datasets to evaluate claims or assumptions made about different variables. The project covers one-sample, two-sample, paired, and non-parametric tests, as well as variance tests and proportion tests.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Datasets](#datasets)
4. [Statistical Tests](#statistical-tests)
    1. [One-sample Sign Test](#one-sample-sign-test)
    2. [One-sample Z-test](#one-sample-z-test)
    3. [Mann-Whitney U Test](#mann-whitney-u-test)
    4. [Paired T-Test](#paired-t-test)
    5. [Two-sample T-Test](#two-sample-t-test)
    6. [Mood's Median Test](#moods-median-test)
    7. [One-Way ANOVA](#one-way-anova)
    8. [Two-Proportion Z-Test](#two-proportion-z-test)
5. [How to Run](#how-to-run)
6. [Conclusion](#conclusion)

## Introduction

This project uses Python's `scipy` and `statsmodels` libraries to perform hypothesis testing on real-world datasets. It includes tests for normality, comparison of means, median tests, and proportions. The tests are suitable for various business and scientific applications such as comparing product performances, analyzing survey data, and testing claims about populations.

## Prerequisites

Before running the tests, make sure you have the following Python libraries installed:

- `pandas`
- `numpy`
- `scipy`
- `statsmodels`
- `pylab` (optional for normal QQ plot)

You can install the necessary libraries using pip:

```bash
pip install pandas numpy scipy statsmodels

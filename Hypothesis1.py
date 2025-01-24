# -- coding: utf-8 --
"""
Created on Tue Jan 14 08:28:12 2025

@author: anuradha
"""

import pandas as pd
import numpy as np
import scipy
from scipy import stats
#provides statistical function:
# stat contain a varity of statistical tests:
from statsmodels.stats import descriptivestats as sd
# provide descriptive statistic tools, including th sign_test

from statsmodels.stats.weightstats import ztest
# used for conducting z-tests on datasets

#1 sample sign test
# whenever there is a single sample and data is not normal
mark = pd.read_csv("E:/Honars(DS)/Data Science/18-Hypothesis Testing/Signtest.csv")

# normal QQ plot
import pylab
stats.probplot(mark.Scores, dist='norm', plot=pylab)
#creates a QQ plot to visully check if the data flows a normal dis
# test for normalitty

shapiro_test = stats.shapiro(mark.Scores)
#perform the shapiro-walk test for norality
#H0 (null hypothesis) the data is normally distributed.
#H1 (alternative hypothesis) the data is not normally distributed
# outout a test statistics and p-value

print('hapiro Test: ',shapiro_test)

#p-value is 0.024 < 0.05 , data is not normal

#descriptie statistics
print(mark.Scores.describe())
#mean = 84.20 and median = 89.00
# 1 -sample sign test
sign_test_result = sd.sign_test(mark.Scores, mu0 = mark.Scores.mean())
print("sign test result :", sign_test_result)

#result :  p-value =0.82
#Interpretation
# H0 the median of scores is equal to the mean of scores
#H1 : the median of scores is not equal to the mean of scores
# since the p-value (0.82) is greater than 0.05, we fail to reject the null hypothesis
#conclusion : the median and mean of scors are statically not similar.
# objective : check the fabric length is exactly 150 or differ?

#1-sample z-test
fabric = pd.read_csv("E:/Honars(DS)/Data Science/18-Hypothesis Testing/Fabric_data.csv")

#normality test 
fabric_normality = stats.shapiro(fabric)
print('fabric normality test :', fabric_normality)
# p value = 0.1460 > 0.05

fabric_mean = np.mean(fabric)
print("Mean Fabric Length :", fabric_mean)

#z-test
z_test_result, p_val = ztest(fabric["Fabric_length"], value=150)
print("z-test result :", z_test_result, 'p-value :', p_val)
#result : p-value = 7.75 * 10^-6

#Interpretation 
# H0 : the mean fabric length is 150
#H1 : the mean fabric lenth is not 150
# since the p-value is extremly small (less than 0.05), we reject the null hypothesis
#conclusion : the mean fabric length significantly differ from
# objective : check is there any difference in performance if additive is added in the 

# Mann-Whitney Test

fuel = pd.read_csv("E:/Honars(DS)/Data Science/18-Hypothesis Testing/mann_whitney_additive.csv")
fuel.columns = ["Without_additive", "with_additive"]

#Normality Tests
print("Without Additive Normality:", stats.shapiro(fuel.Without_additive))
#p=0.50 > 0.05 : accept H0
print("With Additive Normality: ", stats.shapiro(fuel.with_additive))
#0.04 < 0.05 :reject H0 data is not normal
#Mann-Whitney U test

mannwhitney_result = stats.mannwhitneyu(fuel.Without_additive, fuel.with_additive)
print("Mann-whitney test result : ", mannwhitney_result)

#result : p-value = 0.445
# interpretation
#H0: o difference in performance between without_additive and with_additive.
#H1: A signifiacnce difference exists
# since the p-value (0.445) is greater than 0.05 , we fail to reject the null hypothesis

#conclusion: Adding fuel additive does not significantly impact performance
#Applise the Mann-Whitney U test to check it there is a significant difference between with and without additive

#H0 : no difference i performance between the groups
# H1: Significant difference in performance.

# Paired T-Test
sup = pd.read_csv("E:/Honars(DS)/Data Science/18-Hypothesis Testing/paired2.csv")

#Normality test
print("Supplier A Normality Test: ",stats.shapiro(sup.SupplierA))
#p-value = 0.8961 >0.05 : fails to reject the H0 , data is normal

print("Supplier B Normality Test: ",stats.shapiro(sup.SupplierB))
#p-value = 0.8961 >0.05 : fails to reject the H0 , data is normal

# Paired T-Test
t_test_result, p_val = stats.ttest_rel(sup['SupplierA'], sup['SupplierB'])
print("Paired T-Test Result :", t_test_result, "P-Vlue:", p_val)

#Result: p-value = 0.00
#Interpretation
# H0 : No significant difference in transaction times between Supplier A and Suppier B
# H1 : A significannt difference exists.

#Since the p-value (0.00) is less than 0.05 , we reject the null hypothesis.
#conclusion: there is a significanct differnce in transaction times between the Supplier A nad Supplier B

# objective : there is a significant difference in between the promotional offers.

#Two -Sample T-Test
offers = pd.read_excel("E:/Honars(DS)/Data Science/18-Hypothesis Testing/Promotion.xlsx")
offers.columns = ["InerestRateWaiver", "StandardPromotion"]

#normality test
print("InerestRateWaiver Normality : ", stats.shapiro(offers.InerestRateWaiver))
print("StanrdPromotion Normality:",stats.shapiro(offers.StandardPromotion))

#varience
levene_test = scipy.stats.levene(offers.InerestRateWaiver, offers.StandardPromotion)
print("Levene Test (Varience) :", levene_test)

#pvalue = 0.2875
#H0 = varience equal
#H1 = varience unequal
#p-value = 0.2875 > 0.05 fail to reject null hypothesis (H0 is accepted)
# Tow sample T-Test

ttest_result = scipy.stats.ttest_ind(offers.InerestRateWaiver, offers.StandardPromotion)
print("Two-Sample T-Test:",ttest_result)

#Result : p-value =0.0242
# Interpretation 
# H0 : bothe offers have the same mean impact
# h1 : the mean impact of the two offers are different
# since the p-valu (0.0242) is less than 0.05 , we reject the null hypothesis
# conclusion : there is a significant difference between the two promotional offers

#Mood's median test
# objective: is the median is of pooh, piglet , and trigger are statistically equal.
# it has equal median or not

animals =pd.read_csv("E:/Honars(DS)/Data Science/18-Hypothesis Testing/animals.csv")

# Normality tests
print("Pooh Normality :",stats.shapiro(animals.Pooh))
# p-value = 0.0122

print("Piglet Normality :",stats.shapiro(animals.Piglet))
# p-value = 0.044

print("Tigger Normality :",stats.shapiro(animals.Tigger))
# p-value = 0.0219

# H0 : data is normal
# h1 : data is not normal
# Since all p value are less than 0.05 hence object the null hypothesis
# data is not normal , hence Mood's Test

#Median Test
median_test_result = stats.median_test(animals.Pooh, animals.Piglet, animals.Tigger)
print("Mood Median test :",median_test_result)

animals.describe() 

# Result: p-value = 0.189
# Interpretation 
# H0 : All groups have equal median
# H1 : 
# p- value : 0.186
# conclusion : the median of pooh , piglet, tigger are statisticaly equal

# one way anova test
# objective : is the transaction times for the three suppliers are not significantly different.

contract = pd.read_excel("E:/Honars(DS)/Data Science/18-Hypothesis Testing/ContractRenewal_Data(unstacked).xlsx")
contract.columns =["Supp_A", "Supp_B", "Supp_C"]

# Normality test
print("Supp_A normality :", stats.shapiro(contract.Supp_A))
print("Supp_B normality :", stats.shapiro(contract.Supp_B))
print("Supp_C normality :", stats.shapiro(contract.Supp_C))

# All p  -value are greater than 0.05
# we fail to reject the null hypothesis
# i.e H0 is accepted means data is normal
# Vrience test

levene_test = scipy.stats.levene(contract.Supp_A, contract.Supp_B, contract.Supp_C)
print("Levene Test ( varience) :", levene_test)
# H0 : dat is having equal varience

# H1 : data is having differnece in varience
# p - value = 0.7775 > 0.05, H0 is accepted

# ANOVA test
anova_result = stats.f_oneway(contract.Supp_A, contract.Supp_B, contract.Supp_C) 
print("One_way ANOVA:", anova_result)

# result p-value : 0.104
# Interpretation 
# H0 : All suppliers have the same mean transaction time.
# H1 : At least one supplier has a different mean 
# since the p-value (0.104) is greater than 0.05 , we fail to reject
# the null hypothesis

# conclusion : The transaction times for the three suppliers are not




#Two proportion  Z- test

'''
Use a two sided test when we want to detect the difference without assumption
 beforement which  group will have higher or lower portion 
 Example:If theres a difference in soft drink assumption between the adults and the 
  and the children without: assuming which group consumes more.
  
  
  Objective:There  is a signinicant  difference in soft drink consumptions between adults and children
'''

soft_ddrink = pd.read_excel("E:/Honars(DS)/Data Science/18-Hypothesis Testing/JohnyTalkers.xlsx")

from statsmodels.stats.proportion import  proportions_ztest

#Data Preparation

count =np.array([58,152])
nobs=np.array([])

#Similary if 740 children were surveyed and 152 of them reported consuming 
#soft drinks,the second count is 152 .Thus count=[58,152]

#nobs:Represents the total number of individuals surveyed in each group.


#The total number of adults survyed is 480.THe total number of children  surveyed is 480.



#Thses values are often extraccted from a dataset .If your data is in a file
#(like jonyTalkers.xlsx) You can calculate these values as follows:
    
    
    



import pandas as pd

#load the dataset
soft_drink = pd.read_excel("E:/Honars(DS)/Data Science/18-Hypothesis Testing/JohnyTalkers.xlsx")

soft_drink
#filter the data into adults and the children categories
adults=soft_drink[soft_drink['Person']=='Adults']
children=soft_drink[soft_drink['Person']=='Children']







#Count of successor(soft drink consumers) for each group

count_adults=adults[adults['Drink']=='Purchased'].shape[0]

count_children=children[children['Drink']=='Purchased'].shape[0]

#Total observation for each group
nobs_adults=adults.shape[0]
nobs_children=children.shape[0]


#Final array for z-test
count=[count_adults,count_children]
nobs=[nobs_adults,nobs_children]

print("Count(Soft Drink Consumer):",count)
print("Total Observation",nobs)

####################################


import pandas as pd

#load the dataset
soft_drink=pd.read_csv("E:/Honars(DS)/Data Science/18-Hypothesis Testing/JohnyTalkers.csv")
soft_drink
#filter the data into adults and the children categories
adults=soft_drink[soft_drink['Person']=='Adults']
adults
children=soft_drink[soft_drink['Person']=='Children']
children

#count the successes (soft drink customers) for each grpoup
count_adults=adults[adults['Drinks']=='Purchased'].shape[0]
count_children=children[children['Drinks']=='Purchased'].shape[0]
#total observations for each group

nobs_adults=adults.shape[0]
nobs_children=children.shape[1]

#final array for the z-test
count=[count_adults,count_children]
count
nobs=[nobs_adults,nobs_children]
nobs


from statsmodels.stats.proportion import proportions_ztest

#Two sided Test
z_stat,p_val=proportions_ztest(count,nobs,alternative='two-sided')
print("Two Sided Proportional Test :",z_stat,"P value:",p_val)


#resukt p_value is 0.0 

#Interpretation
"""
H0= proportions of adults and children consuming the soft drink are same
H1=Proportions are differenet

Conclusion=There is a significant difference in the soft drink consuption
"""

###########################################################################

#Chi Square Test

#Objective:is defective proportions are independant of the country ?
#THe dataset contain two columns:
    
    #Defective:Indicates whether an item is defective (likely binary,)
    #with 1 for defective and 0 for not defective).
    #COuntry :Specifices the country associated with the item (eg."India")
    #The dataset  has 800 entries and there are no missing values in either
    #column.It appears to be designed to analyzes.
    
    
    
    
import pandas as pd
from scipy.stats import chi2_contingency

# Load the dataset
Bahman = pd.read_excel("E:/Honars(DS)/Data Science/18-Hypothesis Testing/Bahaman.xlsx")

# Cross Tabulation
count = pd.crosstab(Bahman["Defective"], Bahman["Country"])
print(count)

# Perform the Chi-Square test
chi2_result = chi2_contingency(count)

# Display the result
print("Chi-Square Statistic:", chi2_result[0])
print("P-value:", chi2_result[1])
print("Degrees of Freedom:", chi2_result[2])
print("Expected Frequencies:\n", chi2_result[3])


#Result:pvalue=0.6315
#Interpretation :
#H):Defective proportional are independant of the counry


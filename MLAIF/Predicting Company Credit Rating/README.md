Predicting Company Credit Rating
---

**Objective**   
This assignment is to predict corporate events using financial variables. Credit rating is a heated area in finance literature (see Hull et al. 2004; Avramov 2007). The application of machine learning in predicting credit rating is also popular in industry (e.g. Huang et al. 2004; Lee 2007; Khandani et al. 2010).  

**Methods**  
PCA  
Regression: LASSO, Ridge and ElasticNet  
Classification: Logistic Regression, LDA and Naive Bayes  

**Programing language**  
Python  


**Dataset Introduction**  
MLAIF_sample_dataset.csv: a sample dataset intercepted from the original data.  

There are 22 level ratings from D to AAA.

The credit rating has been converted to values following prior studies. This dataset contains a number of financial variables based on financial reports. The data is from Compustat.  

key variables:

Var|Definition
---|---
ratescore|rating score in year t
ratescore_1|rating score in year t+1
rating_1 | rating in year t+1

Predicting Stock Return
---

**Introduction**   
How to predict stock return is one major theme in finance literature (asset pricing). For industry practitioners, the high frequency trading (HFT) is well developed in the US. There is also a growing literature on this issue (see Brogaard et al. 2014; Chaboud et al. 2014; Budish et al. 2015; Biais et al. 2015). It is also getting more and more popular in mainland China and Hong Kong. In typical HFT strategy, the dataset used is tick-by-tick data, which can be accessed in China using level-2 data service.

**Objective**  
The main interest is to predict increase or decrease of the index (close) in the next period.  

**Methods**  
Deep learning: neural network, RNN(LSTM) 

**Programing Language**  
Python  


**Dataset Description**  
sample_dataset.xlsx: a sample dataset with data of one minute-level time series for CSI 300 Index.


Key variables:

Var|Definition
---|---
DATETIME|Time: by minutes
open|Open price
high|high price
low|low price
close|close price
volume|Volume
amount|Transaction amount


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 11:54:18 2018

@author: MSBA 8
"""

import pandas as pd
import numpy as np
import datetime

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt

raw = pd.read_excel("~/sample_data.xlsx", na_values="N/A")
raw = raw[raw.Temp.notnull()]
raw = raw[raw.Wind_Speed_Revised.notnull()]
raw["Date"] = raw["Date"].apply(lambda x: np.asarray(datetime.datetime.strftime(x, '%Y-%m-%d').split("-")[1], dtype="float64"))
raw["Time"] = raw["Time"].apply(lambda x: np.asarray(datetime.time.strftime(x,'%H:%M:%S').split(":")[0], dtype="float64"))

#raw.head()

# create x and y
X = np.asarray(raw[["Time", "Temp", "Humidity", "Date"]])
y = np.asarray(raw["Temp"])

# normalize the dataset
scaler = MinMaxScaler()
X = scaler.fit_transform(X)
y = scaler.fit_transform(y.reshape(-1,1))

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))

# Initialising the RNN
regressor = Sequential()
regressor.add(LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 4)))
regressor.add(Dense(units = 1)) 
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the RNN to the Training set
regressor.fit(X_train, y_train, batch_size = 32, epochs = 200)

# check test set
inputs = X_test
inputs = np.reshape(inputs,(inputs.shape[0], 1, inputs.shape[1]))
predicted_temp = regressor.predict(inputs)
predicted_temp = scaler.inverse_transform(predicted_temp)

# Evaluation: on test set
mse = mean_squared_error(y_test, predicted_temp)
r2 = r2_score(y_test, predicted_temp)
mape = np.mean(np.abs(y - predicted_temp) / (y)) * 100

# Evaluation: on whole set
inputs = X
inputs = np.reshape(inputs,(inputs.shape[0], 1, inputs.shape[1]))
predicted_temp2 = regressor.predict(inputs)
predicted_temp2 = scaler.inverse_transform(predicted_temp2)

mse2 = mean_squared_error(scaler.inverse_transform(y), predicted_temp2)
r2_2 = r2_score(scaler.inverse_transform(y), predicted_temp2)
mape2 = np.mean(np.abs((scaler.inverse_transform(y) - predicted_temp2) / (scaler.inverse_transform(y)))) * 100

# Plot
x_axis = raw.index
y_line1 = scaler.inverse_transform(y)
y_line2 = predicted_temp2

plt.plot(x_axis, y_line1)
plt.plot(x_axis, y_line2, 
         color='red',  
         linewidth=1.0,  
         linestyle='--'  
        )

plt.show()
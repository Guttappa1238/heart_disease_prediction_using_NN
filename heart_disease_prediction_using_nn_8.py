# -*- coding: utf-8 -*-
"""Heart_disease_prediction_using_NN_8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fN0c4n_hii7FaOSxmOP7_5qGz6wh1js1
"""

##!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
##!unzip ngrok-stable-linux-amd64.zip



###get_ipython().system_raw('./ngrok http 6006 &')





import pandas as pd 
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import keras
from pandas.plotting import scatter_matrix

##read dataset 

data = pd.read_csv('final_raja.csv')

#print( 'Shape of DataFrame: {}'.format(data.shape))
#data.head()

data = data.apply(pd.to_numeric)
data.dtypes

#data.describe()

#data['num       ']

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
standardScaler = StandardScaler()
columns_to_scale = ['cp',
                     'chol',
                     'thal','fbs','age','sex']
data[columns_to_scale] = standardScaler.fit_transform(data[columns_to_scale])
# create X and Y datasets for training
from sklearn import model_selection

X = np.array(data.drop(['num       ','restecg','exang','thalach','ca','fbs'], axis=1))
y = np.array(data['num       '])




X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = 0.2, random_state=1)

#convert the data to categorical labels
from keras.utils.np_utils import to_categorical

Y_train = to_categorical(y_train, num_classes=None)
Y_test = to_categorical(y_test, num_classes=None)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam




# define a function to build the keras model

model = Sequential()
model.add(Dense(32, input_dim=8, kernel_initializer='random_normal', activation='relu'))
model.add(Dense(6, kernel_initializer='random_normal', activation='relu'))
model.add(Dense(3, activation='sigmoid'))

# compile model
adam = Adam(lr=0.001,decay= 1e-5)
model.compile(loss='categorical_crossentropy',
              optimizer=adam,
              metrics=['accuracy'])

 
# fit the model to the training data
model.fit(X_train, Y_train, validation_data=(X_test, Y_test),epochs=300, verbose = 10)









# generate classification report using predictions for categorical model
from sklearn.metrics import classification_report, accuracy_score

categorical_pred = np.argmax(model.predict(X_test), axis=1)

print('Results for Categorical Model')
print(accuracy_score(y_test, categorical_pred))






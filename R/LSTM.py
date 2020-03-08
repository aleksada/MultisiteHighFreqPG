#!/usr/bin/env python
# coding: utf-8

# In[3]:


# multivariate lstm example
from numpy import array
from numpy import hstack
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense


# In[2]:


import csv
with open("rain.raw.df.csv", 'r') as f:
    rain = list(csv.reader(f, delimiter=","))
import numpy as np
rain = np.array(rain[1:], dtype=np.float)


# In[4]:


# multivariate output data prep
from numpy import array
from numpy import hstack
 
# split a multivariate sequence into samples
def split_sequences(sequences, n_steps):
	X, y = list(), list()
	for i in range(len(sequences)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the dataset
		if end_ix > len(sequences)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix, :]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)
 
# define input sequence
NT=28800
in_seq1 = rain[:NT]
in_seq2 = rain[NT:(NT*2)]
#out_seq = array([in_seq1[i]+in_seq2[i] for i in range(len(in_seq1))])
in_seq3 = rain[(960*2):(960*3)]
# convert to [rows, columns] structure
in_seq1 = in_seq1.reshape((len(in_seq1), 1))
in_seq2 = in_seq2.reshape((len(in_seq2), 1))
out_seq = out_seq.reshape((len(out_seq), 1))
# horizontally stack columns
dataset = hstack((in_seq1, in_seq2, out_seq))
# choose a number of time steps
n_steps = 3
# convert into input/output
X, y = split_sequences(dataset, n_steps)
print(X.shape, y.shape)
# summarize the data
for i in range(len(X)):
	print(X[i], y[i])


# In[5]:


# split a multivariate sequence into samples
def split_sequences(sequences, n_steps):
	X, y = list(), list()
	for i in range(len(sequences)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the dataset
		if end_ix > len(sequences)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix, :]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)
 #out_seq = array([in_seq1[i]+in_seq2[i] for i in range(len(in_seq1))])

# define input sequence
NT=28800
in_seq1 = rain[:NT]
in_seq2 = rain[NT:(NT*2)]
in_seq3 = rain[(NT*2):(NT*3)]
in_seq4 = rain[:NT]
in_seq5 = rain[NT:(NT*2)]
in_seq6 = rain[(NT*2):(NT*3)]
in_seq7 = rain[:NT]
in_seq8 = rain[NT:(NT*2)]
# convert to [rows, columns] structure
in_seq1 = in_seq1.reshape((len(in_seq1), 1))
in_seq2 = in_seq2.reshape((len(in_seq2), 1))
in_seq3 = in_seq3.reshape((len(in_seq3), 1))
in_seq4 = in_seq4.reshape((len(in_seq4), 1))
in_seq5 = in_seq5.reshape((len(in_seq5), 1))
in_seq6 = in_seq6.reshape((len(in_seq6), 1))
in_seq7 = in_seq7.reshape((len(in_seq7), 1))
in_seq8 = in_seq8.reshape((len(in_seq8), 1))
# horizontally stack columns
dataset = hstack((in_seq1, in_seq2, in_seq3,in_seq4, in_seq5,in_seq6, in_seq7, in_seq8))
# choose a number of time steps
n_steps = 3
# convert into input/output
X, y = split_sequences(dataset, n_steps)
N_train = 28800-2880
N_test = 2880
X_train = X[:N_train,:,:]
X_test = X[N_train:,:,:]
y_train = y[:N_train,:]
y_test = y[N_train:,:]
# the dataset knows the number of features, e.g. 2
n_features = X.shape[2]
# define model
model = Sequential()
model.add(LSTM(100, activation='relu', return_sequences=True, input_shape=(n_steps, n_features)))
model.add(LSTM(100, activation='relu'))
model.add(Dense(n_features))
model.compile(optimizer='adam', loss='mse')
# fit model
model.fit(X_train, y_train, epochs=50, verbose=1)


# In[29]:


y1hat = np.zeros(len(X_test))
y2hat = np.zeros(len(X_test))
y3hat = np.zeros(len(X_test))
y4hat = np.zeros(len(X_test))
y5hat = np.zeros(len(X_test))
y6hat = np.zeros(len(X_test))
y7hat = np.zeros(len(X_test))
y8hat = np.zeros(len(X_test))
# demonstrate prediction
for i in range(len(X_test)):
    x_input = X_test[i]
    x_input = x_input.reshape((1, n_steps, n_features))
    y1hat[i] = model.predict(x_input, verbose=0)[0][0]
    y2hat[i] = model.predict(x_input, verbose=0)[0][1]
    y3hat[i] = model.predict(x_input, verbose=0)[0][2]
    y4hat[i] = model.predict(x_input, verbose=0)[0][3]
    y5hat[i] = model.predict(x_input, verbose=0)[0][4]
    y6hat[i] = model.predict(x_input, verbose=0)[0][5]
    y7hat[i] = model.predict(x_input, verbose=0)[0][6]
    y8hat[i] = model.predict(x_input, verbose=0)[0][7]


# In[15]:


yhat = np.zeros((len(X_test),8))
# demonstrate prediction
for i in range(len(X_test)):
    x_input = X_test[i]
    x_input = x_input.reshape((1, n_steps, n_features))
    yhat[i,] = model.predict(x_input, verbose=0)[0]


# In[16]:


yhat.shape


# In[6]:


rain_mat = rain.reshape(((NT+1)),8)
rain_test = rain_mat[(N_train+2):(NT-1)]


# In[47]:


MSE = np.square(np.subtract(yhat,rain_test)).mean() 


# In[27]:


MSE


# In[31]:


import matplotlib.pyplot as plt
plt.plot(in_seq1[N_train:])
plt.plot(y1hat)
plt.show()


# In[33]:


plt.plot(in_seq2[N_train:])
plt.plot(y2hat)
plt.show()


# In[34]:


plt.plot(in_seq3[N_train:])
plt.plot(y3hat)
plt.show()


# In[49]:


yhat.shape


# In[50]:


with open('rainest.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(yhat)


# In[ ]:





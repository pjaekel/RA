import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import datetime as dt
plt.style.use('fivethirtyeight')

data = pd.read_excel('Daten_SIX_V4.xlsx', sheet_name = 'Gesamt', index_col ='Datum')
data.columns = ['EXHA']

dataset = data.values

training_data_len = math.ceil(len(dataset) * 0.8)

# Normalize all of the data to be values between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

print(scaled_data)


# Create the scaled training data set
train_data = scaled_data[0:training_data_len, :]
# Split the data into x_train and y_train data sets
x_train = []
y_train = []
for i in range(200, len(train_data)):
    x_train.append(train_data[i - 200:i, 0])
    y_train.append(train_data[i, 0])

# Convert x_train and y_train to numpy arrays
x_train, y_train = np.array(x_train), np.array(y_train)

# Reshape the data into the shape accepted by the LSTM
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Build the LSTM network model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dense(units=25))
model.add(Dense(units=1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')


# Train the model
model.fit(x_train, y_train, batch_size=1, epochs=1)


# Test data set
test_data = scaled_data[training_data_len - 200:, :]
# Create the x_test and y_test data sets
x_test = []
y_test = dataset[training_data_len:, :]
# Get all of the rows from index 1603 to the rest and all of the columns
# In this case it's only column 'Close'), so 2003 - 1603 = 400 rows of data
for i in range(200, len(test_data)):
    x_test.append(test_data[i - 200:i, 0])

# Convert x_test to a numpy array
x_test = np.array(x_test)

# Reshape the data into the shape accepted by the LSTM
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))



# Getting the models predicted price values
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

# Undo scaling

# Calculate the value of RMSE
rmse = np.sqrt(np.mean(((predictions - y_test) ** 2)))


# Plot/Create the data for the graph
train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions data'] = predictions
# Visualize the data
plt.figure(figsize=(16, 8))
plt.title('Model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price', fontsize=18)
plt.plot(train['EXHA'])
plt.plot(valid[['EXHA', 'Predictions data']])
plt.legend(['Train', 'Val', 'Predictions data'], loc='lower right')
plt.show()



# Show the valid and predicted prices
#valid.head()



valid.to_excel(r'/Users/Pit/Documents/Uni/Master/Pro Seminar/RA/EXHA.xlsx', sheet_name='EXHA')







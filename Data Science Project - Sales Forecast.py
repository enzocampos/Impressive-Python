#!/usr/bin/env python
# coding: utf-8

# # Data Science Project - Sales Forecast
# 
# - Our challenge is to be able to predict the sales we will have in a given period based on ad spend on the 3 major networks that the Hashtag company invests in: TV, Newspaper and Radio
# 
# - Database: https://drive.google.com/drive/folders/1o2lpxoi9heyQV1hIlsHXWSfDkBPtze-V?usp=sharing

# #### Import database

# In[23]:


# Import database to Python
import pandas as pd

table = pd.read_csv("advertising.csv")
display(table)


# #### Exploratory Analysis
# - Let's try to visualize how the information of each item is distributed
# - Let's see the correlation between each of the items

# In[24]:


# Exploratory Analysis -> understand how the database is working
import seaborn as sns
import matplotlib.pyplot as plt

# Create a graph
sns.heatmap(table.corr(), annot=True, cmap = "Wistia")

# Show graph
plt.show()


# #### With this, we can start preparing the data to train the Machine Learning Model
# 
# - Separating into training data and test data

# In[25]:


#y -> who do you want to predict -> sales
#x -> the rest of the database (who will you use to make the prediction)

y = table['Vendas']
x = table[['TV', 'Radio', 'Jornal']]

from sklearn.model_selection import train_test_split

x_training, x_test, y_training, y_test = train_test_split(x, y, test_size=0.3)


# #### We have a regression problem - Let's choose the models we are going to use:
# 
# - Linear Regression
# - RandomForest (Decision Tree)

# In[26]:


# Create an AI and make predictions
from sklearn.linear_model import LinearRegression as lr
from sklearn.ensemble import RandomForestRegressor as rdr

model_linearregression = lr()
model_decisiontree = rdr()
model_linearregression.fit(x_training, y_training)
model_decisiontree.fit(x_training, y_training)


# #### AI Test and Best Model Test
# 
# - Let's use R² -> says the % that our model can explain what happens

# In[27]:


# Test to see which AI is better

prediction_linearregression = model_linearregression.predict(x_test)
prediction_decisiontree = model_decisiontree.predict(x_test)

from sklearn.metrics import r2_score

print(r2_score(y_test, prediction_linearregression))
print(r2_score(y_test, prediction_decisiontree))


# #### New Prediction

# In[28]:


new = pd.read_csv("novos.csv")
display(new)


# In[30]:


# Winning model was decision tree
preditction = model_decisiontree.predict(new)
print(preditction)


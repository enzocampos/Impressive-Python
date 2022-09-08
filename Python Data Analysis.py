#!/usr/bin/env python
# coding: utf-8

# # Python Data Analysis
# 
# ### Challenge:
# 
# You work at a telecommunications company and you have customers for several different services, among which are internet and telephone.
# 
# The problem is that, analyzing the history of customers in recent years, you can see that the company has Churn more than 26% of customers.
# 
# This represents a million dollar loss for the company.
# 
# What does the company need to do to solve this problem?
# 
# Database: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Original Kaggle Link: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[1]:


# Step 1: Import database
import pandas as pd

table = pd.read_csv("telecom_users.csv")

# Step 2: Visualize database
# Understand the available information
# So you can fix the mistakes made in the database

# axis = 0 -> row, axis = 1 -> column
table = table.drop("Unnamed: 0", axis=1)

display(table)


# In[2]:


# Step 3: Data treatment
# View and adjust any values ​​that are being recognized incorrectly
table["TotalGasto"] = pd.to_numeric(table["TotalGasto"], errors="coerce")

# Empty values
# Empty columns -> delete

# Axis = 0 -> row, axis = 1 -> column
table = table.dropna(how="all", axis=1)

# Rows with any empty values -> delete
table = table.dropna(how="any", axis=0)

display(table.info())


# In[3]:


# Step 4: Simple Analysis -> understand how the cancellations are occuring
display(table["Churn"].value_counts())
display(table["Churn"].value_counts(normalize=True).map("{:.1%}".format))


# In[5]:


# Step 5: More Complex Analysis -> Understand possible cancellations causes and solutions
import plotly.express as px

# Create a graph
# For each column in the database, create 1 graph each

for columns in table.columns:
    display(columns)
    cancel = "Churn"
    graph = px.histogram(table, x=columns, color=cancel)

    # Show graph
    graph.show()


# Escreva aqui suas conclusões:
# 
# - Familias maiores tendem a cancelar menos
#     - Podemos oferecer um 2º numero de graça para o cliente ou um plano família
#     
# - Quanto mais tempo como cliente, menor a chance de cancelar
#     - Ação de bonificar o cliente nos primeiros 12 meses
#     - Nos primeiros meses os clientes estão cancelando muito
#         - Podemos estar com um problema no inicio do período do cliente
#         - Podemos estar fazendo alguma ação de marketing muito ruim
#         
# - Temos algum problema na Fibra, os clientes estão cancelando muito
#     - Vou olhar mais a fundo a causa raiz do problema na Fibra
#     
# - Quanto menos serviço o cara tem, maior a chance do cara cancelar
#     - Podemos oferecer um serviço extra de graça
#     
# - Podemos incentivar pagamento no debito automatico ou no cartão
# 
# - Podemos oferecer incentivos para contrato anual

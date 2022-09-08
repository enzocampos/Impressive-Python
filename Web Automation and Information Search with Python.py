#!/usr/bin/env python
# coding: utf-8

# # Web Automation and Information Search with Python
# 
# #### Challenge: 
# 
# We work in an importer and the price of our products is linked to a price from:
# - Dollar
# - Euro
# - Gold
# 
# We need to automatically get the price of these 3 items from the internet and know how much we should charge for our products, considering a contribution margin that we have in our database.
# 
# Database: https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv?usp=sharing
# 
# For that, let's create a web automation:

# In[12]:


# chromedriver -> Chrome or Brave

from selenium import webdriver # create browser
from selenium.webdriver.common.by import By # locate elementes from the website
from selenium.webdriver.common.keys import Keys # allows us to use the keyboard keys

browser = webdriver.Chrome()

# Step 1: Go to Google
browser.get("https://www.google.com/")

# Step 2: Look for dollar price
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Dollar Price" + Keys.ENTER)

# Step 3: Get dollar price
dollar_price = browser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(dollar_price)

# Step 4: Get euro price
browser.get("https://www.google.com/")
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Euro Price" + Keys.ENTER)
euro_price = browser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(euro_price)

# Step 5: Get gold price
browser.get("https://www.melhorcambio.com/ouro-hoje")
gold_price = browser.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')
gold_price = gold_price.replace(",",".")

print(gold_price)


# ### Now let's update our price base with the new prices

# - Importing database

# In[13]:


# Step 6: Update my database with new prices
import pandas as pd

table = pd.read_excel("Produtos.xlsx")
display(table)


# - Updating prices and final sale price

# In[14]:


# Update price with its corresponding currency
# Dollar
# The rows where 'Moeda' = 'Dólar'
table.loc[table["Moeda"] == "Dólar", "Cotação"] = float(dollar_price)

# Euro
table.loc[table["Moeda"] == "Euro", "Cotação"] = float(euro_price)

# Gold
table.loc[table["Moeda"] == "Ouro", "Cotação"] = float(gold_price)

# Update purchase price = original price * price
table["Preço de Compra"] = table["Preço Original"]*table["Cotação"]

# Update sale price = purchase price * margin
table["Preço de Venda"] = table["Preço de Compra"]*table["Margem"]

display(table)


# ### Now let's export a new updated price base

# In[15]:


table.to_excel("Produtos Novo.xlsx", index=False)
browser.quit()


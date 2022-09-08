#!/usr/bin/env python
# coding: utf-8

# # Automation of Systems and Processes with Python
# 
# ### Challenge:
# 
# Every day, our system updates the previous day's sales.
# Your daily job, as an analyst, is to send an email to the board, as soon as you start working, with the billing and the amount of products sold the day before.
# 
# Board's e-mail: yourgmail+board@gmail.com
# Location where the system provides sales from the previous day: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing

# In[79]:


# !pip install pyautogui
# !pip install pyperclip


# In[80]:


import pyautogui
import pyperclip
import time as ti

pyautogui.PAUSE = 1

# Step 1: Get into the company's system
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

#wait for a while
ti.sleep(6)

# Step 2: Navigate the system to find the database
pyautogui.click(x=-966, y=596, clicks=2)
ti.sleep(4)

# Step 3: Export/Download database
pyautogui.click(x=-966, y=596)
pyautogui.click(x=-209, y=498)
pyautogui.click(x=-399, y=884)
ti.sleep(5)


# ### Let's now read the downloaded file to get the indicators
# 
# - Biling
# - Amount of Products

# In[81]:


# Step 4: Import the database to Python
import pandas as pd

table = pd.read_excel(r"C:\Users\enzom\Downloads\Vendas - Dez.xlsx")
display(table)


# In[82]:


# Step 5: Calculate the indicators
# billing - last column's sum
billing = table["Valor Final"].sum()

#amount of products sold - quantidade column's sum
amount = table["Quantidade"].sum()

print(amount)
print(billing)


# ### Let's send an e-mail through gmail

# In[83]:


# Step 6: Send an e-mail to the board with the report
# open e-mail (link: https://mail.google.com/mail/u/0/?hl=pt-BR#inbox)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/?hl=pt-BR#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
ti.sleep(7)

# click on `write`
pyautogui.click(x=-1231, y=501)
ti.sleep(7)

# write e-mail to the recipient
pyautogui.write("enzomontelatto1@gmail.com")
pyautogui.press("tab") # selecting the recipient
pyautogui.press("tab") # going into the `subject` area

# write subject
pyperclip.copy("Sales Report")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# write e-mail`s body section
text = f"""Dear board, good morning

Yesterday`s billing was: R${billing:,.2f}
Amount of sold products: {amount:,}
    
Kind regards.
Enzo Python"""

pyautogui.write(text)
ti.sleep(2)

# send e-mail
pyautogui.hotkey("ctrl", "enter")


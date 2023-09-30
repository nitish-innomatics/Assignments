#!/usr/bin/env python
# coding: utf-8

# **File handling + Time module**
# 
# 
# Create a Python script that simulates a simple login system. The script should prompt the user to enter their username and password. If the entered username and password match the predefined credentials, the script should log a successful login event to a log file. If the credentials do not match, it should log a failed login attempt to the log file.
# Example Output
# Assuming the predefined credentials are `username: "user123"` and `password: "pass123"`, here's an example output of the script:
#  
# 
# 
# ![image.png](attachment:image.png)

# Create any 5 of following modules
# 
# a.	Restaurant   
# 
# b.	IPL
# 
# c.	Mathematics
# 
# d.	Data Science  
# 
# e.	India
# 
# f.	Shopping mall
# 
# g.	Amazon_price   
# 
# 
# Do some research  while creating them

# ### Filehandling + Time module

# In[2]:


import time


# In[14]:


user = "user123"
passcode = "pass123"
username = input("Please enter your username: ")
if username == user:
    password = input("please enter your password: ")
    if password == passcode:
        print(f"Login successfull for {username}",time.ctime())
    else:
        print(f"Login failed for {username}",time.ctime())
else:
    print(f"Login failed for {username}",time.ctime())


# ### Creating module

# In[15]:


import india


# In[16]:


india.highestruns2k23()


# In[17]:


india.prsnt_mens_squad()


# In[18]:


india.paygrade()


# In[19]:


india.highestwickets2k23()


# In[20]:


india.teams()


# In[21]:


import IPL


# In[22]:


IPL.ipl_teams()


# In[2]:


import mathematics


# In[3]:


mathematics.addition(2,3)


# In[4]:


mathematics.subration(2,3)


# In[5]:


mathematics.multiplication(2,3)


# In[6]:


mathematics.division(2,3)


# In[7]:


mathematics.reminder(2,3)


# In[1]:


import mall


# In[2]:


mall.floors()


# In[3]:


mall.floor_no(1)


# In[4]:


mall.floor_no(2)


# In[5]:


mall.floor_no(3)


# In[6]:


mall.floor_no(4)


# In[ ]:





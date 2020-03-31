#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


# In[3]:


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


# In[4]:


def unique_list():
    tel_numbers = []
    for texts_numbers in texts:
        if texts_numbers[0] not in tel_numbers:
            tel_numbers.append(texts_numbers[0])
        if texts_numbers[1] not in tel_numbers:
            tel_numbers.append(texts_numbers[1])
    
    for calls_numbers in calls:
        if calls_numbers[0] not in tel_numbers:
            tel_numbers.append(calls_numbers[0])
        if calls_numbers[1] not in tel_numbers:
            tel_numbers.append(calls_numbers[1])

    return len(tel_numbers)



if __name__ == '__main__':
    
    print("There are",unique_list(),"different telephone numbers in the records.")

   


# In[ ]:





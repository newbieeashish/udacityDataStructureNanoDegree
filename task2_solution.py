#!/usr/bin/env python
# coding: utf-8

# In[13]:


import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


# In[14]:


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


# In[15]:


calls


# In[44]:


def totalCallTime():
    
    tel_call = dict()
    
    for callDetail in calls:
        
        
        if callDetail[0] not in tel_call:
            
            tel_call[callDetail[0]] = int(callDetail[3])
        
        else:
            
            a = int(callDetail[3])
            
            tel_call[callDetail[0]] = tel_call.get(callDetail[0])+a
            
        if callDetail[1] not in tel_call:
            tel_call[callDetail[1]] = int(callDetail[3])
        else:
            
            
            a = int(callDetail[3])
            tel_call[callDetail[1]] = tel_call.get(callDetail[1])+a
    return longestCall(tel_call)

def longestCall(tel_call):
    
    
    call_duration = 0
    tel_number = ''
    for t_num, duration in tel_call.items():
        if duration > call_duration:
            call_duration = duration
            tel_number = t_num
            
   
    return tel_number, call_duration

if __name__ == '__main__':
    x = totalCallTime()
    print(x[0],"spent the longest time,",x[1], "seconds, on the phone during September 2016.")

    


# In[ ]:





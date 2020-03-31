#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


# In[2]:


calls


# """
# TASK 4:
# The telephone company want to identify numbers that might be doing
# telephone marketing. Create a set of possible telemarketers:
# these are numbers that make outgoing calls but never send texts,
# receive texts or receive incoming calls.
# 
# Print a message:
# "These numbers could be telemarketers: "
# <list of numbers>
# The list of numbers should be print out one per line in lexicographic order with no duplicates.
# """

# In[16]:


def telemarketer():
    call_senders = set([data[0] for data in calls])
    call_receivers = set([data[1] for data in calls])
    message_senders = set([data[0] for data in texts])
    message_receivers = set([data[1] for data in texts])

    call_senders_susp = []

    for call_sender in call_senders:
        if (call_sender not in call_receivers and call_sender not in message_senders and
                call_sender not in message_receivers):
            call_senders_susp.append(call_sender)

    return sorted(call_senders_susp)

        
if __name__ == '__main__':
    print("These numbers could be telemarketers: ",telemarketer())
                
                         


# 

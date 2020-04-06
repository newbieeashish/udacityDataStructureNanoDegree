#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sort_012(input_list):
    low = 0
    mid = 0
    high = len(input_list) - 1
    # for a different type of list
    # middle value could be passed in for comparision
    mid_value = 1
    while mid <= high:
        if input_list[mid] < mid_value:
            # swap input_list[low] & input_list[mid]
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] > mid_value:
            # swap input_list[mid] & input_list[high]
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1
        else:
            mid += 1
    return input_list


# In[3]:


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)

test_case = [2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 2, 1]
test_function(test_case)

test_case = [2,2,2,2,2,2,2,2,2,2,2]
test_function(test_case)

test_case = []
test_function(test_case)


# In[ ]:





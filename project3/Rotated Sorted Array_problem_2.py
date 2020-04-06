#!/usr/bin/env python
# coding: utf-8

# In[4]:


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    # parition array if needed
    first_index = 0
    mid_index = len(input_list) // 2
    last_index = len(input_list) - 1
   

    # before we embark on a search see if we already have target data
    if number == input_list[first_index]:
        # found it in first position
        return first_index

    if number == input_list[mid_index]:
        # found it in middle position
        return mid_index

    if number == input_list[last_index]:
        # found it in last position
        return last_index

    # partition the input list and do a binary search but first
    # find the index to partition the list
    indx = find_partition_index(input_list, first_index, last_index)
    #print("partition index is", indx)
    #print("input_list", input_list)

    if indx == -1:
        # could be a sorted list, let's try a binary search
        return binary_search(input_list, number, first_index, last_index)

    # search left partition
    if number >= input_list[first_index] and number <= input_list[indx]:
        return binary_search(input_list, number, first_index, indx)

    # search right partition
    if number >= input_list[indx + 1] and number <= input_list[last_index]:
        return binary_search(input_list, number, indx + 1, last_index)



def find_partition_index(input_list, first, last):
    
    indx = -1
    while indx != ((first + last) // 2):
        indx = (first + last) // 2
        if input_list[indx] > input_list[indx + 1]:
            break
        if input_list[indx] > input_list[first]:
            first = indx
        if input_list[last] > input_list[indx]:
            last = indx
    return indx


def binary_search(input_list, number, first, last):
    # cannot find it
    if first > last:
        return -1
    middle = (first + last) // 2
    if number == input_list[middle]:
        return middle
    elif number < input_list[middle]:
        # search on the left partition
        return binary_search(input_list, number, first, middle - 1)
    else:
        # search on the right partition
        return binary_search(input_list, number, middle + 1, last)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# In[5]:


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# In[6]:


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 2, 3, 4, 6, 7, 8, 9], 6])

test_function([[6, 7, 8, 9, 10, 11, 12, 13, 14], 10])

test_function([[12, 13, 14, 15, 16, 17, 18, 10, 11], 10])
test_function([[12, 13, 14, 15, 16, 17, 18, 10, 11], 13])
test_function([[16, 11, 12, 13, 14, 15], 11])
test_function([[1,1,1,1,1,1,1,1,1,1,1,1],1])


# In[ ]:





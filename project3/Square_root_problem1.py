#!/usr/bin/env python
# coding: utf-8

# In[3]:


def sqrt(number):
    if number < 0:
        return None

    if (number == 0) or (number == 1):
        return number

    start = 0
    end = number // 2

    while start <= end:
        middle = (end + start) // 2
        middle_pow = middle * middle

        if middle_pow == number:
            return middle
        elif middle_pow < number:
            start = middle + 1
            result = middle
        else:
            end = middle - 1

    return result


# In[4]:


print('Normal Cases:')
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass \n" if (5 == sqrt(27)) else "Fail \n")

# Edge cases
print('Edge Cases:')
print("Pass" if (None == sqrt(-1)) else "Fail")
print("Pass" if (99380 == sqrt(9876543210)) else "Fail")


# In[ ]:





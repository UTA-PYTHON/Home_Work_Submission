#!/usr/bin/env python
# coding: utf-8

# ## Homework 5 - Functions

# ### 1. Write a function named add that takes two numbers as arguments and returns their sum.

# In[2]:


def add(a,b):
  return a+b

add(1,2)


# ### 2. Write a function named average that takes a list of numbers and returns their average.

# In[3]:


list1=[2,4,6,8,10,12,14,16,18,20]

average= sum(list1)/len(list1)

print(average)


# ### 3. Write a function named factorial that calculates the factorial of a given number. The factorial of a number n is the product of all positive integers less than or equal to n. For example, the factorial of 5 is 5*4*3*2*1=120

# In[1]:


n = int(input("Enter a number: "))

factorial = 1

if n >= 1:
    for i in range (1, n+1):
        factorial = (factorial*i)

print(factorial)


# ### 4. Write a function named string_length that takes a string and returns its length without using the built-in len() function.

# In[11]:


z=[1, 2, 3, 4, 5]

count=0

for i in z:
   count= (count + 1)

print(count)


# ### 5. Write a function named is_prime that checks if a given number is prime. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. The function should return True if the number is prime, otherwise False.

# In[18]:


num = 11

if num > 1:
    for i in range(2, int(num/2)+1):
        if (num%i)==0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# ### 6. Write a function named unique_elements that takes a list as an argument and returns a list of its unique elements in the order they were first encountered.

# In[4]:


numbers=[1,1,1,2,2,3,9,87,24,23,23,43,43]

check={}

for i in numbers:
  if i != check.get(i):
    print(i)
    check[i]=i
  else:
    check[i]=i


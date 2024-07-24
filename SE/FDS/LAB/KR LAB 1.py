#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = input("Enter your name: ")
print(name)


# In[13]:


count = 0
for char in name:
    count += 1
print(count)


# In[3]:


statement = input("Enter a sentence: ")
statement = statement.split(" ")
max = 0
for i in statement:
    if len(i) >= max:
        max = len(i)
        word = i
print("The word with max length is: " + word)
print("and its length is: " + str(max))


# In[17]:


# Frequency of a letter given by the user
word = input("Enter a word: ")
letter = input("Enter the letter to be checked: ")
count = 0
for i in word:
    if i == letter:
        count += 1
print("Frequency of the letter " + letter + " in the given string is: " + str(count))


# In[11]:


# Frequency of every Letter in a string
string = input("Enter a string: ")
dstring = ""
for i in string:
    if i not in dstring:
        dstring += i
for letter in dstring:
    count = 0
    for i in string:
        if i == letter:
            count += 1
    print("Frequency of the letter " + letter + " is: ", count)
    


# In[16]:


# Palindrome
string = input("Enter a word: ")
string.lower()
if  string == string[::-1]:
    print("YES. Given string is a Palindrome.")
else:
    print("NO. Given string is not a Palindrome.")


# In[18]:


string = input("Enter a string: ")
string = string.split(" ")
tocheck = input("Enter the word: ")
count = 0
for word in string:
    if word == tocheck:
        count += 1
print("Frequency of the word " + tocheck + " is " + str(count))

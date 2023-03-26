#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Palindrome

def palindrome(word):
    if(word[::-1] == word):
        print('Palindrome')
    else:
        print('Not a Palindrome')
    
def main():
    print('Enter an String')
    word = input()
    palindrome(word)
main()


# In[33]:


#Percentage Calculator

def average():
    total = 0
    for i in range(0, 6):
        print('Enter the marks of subject', i)
        mark = int(input())
        total += mark
    print('The percentage is: ', (total * 100) / 550)
    
def main():
    print('Welcome to Percentage Calculator')
    average()
    
main()   


# In[35]:


#Even Number Checker

def even(number):
    if number % 2 == 0:
        print('Number is even')
    else:
        print('Number is not even')

def main():
    print('Enter a number')
    num = int(input())
    even(num)
main()


# In[41]:


#Sentence Smasher

def sentence(length):
    sentence = []
    for i in range(0, length):
        print('Enter a word')
        sentence.append(input())
    print(*sentence, sep = ' ')
    
def main():
    print('Sentence Smasher')
    print('How many words you want to write in a sentence?')
    length = int(input())
    sentence(length)
main()


# In[51]:


#Make Negative

def make_negative(number):
    if(number == 0):
        return number
    elif(number[0] == '-'):
        return number
    else:
        return '-' + number

def main():
    print('Enter the number')
    num = input()
    negative = make_negative(num)
    print(negative)

main()


# In[55]:


#Needle in HayStack

def find_Needle(hayStack):
    for item in hayStack:
        if(item == 'Needle'):
            print('Needle Found at Posistion', hayStack.index(item))

def main():
    hayStack = ['Jay', 'Kay', 'Nay', 'Needle', 'Hay']
    find_Needle(hayStack)
    
main()


# In[ ]:





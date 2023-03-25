#!/usr/bin/env python
# coding: utf-8

# In[7]:


def playing(name):
    if name[0] == 'R' or name[0] == 'r':
        return 'Playing Bjengo'
    else:
        return 'Not Playing Bjengo'
    
def main():
    print('Enter your name')
    name = input()
    state = playing(name)
    print(state)

main()


# In[26]:


def go_for_a_walk(temprature, raining):
    if (temprature < 14) and not raining:
        print('Go for a walk')
    else:
        print('Donot go for a walk')

def main():
    print('Enter temprature')
    temprature = int(input())
    print('Is it raining?')
    raining = input()
    go_for_a_walk(temprature, raining)

main()


# In[34]:


def factorial(num):
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        print('The factorial is', factorial)

def main():
    print('Enter a number')
    num = int(input())
    factorial(num)

main()


# In[40]:


import sys
def calculator(choice, num1, num2):
    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        print(num1 / num2)
    else:
        print('Please Enter a Valid Choice')
        sys.exit()

def main():
    print('Welcome to Calculator!')
    print('Enter your choice\n1 for Add\n2 for Subtract\n3 for Multiplication\n4 for Division')
    choice = int(input())
    print('Enter number 1')
    num1 = int(input())
    print('Enter number 2')
    num2 = int(input())
    calculator(choice, num1, num2)

main()


# In[41]:


from random import randint
import sys
def number_guesser(num):
    number = randint(0,100)
    if(num == number):
        print('YOU WIN! CORRECT GUESS')
        sys.exit()
    else:
        print('INCORRECT GUESS!')
        
def main():
    count = 0
    while count < 3:
        print('Guess a number between 0 and 100')
        num = int(input())
        number_guesser(num)
        count += 1
    print('GAME OVER! YOU LOSE')
main()


# In[ ]:





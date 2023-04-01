#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Deadfish

def Deadfish(value):
    length = len(value)
    i = 0
    result = 0
    while i < length:
        if value[i] == 'i':
            result += 1
        elif value[i] == 'd':
            result -= 1
        elif value[i] == 's':
            result *= result
        elif value[i] == 'o':
            print(result)
        i += 1
    
    
def main():
    print("Welcome to DeadFish Parser!")
    print("===========================")
    print("The 4 rules are:\n1. i for increment\n2. d for decrement\n3. s for square \n4. o for output"
          "\n5. Any other character will be ignored")
    print("Enter the String for commands")
    order = input()
    Deadfish(order)
    
main()


# In[23]:


#Likes Mechanism

def likes(people):
    print(people[0], ',', people[1],' and ', len(people) - 2, ' other liked this Post!')

def main():
    people = []
    print("Welcome to Like Checker")
    print("=======================")
    print("How many People Liked a Post")
    count = int(input())
    for i in range(count):
        print("Enter the name of ", i, "person liked the post")
        people.append(input())
    likes(people)
    
main()


# In[21]:


#Triangle Checker

def validation(a, b, c):
    if a + b > c:
        print("A valid triangle can be made with these 3 sides")
    else:
        print("You cannot make a triangle with these 3 sides")

def main():
    print("Welcome to Triangle Checker")
    print("===========================")
    print("Enter the length of Side 1")
    a = int(input())
    print("Enter the length of Side 2")
    b = int(input())
    print("Enter the length of Side 3")
    c = int(input())
    validation(a,b,c)
    
main()


# In[27]:


#Opposite Number Getter

def opposite(number):
    if number[0] == '-':
        print(number[1])
    else:
        print('-',number)

def main():
    print("Welcome to Opposite Number Getter!")
    print("==================================")
    print("Enter a Number")
    num = input()
    opposite(num)

main()


# In[4]:


#Case Sensitive Repitition
def case_sensitive(value):
    length = len(value)
    i = 0
    while i < length:
        print(value[i],value[i])
        i += 1
    
def main():
    print("Welcome to case-sensitivity Repitition")
    print("===================================")
    print("Enter a String")
    value = input()
    case_sensitive(value)

main()


# In[ ]:





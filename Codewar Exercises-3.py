#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Dish Checker for Animals

def feast(animal, dish_name):
    if animal[0].upper() == dish_name[0].upper() and animal[len(animal) - 1].upper() == dish_name[len(dish_name) - 1].upper():
        print(animal, 'can bring', dish_name, 'to the feast')
    else:
        print(animal, 'cannot bring', dish_name, 'to the feast')

def main():
    print("Welcome to Animal Dish Checker")
    print("==============================")
    print("Enter the name of Animal")
    animal = input()
    print("Enter the name of Dish")
    dish = input()
    feast(animal, dish)
    
main()


# In[1]:


#Milliseconds Converter

def converter(hrs, mins, secs):
    ms_hrs = hrs * 3600000
    ms_mins = mins * 60000
    ms_secs = secs * 1000
    ms_total = ms_hrs + ms_mins + ms_secs
    print("The total Milliseconds in", hrs, "hours", mins, "minutes and", secs, "seconds are: ", ms_total, "milliseconds")

def main():
    print("Welcome to Milliseconds converter")
    print("=================================")
    print("Enter the number of hours. It should be less than 24")
    hours = int(input())
    print("Enter the number of minutes. It should be less than 60")
    mins = int(input())
    print("Enter the number of seconds. It should be less than 60")
    secs = (int(input()))
    if hours > 23 or mins > 59 or secs > 59:
        print("Invalid Entries!. Terminating........")
    else:
        converter(hours, mins, secs)

main()


# In[11]:


#Rock Paper Scissors

def rock_paper_scissors(ply_1, ply_2):
    if (ply_1.upper() == "SCISSOR") and (ply_2.upper() == "PAPER"):
        print("PLAYER 1 WON!")
    elif (ply_1.upper() == "SCISSOR") and (ply_2.upper() == "ROCK"):
        print("PLAYER 2 WON!")
    elif (ply_1.upper() == "PAPER") and (ply_2.upper() == "PAPER"):
        print("DRAW!")
    else:
        print("Terminating.......! Invalid")

def main():
    print("Welcome to ROCK PAPER SCISSORS!")
    print("===============================")
    print("Enter Player 1 input")
    ply_1 = input()
    print("Enter Player 2 input")
    ply_2 = input()
    if (ply_1.upper() == "ROCK" or ply_1.upper() ==  "PAPER" or ply_1.upper() == "SCISSOR") and (ply_2.upper() == "ROCK" or ply_2.upper() ==  "PAPER" or ply_2.upper() == "SCISSOR"):
        rock_paper_scissors(ply_1, ply_2)
    else:
        print("Invalid")
        
main()


# In[15]:


#Character Writer
def character_writer(character, times):
    for i in range(times):
        print(character)

def main():
    print("Welcome to Character Writer")
    print("===========================")
    print("Enter a character\nNOTE: IF YOU WROTE MORE THAN ONE CHARACTER ONLY THE FIRST ONE WILL BE CONSIDERED")
    ch = input()
    print("Enter how many times would you want to print it?")
    times = int(input())
    character_writer(ch[0], times)
    
main()


# In[18]:


#Volume of Cuboid

def volume(length, height, width):
    print("The volume of cuboid is ", length * height * width)
    
def main():
    print("Welcome to Volume Calculator")
    print("============================")
    print("Enter the length of cuboid")
    length = int(input())
    print("Enter the height of cuboid")
    height = int(input())
    print("Enter the width of cuboid")
    width = int(input())
    volume(length, height, width)
    
main()


# In[ ]:





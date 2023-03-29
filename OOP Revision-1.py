#!/usr/bin/env python
# coding: utf-8

# In[22]:


class cat:
    species = 'russian'
    
    #Constructor
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
#     def description(self):
#         return f"{self.name} is {self.age} years old and a {cat.species} cat"

    #Dunder Method
    def __str__(self):
        return f"{self.name} is {self.age} years old and a breed of {self.breed} cat"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
        
# mishi = cat('mishi', 4)
# print(mishi.name)
# print(mishi.age)
# mishi.description()
# mishi.species = 'german'
# print(mishi)
# mishi.speak('Meow Meow')
# wishi = cat('wishi', 3, 'british shorthair')
# print(wishi)
# print(wishi.speak('Meow'))
# jack = cat('jack', 5, 'persian')
# print(jack)
# print(jack.speak('Meow Meow'))
# neil = cat('neil', 4, 'scottish fold')
# print(neil)
# print(neil.speak('Meoooooow'))


# In[39]:


class wishi(cat):
    def speak(self, sound = 'Meow'):
        return f"{self.name} says {sound}"

wishi = wishi('wishi', 5, 'british shorthair')
# print(wishi.breed)
print(wishi.speak())


# In[40]:


class jack(cat):
    def speak(self, sound = 'Meow Meow'):
        return f"{self.name} says {sound}"

jack = jack('jack', 6, 'persian')
# print(jack.age)
# print(jack)
print(jack.speak())


# In[42]:


class neil(cat):
    def speak(self, sound = 'Meoooooow'):
        return f"{self.name} says {sound}"

neil = neil('neil', 2, 'scottish fold')
print(neil.speak())


# In[ ]:





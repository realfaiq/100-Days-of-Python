#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def speak(self):
        return f"{self.name} is saying Hi!"
    
    def __str__(self):
        return f"Hello! My name is {self.name} and my age is {self.age}. My height is {self.height}"


# In[4]:


person1 = Person('John', 23, 1.8)
print(person1)


# In[10]:


class Employee:
    comission = 0.2
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary
        
    def increment_on_salary(self):
        return self.salary * Employee.comission
    
    def __str__(self):
        return f"id-{self.id}\nName-{self.name}\nAge-{self.age}\nSalary-{self.salary}"


# In[15]:


employee1 = Employee(1, 'Arshad', 22, 15000)
employee2 = Employee(2, 'Areel', 35, 20000)
print(employee1)
print(employee2)
print("==============")
print("After Increment the Salaries are")
print(employee1.name,"\nSalary-",employee1.increment_on_salary())
print(employee2.name,"\nSalary-",employee2.increment_on_salary())


# In[22]:


class send_conversations:
    
    def send_message(self):
        self._connect()
        self._body
        self._send
        print('Sent!!!!')
        
    def _connect(self):
        pass
    
    def _body(self):
        pass
    
    def _send(self):
        pass


# In[24]:


message1 = send_conversations()
message1.send_message()


# In[2]:


class Student:
    def __init__(self, id, name, father_name, CGPA):
        self.id = id
        self.name = name
        self.father_name = father_name
        self.CGPA = CGPA
        
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    def __str__(self):
        return f"Student Id: {self.id}\nStudent Name: {self.name}\nStudent Father Name: {self.father_name}\nCGPA: {self.CGPA}"


# In[8]:


class Animal:
    def __init__(self, name, Type, legs):
        self.name = name
        self.Type = Type
        self.legs = legs
        
    def __str__(self):
        return f"Animal: {self.name}, Type: {self.Type}, Legs: {self.legs}"


# In[9]:


animal1 = Animal('Dog', 'Pet', 4)
print(animal1)


# In[10]:


class Cat(Animal):
    def __init__(self, name, Type, legs, voice):
        super().__init__(name, Type, legs)
        self.voice = voice
        
    def speak(self):
        return f"The {self.name} says {self.voice}"
    
    def __str__(self):
        return f"Cat name is {self.name} and it is of type {self.Type} and has {self.legs} legs"


# In[11]:


persian = Cat('Mishi', 'Pet', 4, 'Meow')
print(persian)
print(persian.speak())


# In[12]:


name = 'John'
print(len(name))


# In[13]:


fruits = ['apples', 'mangoes', 'bananas', 'oranges']
print(len(fruits))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[46]:


#Creating Class

class Employee:
    
    #pass For Empty class
    #Class Variables
    raise_amount = 1.04 
    num_of_employees = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + 'last' + '@company.com'
        Employee.num_of_employees += 1
    
    @property
    def email(self):
        return '{} {}@gmail.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def amount_raiser(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
    
    def __add__(self, other):
        return self.pay + other.pay

emp_1 = Employee('Faiq', 'Ahmad', 60000) #Instantiating
emp_2 = Employee('John', 'Doe', 50000)
# print(emp_1 + emp_2)
# emp_1.fullname('John Smith')
print(emp_1.fullname)

# print(Employee.num_of_employees)

# emp_1.amount_raiser(1.05)
# print(Employee.raise_amount)

# emp_str_1 = 'Lilly-Rose-50000'

# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.fullname())
# print(new_emp_1.email)

import datetime
my_date = datetime.date(2023, 3, 27)
print(Employee.is_work_day(my_date))


# In[23]:


#Inheritance

class Developer(Employee):
    #Overiding the variable
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        

dev_1 = Developer('Cersei', 'Lannister', 70000, 'Python')
dev_2 = Developer('Tywin', 'Lannister', 80000, 'Java')

print(dev_1.email)
print(dev_2.email)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.prog_lang)


# In[32]:


#Inheritance

class Manager(Employee):
    
    def __init__(self, first, last, pay, prog_lang, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employees(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_employees(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
# print(mgr_1.email)
# mgr_1.print_employees
print(isinstance(mgr_1, Employee))


# In[ ]:





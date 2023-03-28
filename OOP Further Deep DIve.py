#!/usr/bin/env python
# coding: utf-8

# In[64]:


import csv

class Item:
    #class attributes
    pay_rate = 0.8
    all = []
    
    #Constructor
    def __init__(self, name: str, price: float, quantity = 0):
        #Run validations to recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"
        
        #Assign values to self
        #instance attributes
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)
        
    @property
    #Getter
    #Read-only Attribute with property Decorator
    def name(self):
        return self.__name
    
    @name.setter
    #Setter
    #Encapsulation
    #Still if you want to change the read-only value you use the above kind of setter
    def name(self, value):
        if(len(value) >= 10):
            raise Exception('The value of name should be less than 10')
        else:
            self.__name = value
    
    def calculate_total_price(self):
        return self.price * self.quantity 
    
    def apply_discount(self):
        #The reason of using self.pay_rate is that although it is class level attribute but for item we want to override it so 
        #at first it will look at instance level as for item1 it will not find it on instance level then it will go to class 
        #level but for item2 it will find at instance level becuase we've assigned it at instance level.
#         self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('D:/100 days of Python/OOP Further/data.CSV', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    #Abstraction 
    #Because send_email has many functionality like connect, prepare_body and send which are private and not accessable
    #to user which we did by hiding the details from user by adding __ to connect, prepare_body and send from user
    def __connect(self):
        pass
    
    def __prepare_body(self):
        return f""""
            Hello Someone.
            We have {self.name} {self.quantity} times.
            Regards, Faiq.
        """
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()
        
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
#     @property
#     def read_only_name(self):
#         return 'AAA'

    
# item1 = Item('Phone', 100, 1)
# item2 = Item('Laptop', 1000, 3)
# item2.has_numpad = False
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(item2.has_numpad)
#Class level attribute can be accessed by class and as well as instances as given below
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)
#Magic attribute __dict__ that gives all the attributes belong to class or object
# print(Item.__dict__)
# print(item1.__dict__)
# item1.apply_discount()
# print(item1.price)
# item2.pay_rate = 0.6
# item2.apply_discount()
# print(item2.price)
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)
# for instance in Item.all:
#     print(instance.name)
# Item.instantiate_from_csv()
# print(Item.all)
# print(Item.is_integer(7))


# In[67]:


#Inheritance
class Phone(Item):
     #Constructor
    def __init__(self,name: str, price: float, quantity = 0, broken_phone = 0):
        
        super().__init__(
            name, price, quantity
        )
        
        #Assertions
        assert broken_phone >= 0, f"Broken Phone {broken_phone} is not greater than or equal to 0"
        
        #Assigning
        self.broken_phone = broken_phone
       

phone1 = Phone("jscPhonev10", 500, 5, 1)
# print(Item.all)
# print(Phone.all)


# In[68]:


item1 = Item('MyItem', 750)
print(item1.name)
item1.name = 'OtherName'
print(item1.name)
item1.send_email()


# In[69]:


#Polymorphism
#One single entity used for multiple objecrs
phone1.apply_discount()
print(phone1.price)


# In[ ]:





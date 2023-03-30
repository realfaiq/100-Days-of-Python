#!/usr/bin/env python
# coding: utf-8

# In[5]:


class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f"Payroll for {employee.id} - {employee.name}")
            print(f"Check amount: {employee.calculate_payroll()}")
            if employee.address:
                print('- Sent to:')
                print(employee.address)
            print('')


# In[4]:


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.address = None


# In[9]:


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
    
    def calculate_payroll(self):
        return self.weekly_salary


# In[10]:


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
        
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


# In[11]:


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission_rate):
        super().__init__(id, name, weekly_salary)
        self.commission_rate = commission_rate
        
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission_rate


# In[12]:


# salary_employee = SalaryEmployee(1, 'Faiq Ahmad', 1000)
# hourly_employee = HourlyEmployee(2, 'Sania Ashfaq', 2, 200)
# commission_employee = CommissionEmployee(3, 'Kiara Advani', 1000, 200)
# payroll_system = PayrollSystem()
# payroll_system.calculate_payroll([
#     salary_employee,
#     hourly_employee,
#     commission_employee
# ])


# In[13]:


# Duck Typing
# class DisgruntledEmployee:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name


# In[14]:


# salary_employee = SalaryEmployee(1, 'Faiq Ahmad', 1000)
# hourly_employee = HourlyEmployee(2, 'Sania Ashfaq', 2, 200)
# commission_employee = CommissionEmployee(3, 'Kiara Advani', 1000, 200)
# payroll_system = PayrollSystem()
# payroll_system.calculate_payroll([
#     salary_employee,
#     hourly_employee,
#     commission_employee
# ])


# In[15]:


class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')


# In[16]:


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')


# In[17]:


class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')


# In[18]:


class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')


# In[19]:


class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')


# In[20]:


class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)


# In[21]:


manager = Manager(1, 'Mary Poppins', 3000)
manager.address = Address(
    '121 Admin Rd', 
    'Concord', 
    'NH', 
    '03301'
)
secretary = Secretary(2, 'John Smith', 1500)
secretary.address = Address(
    '67 Paperwork Ave.', 
    'Manchester', 
    'NH', 
    '03101'
)
sales_guy = SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = FactoryWorker(2, 'Jane Doe', 40, 15)
temporary_secretary = TemporarySecretary(5, 'Robin Williams', 40, 9)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary
]
productivity_system = ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)


# In[22]:


#Composition
class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)


# In[23]:


address = Address('55 Main St.', 'Concord', 'NH', '03301')
print(address)


# In[25]:


class Component:
    def __init__(self):
        print('Component class!')
    
    def method1(self):
        print('Component\'s Method 1 has been executed')


# In[27]:


class Composite:
    def __init__(self):
        self.obj1 = Component()
        print('Composite class object has been created!')
        
    def method2(self):
        print('Composite\'s class method 2 has been executed')
        self.obj1.method1()
        
obj2 = Composite()
obj2.method2()


# In[ ]:





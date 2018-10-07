# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:44:20 2018

@author: Aakriti Adhikari
"""

class Employee:
    def __init__(self, salary, age):
        self.salary = salary
        self.age = age
    def showsalary(self):
        print(self.salary)
    def showage(self):
        print(self.age)
    def incsalary(self):
        self.salary = (self.salary*1.5)
        return self.salary
class Name:
    def __init__(self, name):
        self.name = name
  
    
class Female(Employee, Name):
    def __init__(self,  salary,  age, name, gender):
        Employee.__init__(self, salary, age)
        Name.__init__(self,name)
        self.gender = gender
      
        
s = Female(1000, 21, 'aakriti', 'F')
s.incsalary()
s.showsalary()
s.showage()
print(s.incsalary())


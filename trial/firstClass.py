# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 19:06:41 2018

@author: 583435
"""

"""
class Person:
  x = 0
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(Person.x)
"""

"""
#Ex.1:
class A:
    def __init__(self):
        print('one')

    def f(self):
        print(float())
        print(hex(-255))

class B(A):
    def __init__(self):
        print('two')

    def f(self):
        print(float())
        print(hex(-42))

x = B()
print(x.f())

y = A()
print(y.f())
"""

"""
#Ex.2:
class A:
    def __init__(self, a = 5):
        self.a = a

        def f1(self):
            self.a += 10


class B(A):
    def __init__(self, b = 0):
        A.__init__(self, 4)
        self.b = b

    def f1(self):
        self.b += 10

x = B()
x.f1()
print(x.a,'-', x.b)
"""

"""
class class1:
    a = 1

    def f1(self):
        a = 2
        class1.a += 1
        print(class1.a, end=' ')
        print(a, end=' ')

class1().f1()
class1().f1()
"""

class Animal():
    
    def __init__(self, name):
        print("Animal Class setup")
        self.name = name

    def __str__(self):
        #Take care to use return
        return (f"My Animal name is {self.name}")
        
    def who_am_i(self):
        print("This is an Animal Class")
    
    def eat(self):
        print("Love eating")
        
class Dog(Animal):
    
    def __init__(self, name):
        Animal.__init__(self, name)
        print("Dog Class created")

    def who_am_i(self):
        print("I am a Dog Class Object")  
        

myAnimal = Animal(name="Leo")
myDog= Dog(name="Jax")

myDog.who_am_i()
print(myDog)
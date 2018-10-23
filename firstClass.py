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
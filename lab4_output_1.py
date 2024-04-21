#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Animal:
    def speak(self):
        pass

    def move(self):
        pass

class Dog:
    def __init__(self):
        self.animal = Animal()

    def speak(self):
        self.animal.speak()

    def move(self):
        self.animal.move()

# Приклад використання класів
dog = Dog()
dog.speak()
dog.move()


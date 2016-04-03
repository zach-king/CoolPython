#!/usr/bin/python3

class ComplexThing:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __str__(self):
        return self.name + ": " + str(self.data)


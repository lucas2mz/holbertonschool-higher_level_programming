#!/usr/bin/python3
"""
modulo
"""


import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError) as e:
            print(f"Error deserializing object: {e}")
            return None

#!/usr/bin/python3

import pickle
from complex import ComplexThing

# Create the instance
awesome_thing = ComplexThing("awesomeness", 15)
print("Before Pickling:")
print(awesome_thing)

# Pickle the instance
pickle.dump(awesome_thing, open("complex.sav", "wb"))

# Load the instance from save
loaded = pickle.load(open("complex.sav", "rb"))

# Print the loaded instance to verify intact data
print("\nAfter Loading from Pickle: ")
print(loaded)


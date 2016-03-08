#!/usr/bin/python3
import pickle

simple_data = list(range(10))
pickle.dump(simple_data, open("simple.sav", "wb"))


import pickle

awesome_data = list(range(10))
pickle.dump(awesome_data, open("awesome_save.sav", "wb"))


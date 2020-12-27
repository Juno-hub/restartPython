import pickle

profile_file = open("profile.pickle", "wb")
profile = {"Name": "박명수", "Age": 30, "Hobby": ["Football", "Golf", "Coding"]}
print(profile)
pickle.dump(profile, profile_file)  # Save data written profile into file
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)  # Bring to data in file
print(profile)
profile_file.close()

weather = input("What's the weather like today? ")
if weather == "rainy" or weather == "snowy":
    print("Take an umbrella")
elif weather == "particlate matter":
    print("Take a mask")
else:
    print("You don't need preparation")

temp = int(input("What's the temperature outside? "))
if temp >= 30:
    print("Too hot. You would be better not to go out")
elif 10 <= temp and temp < 30:
    print("The temperature is good to go out!")
elif 0 < temp < 10:
    print("Take a outwear")
else:
    print("Too cold. You would be better not to go out")

#This is a simple program to advice users based on specific weather conditions

weather_condition = str(input("What's the weather like today? (sunny/rainy/cold):"))

if weather_condition == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_condition == "rainy":
    print(" Don't forget your umbrella and a raincoat.")
elif weather_condition == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
  wirint("Sorry, I don't have recommendations for this weather.")
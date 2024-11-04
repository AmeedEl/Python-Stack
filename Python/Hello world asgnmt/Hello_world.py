

title = "Hello World"
print(title)

name = "Ameed"
print("Hello", name)
print("Hello" + name)

age = 26 
print("Hello", age)
print("hello" * age)  # it gave an error when using (+), replaced it with (*).

fav_food1 = "Pizza"
fav_food2 = "Burger"
print("I would love to eat {} But i would rather eat {} instead.".format(fav_food1, fav_food2))
print(f"I would love to eat {fav_food1} But i would rather eat {fav_food2}.")
print("I would love to eat" , fav_food1 , "but today i feel like eating" , fav_food2)

#before i replaced the (+) with (*), the last print(didnt work, gave an error).
#it turned out that if there's an error before it won't work after for other funcs.
import random

def randInt(min=0 , max=100):
    range_size = max - min + 1
    num = int(random.random() * range_size) + min
    return num     # should print random floating number between 0 and 1

print(randInt()) # print (0 and 1 , 0 to 100)
print(randInt(max=50))    # print random int between 0 to 50
print(randInt(min=50))    # print random int between 50 to 100
print(randInt(min=50, max=500))   # print random int between 50 and 500
print("\n")

def randInt(min=0, max=100):
     return random.random()
print(randInt())
print("\n")

def randInt(min=0, max=100):
    return random.random() * 50 
print(randInt())
print("\n")

def randInt(min=0, max=100):
    return random.random() * 25 + 10    
print(randInt())
print("\n")

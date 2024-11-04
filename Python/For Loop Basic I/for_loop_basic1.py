
#count = 0
#while count <= 150:
 #   print("looping - ", count)
  #  count += 1

for i in range(0, 151):
    print(i)

#count = 5 
#while count <= 1000:
 #   print("looping - ", count)
  #  count *= 5

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0 
for i in range(0, 500001, 1):
    if i % 2 != 0:
      sum += i 
print(sum)
      
number = 2018  #starts at 2018
while number > 0:   #loop till the number is positive
    print(number)
    number -= 4  # decrement by 4 every loop

# set the variables
lowNum = 2
highNum = 27
mult = 3

for num in range(lowNum, highNum + 1):     # loop thru the range from lowwNum to highNum | we add +1 because range() excludes the endpoint, this ensures we include 9 in the loop.
    if num % mult == 0:     # check if num is a multiple of mult
        print(num)
        
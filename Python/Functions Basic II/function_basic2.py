
def countdown(num):
    return [i for i in range(num, -1, -1)]
result = countdown(5)
print(result)
print("\n")

def print_and_return(numbers):
    print(numbers[0])
    return numbers[1]
result = print_and_return([1, 2])
print("Returned:", result)
print("\n")

def first_plus_length(first):
    if not first:
        return 0
    return first[0] + len(first)
result = first_plus_length([1, 2, 3, 4, 5])
print(result)
print("\n")

def values_greater_than_second(list):
    if len(list) < 2 :   #Check if the list has less than 2 elemnts
        return False
    sec_value = list[1]    # Grabs the second value and check it. 
    new_list = [value for value in list if value > sec_value]   # creat a new list with the values greater than the sec
   
    print(len(new_list))
    return new_list       # returns the new list

result = values_greater_than_second([12, 16, 5, 10, 20, 3, 8, 22, 30, 26])  # after the sec value (16) print it and what is less than (16) forget about it.
print(result)
print("\n")


def length_and_value(size, value):
    return [value] * size           # create a list with the secified value and size

result1 = length_and_value(6, 3)
print(result1)
result2 = length_and_value(16, 1)
print(result2)
print("\n")

#1. 
def biggie_size(list):
    for i in range(len(list)):  # go thru the list and replace positive nums to (big)
        if list[i] > 0:
            list[i] = "big"
    return list

lst = biggie_size([3,-7,8,-2])
print(lst)
print("\n")

#2.
def count_positives(numbers):
    # Check if the list is not empty before replacing the last value
    if numbers:
        numbers[-1] = sum(1 for x in numbers if x > 0)
    return numbers 

print(count_positives([-1, 1, 3, 2]))  # Output: [-1, 1, 3, 3]
print(count_positives([1, 5, 3, -2, -6, 8, -2]))  # Output: [1, 5, 3, -2, -6, 8, 4]
print("\n")

#3.
def sum_total(numbers):
    # initialize a variable to keep track of the total sum
    total = 0
    # loop thru each number in the list 
    for number in numbers:
        total += number  # add the current number to the total
    return total   # return the final total

print(sum_total([2,5,9,1]))  # expected output: 17
print(sum_total([5,8,3,3,6]))  # expected output: 25
print("\n")

#4.
def average(numbers):
    # Check if the list is empty
    if len(numbers) == 0:
        return 0    # you could aslo raise an exception or return None based on requirements
    total = sum(numbers)  # calculate the sum of the numbers
    count = len(numbers)  # calculate the number of elements in the list
    avg = total / count   # calculate the average  | Perform the division
    return avg  # return the result

print(average([2,5,8,3,1]))   # expected output: 3.8
print("\n")

#5.
def length(my_list):
    # Calculate the length of the list 
    count = len(my_list)   # the built-in len() function to calcs the length.
    # Return the calcs length
    return count  # return the length of the list. 

print(length([4,3,6,1,6,9]))   # Expected output: 6 
print(length([]))    # Output: 0 
print("\n")

#6.
def minimum(num_list):
    # Check if the list is empty
    if len(num_list) == 0:
        return False     # Return False if the list is empty
    
    # find the minimum value in the list
    min_value = min(num_list)   # use the built-in min() function to find the minimum

    # return the minimum value
    return min_value   # return the minimum value found in the list

print(minimum([6,-2,-5,19,20,-1,4]))   # Expected output: -5
print(minimum([]))     # output: False 
print("\n")

#7.
def maximum(nums_list):
    # Check if the list is empty 
    if len(nums_list) == 0:
        return False      # return False if the list is empty
    
    # find the maximum value in the list
    max_value = max(nums_list)    # use the built-in max() function to find the maximum

    # return the maximum value
    return max_value   # return the maximum value found in the list

print(maximum([10, -3, 16, 20, -12, 23]))   # output: 23
print(maximum([]))       # output: False
print("\n")


#8.
def ultimate_analysis(numbers):
    if len(numbers) == 0:      # check for empty list
        return {
            'sumTotal': 0,
            'average': 0,
            'minimum': None,
            'maximum': None,
            'length': 0
        }
    
    sumTotal = sum(numbers)
    average = sumTotal / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    length = len(numbers)

    result = {
        'sumTotal': sumTotal,
        'average': average,
        'minimum': minimum,
        'maximum': maximum,
        'length': length
    }

    return result

analysis = ultimate_analysis([22, 10, 6, 3, -4])
print(analysis)
print("\n")

#9.
def reverse_list(lst):
    # left pointer starting at the beginning of the list (index 0).
    left = 0 
    right = len(lst) - 1    # right pointer starting at the end of the list (last index).

    # loop to swap elements, we want the loop continues as long as the (left) pointer is less than the (right) one. 
    # Inside the loop; 
    # - Swap the elements at the left and right indices. 
    # - Increment the left pointer (move it to the right)
    # - Decrement the right pointer (move it to the left)
# the loop condition ensures that we only swap until the pointers meet in the middle

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]     # Swap the elements
        left += 1    # move left pointer to the right
        right -= 1   # move right pointer to the left

    return lst   # Return the reversed list


the_list = [1, 2, 3, 4, 5, 6, 7, 8]   
reverse_list = reverse_list(the_list)
print(reverse_list)       # output: [8, 7, 6, 5, 4, 3, 2, 1]

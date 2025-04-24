#List of numbers that the user neeeds to add
List_of_numbers = [1,2,3,4,5,6]

# A function for adding the list of numbers
def sum_of_elements(List_of_numbers):
    total = 0

    #Using a for loop to add the numbers in a list
    for numbersx in List_of_numbers:
        total += numbersx
    return total

Result = sum_of_elements(List_of_numbers)
print("Sum of the result is: ", Result)



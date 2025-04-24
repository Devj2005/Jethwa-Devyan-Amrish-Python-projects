#To check if a number is odd or even we can use the modulo operator.
#Modulo is done to give you a remainder when you divide one number by another
#Converts the string to a  float for computations to be performed

num1 = float(input("Enter number to check if it is even or odd: "))


if num1%2 == 0:
    print("The number is an even number")
else:
    print("The number is an odd number")

#So once the you divide the number by 2 and the remainder is 0 then
#it is an even number but if there is a remainder then it is an odd number
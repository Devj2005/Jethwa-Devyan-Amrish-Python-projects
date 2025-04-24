#To check if a number is odd or even we can use the modulo operator.
#Modulo is done to give you a remainder when you divide one number by another
#Converts the string to a  float for computations to be performed

def check_oddoreven(nu):
    if nu % 2 == 0:
        print("The number given is Even")
    else:
        print("The number given is odd!")

numtest = int(input("Input any number to check if its odd or even: "))
check_oddoreven(numtest)
print()

#So once the user input the number then you divide the number by 2 and the remainder is 0 then
#it is an even number but if there is a remainder then it is an odd number
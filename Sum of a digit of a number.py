#We can input a number convert it to a string then separate each of the string then add them by looping by converting them back to an integer

def digitsummer(x)
    sumx = 0
    for digits in str(x):
        sumx += int(digits)
        return sumx


num1 = int(input("Input the number to find the sum : "))

result = digitsummer(num1)

print("Answer of sum of each digit is: ",result)

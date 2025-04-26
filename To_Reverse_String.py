#To reverse a given string to start with the last character
#We cant use the ::-1 method but we can use a loop like while

def reversal_of_string(texts):
    reversed_textsx = "" #Start with an empty string
    indexx = len(texts)-1 #because indexing start at 0 to give how many letters are in the text

    while indexx >= 0 :
        reversed_textsx = reversed_textsx + texts[indexx]
        indexx = indexx - 1

    return reversed_textsx


final = input("What is the text you want to reverse? ")
result = reversal_of_string(final)
print("Answer of reverse of string is: ",result)

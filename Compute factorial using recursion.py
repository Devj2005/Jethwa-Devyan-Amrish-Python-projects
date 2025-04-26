# Recursion is when a function keeps on calling itself until given a stopping point
# It has a base case which stops the recursion from going on inifinetely.
# It has a recursive case which keeps on calling itself(a function maybe) unti stopped by the base case

def fact_nfactorialx(num):
    if num == 0 or num == 1: #Base Case
        return 1
    else:
        return num * fact_nfactorialx(num - 1) #Recursive case




n = int(input("Input the number to find the factorial of: "))

results = fact_nfactorialx(n)

print("Answer of factorial is: ",results )

#lets say you input 5
#then it will go to the function numx = 5
# then 5 * (5-1)
# then 4 * (4-1)
# then 3 * (3-1)
# then 2 * (2-1)
# then it stops at 1

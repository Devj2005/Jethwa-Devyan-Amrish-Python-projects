#A factorial of a number means we multiply a given number form itself down to 1
#So in this case a loop can work with the initial value being 1

def fact_checkerloop(numx):
    answer = 1 # cant start with zero as any number multiplied by 0 is 0
    for i in range(1,numx+1):
        answer = answer * i
    return answer

results = int(input("Input the number you want to find the factorial on: "))
print("Answer of factorial is: ",fact_checkerloop(results))

#1*1 = 1
#1*(1+1) = 2
#2*(2+1) = 6
#6*(3+1) = 24


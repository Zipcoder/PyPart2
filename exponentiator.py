def exponetiate(num1,num2):
    return num1**num2

def raise_to_fourth_power(number):
    return exponetiate(number,4)

square = lambda x:exponetiate(x,2)
cube = lambda x:exponetiate(x,3)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))
def fact(x):
    i = 1
    for j in range(1, x+1):
        i = i * j
    return i

def func(x):
    return fact(x-1)*fact(x) / (fact(x-365) * fact(x+364))

def func1(x):
    num = 1
    for i in range(365):
        num *= (x-i)
    den = 1
    for i in range(365):
        den *= (x+i)
    return num/den

#print(func(200000))
print(func1(191677))

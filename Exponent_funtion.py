def power(n, p) :
    r = 1
    for i in range(0,p) :
        r *= n
    return r

def fact(n) : 
    r = 1
    for i in range(1,n+1):
        r *= i
    return r

n = int(input("number : "))
p = int(input("power : "))

print("power : ",power(n,p))
print("factorial : ",fact(n))


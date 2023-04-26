#   by pasing value
def add_two(n_1,n_2) :
    print("\n Result : ", n_1 + n_2)

n_1 = int(input("\n Enter no. 1 : "))
n_2 = int(input("\n Enter no. 2 : "))
add_two(n_1,n_2)

# without passing value
def add_two() :
    n_1 = int(input("\n Enter no. 1 : "))
    n_2 = int(input("\n Enter no. 2 : "))
    print("\n Result : ", n_1 + n_2)

add_two()

#   by taking value in the function from the main programm and returnnig the result to the main program
#   here the main programm means , where/when the function was called
 
def add_two(n_1,n_2) :
    sum = n_1 + n_2
    return sum

n_1 = int(input("\n Enter no. 1 : "))
n_2 = int(input("\n Enter no. 2 : "))
print("result : ",add_two(n_1,n_2))
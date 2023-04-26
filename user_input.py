name = input("enter your name : ")
age = int(input("enter your age : "))
print("hii"+ name +"of age", age )


name = input("enter your name : ")
age = int(input("enter your age : "))
print("hii", name ,"of age", age )

#plus is used for concatination of strings and coma can be used for both strings and integeres ,
#so better use coma(,)

#simple calculator

num_1 = float(input("enter no. 1 : "))
num_2 = float(input("enter no. 2 : "))
i = int(input("\n 1 to add\n 2 to subtrat\n 3 to multiply\n 4 to divide \n ENTER YOUR CHOICE : "))
if i == 1 :
    print(num_1 + num_2)
elif i == 2 :
    print(num_1 - num_2)
elif i == 3 :
    print(num_1 * num_2)
else :
    print(num_1 / num_2)
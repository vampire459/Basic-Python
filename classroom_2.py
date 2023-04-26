st_n = int(input("enter no. of students data you want to input : "))
for i in range(st_n) :
    name = input("enter name of student : ")
    class_name = name
    name = type(class_name, (), {})
    obj = name
    obj.age = int(input("enter age of "))

name = input("who's data you want to know : ")
purpose = input("what you want to know abt him or her : ")
print(obj.age)

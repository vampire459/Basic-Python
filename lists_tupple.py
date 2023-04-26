#list
family = ["Arnab","Anuj","Aparna","Alok"] #it's a list , which can contain integer, float, char, string --->> anything 
#which can be named anything not only list
print(family)
print(family[2])
print(family[-2])   #printing the list as per the index
print(family[1:])   #this will print after the index number
print(family[:2])   #this will print upto the index number
family[0] ="Babai"
print(family)
friends = ["Arnab","Sonu","Sibhashis"]
print(friends)
numbers = [1,2,3,4,5]
family.extend(friends)
family.extend(numbers)  #extend helps to extend the list
print(family)
family.append("Ronit")  #inserts at the last position
print(family)
family.insert(1,"dustu")    #inserts at the provided position
family.remove("Ronit")  #delets the provided item 
family.remove(1)
print(family)
family.pop()    #pops the last value like stack
print(family)
family.clear()  #delets every item of the list
family.sort()   #sorts in asscending order
print(family)

#user defined list
listi = []
n = int(input("Array Limit : "))
for i in range(n):
    print("enter value ",i+1," : ")
    listi.append(int(input()))
for i in listi :
    print(i)


#tupple

tupple = (6,9)
print(tupple)

#   tupples are basically denoted by 1st brackets() & lists are denoted by 3rd brackets[]
#   tupples cannot be modified but lists can be modified like deleting , adding or changing

list_of_tupples = [("Arnab","Jana"),(23,45),(5,3)]  #it's a list of tupples , where the values of the list cannot be moddified
print(list_of_tupples)

#   2D List

list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(list[1][1])

for i in list :
    for j in i :
        print(j)

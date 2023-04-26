word = input("enter a word : ")
rslt = ""
for l in word :
    if l in "AEIOUaeiou" :
        rslt += "g" 
    else :
        rslt += l
print(rslt)

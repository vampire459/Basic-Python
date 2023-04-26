#while loop

l = int(input("starting : "))
u = int(input("ending : "))
while l <= u :
    print("\n",l)
    l += 1

#secret word

sec_word = input("Enter the secret word : ")
count = 1
limit = int(input("Enter the limit : "))
while count <= limit :
    word = input("Enter the word : ")
    if sec_word == word :
        count = limit + 1
        print("correct")
    else :
        count += 1
        print("incorret")


# for loop

for x in "Arnab Jana" :
    print(x)

for x in range(10) :
    print(x)

for x in range(69,70) :
    print(x)

friends = ["joy","siva","pro"]
for x in range(len(friends)) :
    print(friends[x])


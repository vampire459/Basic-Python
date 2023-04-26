from Question import Question_class

questions_list = [
    Question_class("\nWhat colour are the apples ? \n a. Red/Green\n b. Orange\n c. Yellow","a"),
    Question_class("\nWhat colour are the Bananas ? \n a. Teal\n b. Magenta\n c. Yellow","c"),
    Question_class("\nWhat colour are the Strawberries ? \n a. Red\n b. Blue\n c. Yellow","a"),
]

def test(questions_list) : 
    for q in questions_list :
        print(q.promt)
        answer = input("\n Enter youtr option : ")
        if answer == q.answer :
            print("\n RIGHT")
        else :
            print("\n WRONG")

test(questions_list)
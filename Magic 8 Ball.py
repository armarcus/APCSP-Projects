#Ava Marcus
#1/22/24
#Magic 8 Ball

import random

print("Welcome to Magic 8 Ball.")
responses = ["Yes", "No", "Certainly", "Definitely not", "Possibly", "Very doubtful", "Without a doubt", "Outlook is good", "Outlook not so good", "Cannot be determined right now"]

#Allows user to ask a question with input and recieve a random response from the Magic 8 Ball.
#while loop allows user to either ask another question or end the program.
while True:
    ask = input("Please ask a yes/no question for the ball to answer.")
    if ask.endswith("?"):
        print(random.choice(responses))
        choice = input("Would you like to ask another question?")
        if (choice == "No") or (choice == "no") or (choice == "N") or (choice == "n"):
            print("Program ended.")
            break
    else:
        print("Question mark not entered. Please re-enter the question.")
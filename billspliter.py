import random

num_people = input("Enter the number of friends joining (including you):\n")
number = int(num_people)
users_dictionary = {}

if number > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(number):
        name = input()
        users_dictionary.update({name: 0})
    
    print("Enter the total bill value:")
    amount= input()
    bill = int(amount)
    for_each = int(bill) / number
    for key,value  in users_dictionary.items():
        users_dictionary[key] = round(for_each, 2)

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No: \n")
    choice = input()
    if choice == "Yes":
        lucky_one = random.choice(list(users_dictionary))
        print(lucky_one, " is the lucky one!")

        for_remaining = bill / (number - 1)

        for key,value  in users_dictionary.items():
            if key == lucky_one:
                users_dictionary[lucky_one] = 0
            else:
                users_dictionary[key] = round(for_remaining, 2)
        print(users_dictionary)
    else:
        print("No one is going to be lucky")
        print(users_dictionary)
else:
    print("No one is joining for the party")
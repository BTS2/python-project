def welcome():
    return input("""Welcome tophonebook
                    at hand:
                    1. All contacts
                    2. New contact
                    3. Show contact
                    4. Edit contact
                    5. Delete contact
                    6. Exit
                    Your choice (1, 2, 3, 4, 5, 6)>: """)

contact = []


def main():

   While True:

    choice = welcome()
    choice = int(choice if choice.isdigit() else 0)

    if choice == '0':
        print('continue')
    elif choice == '1':
        print(choice)
    elif choice == '2':
        print(choice)
    elif choice == '3':    
        print(choice)
    elif choice == '4':    
        print(choice)
    elif choice == '5':    
        print(choice)
    elif choice == '6':
        print("Thank you for using the phonebook")  
    elif choice == '_':    
        print("incorrect choice")


if __main__ == "__main__":
    main()
    print(type([])) #<class "list">
    print

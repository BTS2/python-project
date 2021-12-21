from datetime import datetime

contacts = [
    ['cat', '2222222', '2021-12-16'],
    ['tom', '1111111', '2021-12-16'],
    ['dog', '3333333', '2021-12-16'],
]

choices = [
    '',
    'All contacts', 
    'New contact',
    'Show contact',
    'Edit contact',
    'Delete contact',
    'Exit'
]

  
def welcome():
    prompt = """Welcome to Phone Book
        At hand:\n"""
    tmp = "Your choice("
    
    for index, item in enumerate(choices):
        if index == 0: continue
        tmp += f'{index},'
        
        prompt += f'{" "*12} {index}. {item}\n' 
        
    return prompt + f'{" "*12} {tmp[:-1]} Or q)>:' 
                    
fields = ('name', 'phone')

def add_contact():
    contact = []
    for item in fields:
        field = input(f'Enter {item}: ')
        contact.append(field)
    return contact


def find_contact():
    name = input(f'Enter {fields[0]} for search: ')
    for contact in contacts: 
        print(contact)
        for item in contact:
            if name in item:
                return item         
    return None
        
def edit_contact(i):
    contact = []
    for item in fields:
        field = input(f'Enter {item}: ')
        contact.append(field)
    contact.append(datetime.today().strftime("%Y-%m-%d"))
    contacts[i] = contact
    
def main():
        
    while True:
        choice = input(welcome())
        if choice == 'q': break
        choice = int(choice if choice.isdigit() else 0)
        
        if choice == 0:
            continue
        elif choice == 1:
            print (contacts)
        elif choice == 2:
            contacts.append(add_contact())
        elif choice == 3:
            res = find_contact()
            contact = res if res else 'Nothing found'
            print(contact)
        elif choice == 4:
            res = find_contact()
            index = contacts.index(res)
            edit_contact(index)
            print(contacts) 
        elif choice == 5:
            res = find_contact()
            index = contacts.index(res)
            del contacts[index]
            print(contacts)
        elif choice == 6:
            print('Thanks for using Phone Book')
            break
        elif choice == _:
            print('Incorrect choice')
                    
if __name__ == '__main__':
    main()
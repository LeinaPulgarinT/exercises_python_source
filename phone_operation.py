import pickle
from datetime import date, datetime
from operator import itemgetter, attrgetter

class Contact:
    def __init__(self, id, name, lastname, age, number, email):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.number = number
        self.email = email
        self.creation_date = datetime.now()
        print(f"A new contact has been created with the name {self.name}")

    def __str__(self):
        return f'''\nDocument: {self.id}\nName: {self.name}
        \nLastname: {self.lastname}\nAge: {self.age}\nCellphone: {self.number}
        \nEmail: {self.email}\nCreation date: {self.creation_date}\n'''
class Phone():

    contacts = []

    def __init__(self):
        """Class initializer method."""
        contact_list = open('contacts_file', 'ab+')
        contact_list.seek(0)
        try:
            self.contacts = pickle.load(contact_list)
            print(f'{len(self.contacts)} contact were loaded')
        except:
            print("There aren't contacts")
        finally:
            contact_list.close()
            del(contact_list)

    def create_contact(self, new_contact):
        """Create contact and save it."""
        self.contacts.append(new_contact)
        print(f'Do you want to add {new_contact.name}to contacts list?')
        res = int(input('Enter 1 to add it or 2 to not add it: '))
        if res == 1:
            self.save_contact_at_archive()
            print(f"""
            {new_contact.name} has been added to your contact list
            """)
    
    def save_contact_at_archive(self):
        """Save contact at contacts file."""
        contact_list = open('contacts_file', 'wb')
        order = sorted(self.contacts, key=attrgetter('creation_date'))
        self.contacts = order
        pickle.dump(self.contacts, contact_list)
        contact_list.close()
        del(contact_list)
        del(order)

    def contact_check(self, name):
        archive = open('contacts_file', 'rb')
        my_contacts = pickle.load(archive)
        for i in my_contacts:
            if i.name == name:
                return  True
        else: 
            return False
        archive.close()
        del(archive)


    def update_contact(self, name_contact, data, update_inf):
        """Update a contact."""
        archive = open('contacts_file', 'rb+')
        for i in self.contacts:
            if i.name == name_contact:
                if data == 1:
                    i.id = update_inf
                elif data == 2:
                    i.name = update_inf
                elif data == 3:
                    i.lastname = update_inf
                elif data == 4:
                    i.age = update_inf
                elif data == 5:
                    i.number = update_inf
                elif data == 6:
                    i.email = update_inf
            else:
                continue

        pickle.dump(self.contacts, archive)  
        archive.close()
        del(archive)
        print()
        print()
        print('--- U P D A T E D   C O N T A C T ----')
        self.show_contacts()

    def hide_contact(self, hide_name):
        """Hide a contact."""
        hide = open('contacts_file', 'rb')
        my_contacts = pickle.load(hide)
        for i in my_contacts:
            if i.name == hide_name:
                continue
            else:
                yield i
        hide.close()
        del(hide)

    def show_contacts(self):
        """Show contacts list."""
        show = open('contacts_file', 'rb')
        my_contacts = pickle.load(show)
        print()
        print('---------  contact list -------')
        print()
        for i in my_contacts:
            print(i)
        show.close()
        del(show)


def show_list_contacts():
    """Show contacts list at funtion main."""
    my_schedule = Phone()
    my_schedule.show_contacts()

def create():
    """Ask for the information to create a contact."""
    print('To create a contact enter the fallowing data: ')
    document = input('Identificación: ')
    while document.isdigit() == False:
        print('Invalid entry, try again')
        document = input('Document: ')
    name = input('Name: ')
    lastname = input('Lastname: ')
    age = input('Age: ')
    phone_number = input('Phone number: ')
    try:
        int(phone_number)
    except ValueError:
        while not phone_number.isdigit():
            print('Invalid entry, enter a numeric value')
            phone_number = input('Phone number: ')
    res =False
    while res == False:
        email = input('Email: ')
        if '@' in email and email.count('@') == 1 and '.' in email:
            res = True
        else:
            print('Invalid email, try again')
            res = False

    my_schedule = Phone()
    new_contact = Contact(document, name, lastname, \
    age, phone_number, email)
    my_schedule.create_contact(new_contact)

def update():
    """Update a contact."""
    my_schedule = Phone()
    print()
    print('Select a contact to update: ')
    print()
    my_schedule.show_contacts()
    print()
    name_contact = input('Write the name of the contact: ')
    if my_schedule.contact_check(name_contact) == True:
        print("""
            Enter a number to update: 
            1 -> Document, 2 -> Name, 3 -> Lastname, 4 -> Age, 
            5 -> Cellphone, 6 -> Email 
            """)
        dato = int(input('Option: '))
        if dato >= 1 and dato <= 6:
            info = input('Enter the new data to update: ')
            my_schedule.update_contact(name_contact, dato, info)
        else:
            print(f"Option {dato}, is invalid, try again")
            update()
    else:
        print(f'{name_contact} does NOT EXIST in the contact list')

def hide():
    """Hide the selected contact."""
    my_schedule = Phone()
    print()
    print('---- Choose a contact, you want hide  ----')
    print()
    my_schedule.show_contacts()
    print()
    name_hide  = input('Contact name: ')
    if my_schedule.contact_check(name_hide) == True:
        for i in  my_schedule.hide_contact(name_hide):
            print(i)
        print()
        print('----- H I D D E N   C O N T A C T  ----')
    else:
        print(f'{name_hide} does NOT EXIST in the contact list')


def principal():
    """Program to create, save, update or hide a contact."""
    option = 1
    while option == 1:
        print()
        print('----------- C H O O S E   A N   O P T I O N  -------')
        print('''
        Enter:    1 to VIEW contact list, 
                  2 to CREATE contact,
                  3 to UPDATE contact, 
                  4 to HIDE contact,
                  5 to EXIT
        ''')
        option = int(input('Enter the option: '))
        if option == 1:
            try:
                show_list_contacts()
            except EOFError:
                print("There aren't contacts in the list, create a contact")
        elif option == 2:
            create()
            principal()
        elif option == 3:
            try:
                update()
                principal()
            except EOFError:
                print("There aren't contacts, create one to update")
                create()
                principal()
        elif option == 4:
            try:
                hide()
                principal()
            except EOFError:
                print("There aren't contacts, create one to hide")
                create()
                principal()
        elif option == 5:
            print('--------   Out the program   --------')
            break
        else:
            print(f'La opcion {option} Not Exist, enter a valid option')
            principal()
principal()



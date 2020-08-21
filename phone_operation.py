import pickle
from datetime import date, datetime
from operator import itemgetter, attrgetter

class Contact:
    def __init__(self, id, name, lastname, age, number, email, creation_date):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.number = number
        self.email = email
        self.creation_date = creation_date
        print(f'Se ha creado un nuevo contacto con el nombre {self.name}')

    def __str__(self):
        return f'''{self.creation_date}, {self.name}, {self.lastname}, \
            {self.age}, {self.number}, {self.email}, {self.id} \n '''


class Phone():

    contacts = []

    def __init__(self):
        """Class initializer method."""
        contact_list = open('contacts_file', 'ab+')
        contact_list.seek(0)
        try:
            self.contacts = pickle.load(contact_list)
            print(f'Se cargaron {len(self.contacts)} contactos')
        except:
            print('No hay contactos')
        finally:
            contact_list.close()
            del(contact_list)

    def create_contact(self, new_contact):
        """Create contact and save it."""
        self.contacts.append(new_contact)
        print(f'¿Deseas agregar {new_contact.name} a lista de contactos?')
        res = int(input('ingresa 1 para agregarlo o 2 para no agregarlo: '))
        if res == 1:
            self.save_contact_at_archive()
            print(f"""
            {new_contact.name} ha sido agregador(a) a tu lista de contactos
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

    def update_contact(self, name_contact, data, update_inf):
        """Update a contact."""
        archive = open('contacts_file', 'rb+')
        for i in self.contacts:
            if i.name == name_contact:
                if data == 1:
                    i.id = update_inf
                    break
                elif data == 2:
                    i.name = update_inf
                    break
                elif data == 3:
                    i.lastname = update_inf
                    break
                elif data == 4:
                    i.age = update_inf
                    break
                elif data == 5:
                    i.number = update_inf
                    break
                elif data == 6:
                    i.email = update_inf
                    break
            else:
                continue
        pickle.dump(self.contacts, archive)  
        archive.close()
        del(archive)
        print()
        print()
        print('--- C O N T A C T O  A C T U A L I Z A D O ----')
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
        print('---------  Lista de contactos -------')
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
    print('Para crear un contacto ingresa los siguientes datos: ')
    document = input('Identificación: ')
    while document.isdigit() == False:
        print('Entrada no válida, intenta nuevamente')
        document = input('Identificación: ')
    name = input('Nombre: ')
    lastname = input('Apellido: ')
    age = input('Edad: ')
    try:
        phone_number = int(input('Número tel: '))
    except ValueError:
        print('Entrada invalida, ingrese valor numerico')

    email = input('email: ')
    year = int(input('Año actual: '))
    month = int(input('Mes actual: '))
    day = int(input('Dia actual: '))
    creation_date = date(year, month, day)
    my_schedule = Phone()
    new_contact = Contact(document, name, lastname, \
    age, phone_number, email, creation_date)
    my_schedule.create_contact(new_contact)

def update():
    """Update a contact."""
    my_schedule = Phone()
    print()
    print('Selecciona un contacto para actualizar: ')
    print()
    my_schedule.show_contacts()
    print()
    name_contact = input('Escribe el nombre del contacto: ')
    print("""
        Ingrese un numero que corresponda con la opcion a actualizar: 
        1 -> cedula, 2 -> nombre, 3 -> apellido, 4 -> edad, 
        5 -> número, 6 -> email 
        """)
    dato = int(input('Opción: '))
    info = input('Ingresa la info que deseas actualizar: ')
    my_schedule.update_contact(name_contact, dato, info)

def hide():
    """Hide the selected contact."""
    my_schedule = Phone()
    print()
    print('---- Escoje en la lista el contacto que quieres ocultar ----')
    print()
    my_schedule.show_contacts()
    print()
    name_hide  = input('Nombre contacto: ')
    for i in  my_schedule.hide_contact(name_hide):
        print(i)
    print()
    print('----- C O N T A C T O  O C U L T A D O  ----')


def principal():
    """Program to create, save, update or hide a contact."""
    option = 1
    while option == 1:
        print()
        print('----------- E L I J E   U N A   O P C I O N   -------')
        print('''
        Ingresar: 1 para VER lista de contactos, 
                  2 para CREAR contacto,
                  3 para ACTUALIZAR contacto, 
                  4 para OCULTAR contacto,
                  5 para SALIR
        ''')
        option = int(input('Ingresa la opcion: '))
        if option == 1:
            try:
                show_list_contacts()
            except EOFError:
                print('No contactos en la lista, crea un contacto')
        elif option == 2:
            create()
            principal()
        elif option == 3:
            try:
                update()
                principal()
            except EOFError:
                print('No contactos, para actualizar crea uno')
                create()
                principal()
        elif option == 4:
            try:
                hide()
                principal()
            except EOFError:
                print('No contactos, para ocultar un contacto créalo')
                create()
                principal()
        elif option == 5:
            print('--------   Saliste del programa   --------')
            break
principal()





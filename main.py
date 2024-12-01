import csv
from addcontact import add_contact
from viewcontact import view_contact
from removecontact import remove_contact
from searchcontect import search_contact

def contact_book_management_system():
    print('============================== Welcome To Contact Book Management System ==============================')
    while True:
        print('-------------------------- Options -----------------------')
        print('1. Add Contacts')
        print('2. View Contacts')
        print('3. Search Contact')
        print('4. Remove Contacts')
        print('5. Exit')
        print('-------------------------- Options -----------------------')

        option=input('# Please select your option: ')
        if option == '1':   #for add contact
            print("   ")
            add_contact()
            print("   ")
        elif option == '2':   #for view contact
            print("   ")
            view_contact()
            print("   ")
        elif option == '3':   #for remove contact
            print("   ")
            search_contact()
            print("   ")
        elif option == '4':   #for search contact
            print("   ")
            remove_contact()
            print("   ")
        elif option == '5':   #for exit contact
            print("   ")
            print("============================== Thank You For Using Contact Book Management System ==============================")
            print("   ")
            break
        else:
            print("   ")
            print('*********** Please select a valid option ***********')

contact_book_management_system()
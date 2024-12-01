import csv
from createcsvfile import create_csv_file

def add_contact():
    count = 0
    contact_list = []
    try:
        name = str(input('# Please enter Name: '))
        email = str(input('# Please enter Email: '))
        phone = int(input('# Please enter Phone: '))
        address = str(input('# Please enter Address: '))
        if phone:
            try:
                duplicate_found = False
                with open('contact_book.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        count += 1
                        if row[3] == phone:
                            duplicate_found = True
                            print("   ")
                            print(phone)
                            print('*********** Number already exists ***********')
                            add_contact()
                if not duplicate_found:
                    contact_list.append([count+1, name, email, phone, address])
                    with open('contact_book.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        for i in contact_list:
                            writer.writerow(i)
                        print("   ")
                        print(count+1, name, email, phone, address)
                        print('*********** Successfully added ***********')
            except FileNotFoundError:
                create_csv_file()
        else:
            print('*********** Number And Phone can not be empty ***********')
            add_contact()
    except:
        # print(error)
        print("*********** Phone number must be integer ***********")
        add_contact()











# add_contact()




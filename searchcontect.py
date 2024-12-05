import csv
from createcsvfile import create_csv_file
from viewcontact import view_contact

def search_contact():
    try:
        view_contact()
        print("   ")
        search_param=input("Give a Number to search.....: ")
        with open('contact_book.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[3] == search_param:
                    print('*********** Search Result ***********')
                    print(row[0], ".",  row[1], row[2],row[3], row[4])

    except FileNotFoundError:
        create_csv_file()

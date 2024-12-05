import csv
from createcsvfile import create_csv_file

def view_contact():
    try:

        with open('contact_book.csv', 'r') as file:
            reader = csv.reader(file)
            print('***************** Contact List *****************')
            for row in reader:
                print(row[0], ".",  row[1],'|', row[2],'|',row[3],'|', row[4])
    except FileNotFoundError:
        create_csv_file()


# view_contact()


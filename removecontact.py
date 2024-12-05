import csv
from viewcontact import view_contact

def remove_contact():
    view_contact()
    print("   ")
    contact_to_remove = input('Enter the number of the contact to remove (Example: 1): ')
    updated_rows = []
    with open('contact_book.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != contact_to_remove:
                updated_rows.append(row)
                print(row[0],".",row[1],row[2],row[3],row[4])

    with open('contact_book.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)
        print("   ")
        print("*********** Remove Successfully  ***********")


# remove_contact()
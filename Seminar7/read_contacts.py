import csv

def read_contact(unit=1, file_name='phonebook.csv'):
    with open(file_name, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if unit == 2:
                item = ', '.join(row)
                print(item)
            if unit == 1:
                for item in row:
                    print(item)
                print()
        print('End of contacts\n' + '-' * 20)
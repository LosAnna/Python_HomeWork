def save_to_csv(contact_info):
    with open('phonebook.csv', 'a') as bd:
        for i in range(len(contact_info)):
            if i != len(contact_info) - 1:
                bd.write(f'{contact_info[i]};')
            else:
                bd.write(f'{contact_info[i]}')
        bd.write('\n')
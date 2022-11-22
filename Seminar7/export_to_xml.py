import csv

def csv_to_data(file_name='phonebook.csv'):
    with open(file_name, newline='') as f:
        csv_f = csv.reader(f, delimiter=';')
        data = []
        for row in csv_f:
            data.append(row)
    return data


def export_to_xml(data=csv_to_data()):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<contacts>\n'
    for row in data:
        last_name, name, phone, info = row
        xml += '    <contact>\n'
        xml += '        <Last_name>{}</Last_name>\n' \
            .format(last_name)
        xml += '        <Name>{}</Name>\n' \
            .format(name)
        xml += '        <Phone_number>{}</Phone_number>\n' \
            .format(phone)
        xml += '        <Info>{}</Info>\n' \
            .format(info)
        xml += '    </contact>\n'
    xml += '</contacts>'
    with open('phonebook.xml', 'w') as page:
        page.write(xml)
    return data

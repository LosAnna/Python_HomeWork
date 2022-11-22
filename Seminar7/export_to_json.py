import json
from export_to_xml import csv_to_data


def export_to_json(data=csv_to_data()):
    jsn = '[\n'
    for row in data:
        last_name, name, phone, info = row
        jsn += '    {\n'
        jsn += '        "Last_name": {},\n' \
            .format(last_name)
        jsn += '        "Name": {},\n' \
            .format(name)
        jsn += '        "Phone_number": {},\n' \
            .format(phone)
        jsn += '        "Info": {},\n' \
            .format(info)
        jsn += '    },\n'
    jsn += ']'
    with open('phonebook.json', 'w') as page:
        json.dump(jsn, page)
    # print(jsn)
    return data

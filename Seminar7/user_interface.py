from read_contacts import read_contact
from save_contacts import save_to_csv
from export_to_xml import export_to_xml
from export_to_json import export_to_json

def start():
    print('Выберите необходимую операцию:', '1 - ввод данных в формате "Фамилия, Имя, телефон, описание"',
          '2 - вывод данных в требуемом формате', '3 - экспорт данных в файл', '4 - завершение работы с модулем',
          sep='\n')

    operation_select = int(input())
    if operation_select == 1:
        soname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        phone_number = input('Введите номер телефона: ')
        description = input('Введите описание: ')
        new_list = [soname, name, phone_number, description]
        save_to_csv(new_list)
        start()
        return new_list
    elif operation_select == 2:
        print('Выберите формат отображения данных:', '1 - построчно', '2 - в одну строку', sep='\n')
        num = int(input())
        if num == 1 or num == 2:
            read_contact(num)
        start()
    elif operation_select == 3:
        print('Выберите формат экспорта данных:', '1 - xml', '2 - json', sep='\n')
        num = int(input())
        if num == 1:
            export_to_xml()
            print('Данные успешно экспортированы в формате xml!\n' + '-' * 20)
        elif num == 2:
            export_to_json()
            print('Данные успешно экспортированы в формате json!\n' + '-' * 20)
        else:
            print('Неверный ввод! Повторите!\n' + '-' * 20)
            start()
        start()
    elif operation_select == 4:
        print('Всего хорошего!\n' + '-' * 20)
        exit(0)
    else:
        print('Неверный ввод! Повторите!\n' + '-' * 20)
        start()

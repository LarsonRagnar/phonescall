
# def open_file_read(path):
#     with open(path,'r') as file:
#         main_list=(file.readlines())
#         main_list_str=[x.rstrip().split(":") for x in main_list]
#     return main_list_str
# print(open_file_read('phones.txt'))
#
# def open_file_write(path,list_file):
#     with open(path,'w') as file:
#         file.writelines([':'.join(x)+'\n' for x in list_file])
# list_for_look=[['sergei', 'lohov', '123456'], ['anton', 'palchikov', '456789'], ['jora', 'objora', '789654']]
# def look_list (list_for_look):
#     print([' '.join(x) for x in list_for_look], end= '\n')
# look_list(list_for_look)
def open_file_read(path):
    with open(path, 'r') as file:
        main_list = [x.rstrip().split(":") for x in file.readlines()]
    return main_list

def open_file_write(path, list_file):
    with open(path, 'w') as file:
        file.writelines([':'.join(x)+'\n' for x in list_file])

def add_data(data, list_file):
    list_file.append(data)

def update_data(name, surname, phone, list_file):
    for i, item in enumerate(list_file):
        if item[0] == name and item[1] == surname:
            list_file[i][2] = phone
            break

def delete_data(name, surname, list_file):
    for i, item in enumerate(list_file):
        if item[0] == name and item[1] == surname:
            del list_file[i]
            break

def look_list(list_file):
    print([' '.join(x) for x in list_file], end='\n')

path = 'phones.txt'

main_list = open_file_read(path)
look_list(main_list)

def get_input():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    return [name, surname, phone]

path = 'phones.txt'
main_list = open_file_read(path)
look_list(main_list)

# Добавление новых данных через ввод пользователем
new_data = get_input()
add_data(new_data, main_list)
look_list(main_list)
open_file_write(path, main_list)
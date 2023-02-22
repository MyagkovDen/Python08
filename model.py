def input_text():
    with open('file.txt', 'a') as data:
        surname = data.write(input('Введите фамилию: '))
        data.write(' ')
        name = data.write(input('Введите имя: '))
        data.write(' ')
        fathername = data.write(input('Введите отчество: '))
        data.write(' ')
        phoneNumber = data.write(input('Введите номер телефона: '))
        data.write('\n')
        
def print_text():
    path = 'file.txt'
    data = open('file.txt', 'r')
    for line in data:
        print(line)
    data.close()

def check_text(userInfo):
    path = 'file.txt'
    data = open('file.txt', 'r')
    flag = False
    for line in data.readlines():
        if userInfo in line:
            print(line)
            flag = True
            break
    if flag == False: print('Запись с этим атрибутом отсутствует в справочнике!')
    data.close()

def change_text():
    with open('file.txt', 'r') as data:
        temp = data.read()
    temp = temp.replace(input('Введите запись, которую нужно заменить: '), input('Введите новую редакцию записи: '))
    with open('file.txt', 'w') as data:
        data.write(temp)

def delete_text():
    with open('file.txt', 'r') as data:
        temp = data.read()
    temp = temp.replace(input('Введите запись, которую нужно удалить: '), '')
    with open('file.txt', 'w') as data:
        data.write(temp)
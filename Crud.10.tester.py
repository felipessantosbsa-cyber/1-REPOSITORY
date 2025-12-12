# CRUD TESTER
import json
ARQUIVO = 'numeros_e_nomes.json'

def menu_simple():
    print("---- MENU ----\n" + '--' * 15)
    print("> [1] add\n" + '--' * 15)
    print("> [2] uptade\n" + '--' * 15)
    print("> [3] search\n" + '--' * 15)
    print("> [4] delete\n" + '--' * 15)
    print("> [5] view\n" + '--' * 15)
    print("> [6] exit\n" + '--' * 15)

def add_names_numbers():
    try:
        name = input("what name?: ")
        number = input("what number?: ")
    except ValueError:
        print("write soemthing numbers please")
        return None

    dict_name_numbers = {
        'name': name,
        'number': number
    }
    return dict_name_numbers

def uptade_name_numbers():
    try:
        uptade_number = input("whose people do you want to uptade?: ")
        for unics in number_name_list:
            if unics['name'] == uptade_number:
                while True:
                    new_number = int(input("what is new number?: "))
                    unics['number'] = new_number
                    print(f"you uptade a {uptade_number}")
                    return
        print("no have this people sorry")
    except ValueError:
        print("write soemthing numbers please")
        return None

def delete_name_numbers():

    try:
        delete_name = input("whose people do you want to delete?: ")
        delete_found = False
        for unics in number_name_list:
            if unics['name'] == delete_name:
                number_name_list.remove(unics)
                print(f"you delete {number_name_list}")
                delete_found = True
        if not delete_found:
            print("no have this people")
    except ValueError:
        print("write soemthing numbers please")
        return None

number_name_list = []
power = True

try:
    with open(ARQUIVO, 'r') as names_numbers:
        number_name_list = json.load(names_numbers)
except FileNotFoundError:
    number_name_list = []
    print("not found file")

while power:
    menu_simple()
    try:
        menu_choose = int(input("what opition do you choose: "))
    except ValueError:
        print("write something numbers please")

    if menu_choose == 1:
        dict_name_numbers = add_names_numbers()
        number_name_list.append(dict_name_numbers)
    elif menu_choose == 2:
        uptade_name_numbers()
    elif menu_choose == 3:
        try:
            people_name = input("where you search name?: ")
        except ValueError:
            print("write soemthing numbers please")
        name_found = False
        for unics in number_name_list:
            if unics['name'] == people_name:
                print(f"name: {unics['name']}   |   number: {unics['number']}")
                name_found = True
        if not name_found:
            print("no have this people")
    elif menu_choose == 4:
        delete_name_numbers()
    elif menu_choose == 5:
        for unics in number_name_list:
            print(f"name: {unics['name']}   |   number: {unics['number']}")
    elif menu_choose == 6:
        with open(ARQUIVO, 'w') as names_numbers:
            json.dump(number_name_list, names_numbers, indent=4)
        power = False
print("thank you for using my programm")







        
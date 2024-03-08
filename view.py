from controller import CategoriaController
from dal import CategoriaDal
while True:
    decision = input('1 - Register \n2 - List\n3 - Exit\nType the desired option: ')
    if decision == '1':
        name = input('Name: ')
        description = input('Description: ')
        CategoriaController().register(name, description)
        break
        
    if decision == '2':
        for category in CategoriaDal.read():
            print(category)
        break
    
    if decision == '3':
        break
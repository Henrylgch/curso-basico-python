# def imprimir_mensaje():
#     print('hola mundo')
#     print('estoy aprendiendo python')

# imprimir_mensaje()

def conversacion(mensaje):
    print('Hola')
    print('Como estas?')
    print(mensaje)
    print('Adios')

2
option = input('Elige una opcion (1, 2, 3?: ')
if option == '1':
    conversacion('elegiste la opcion 1')
elif option == '2':
    conversacion('elegiste la opcion 2')
elif option == '3':
    conversacion('elegiste la opcion 3')
else:
    print('elige una opcion correcta')
menu = """
Bienvenido al conversor de monedas, que deseas cambiar?

1 - Pesos Chilenos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """
option = int(input(menu))

def conversor(tipo_pesos, valor_dolar):
    pesos = float(input('Cuantos pesos ' + tipo_pesos + ' tienes?: '))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')

if option == 1:
    tipo_pesos = 'Chilenos'
    valor_dolar = 793
    conversor(tipo_pesos, valor_dolar)

    
elif option == 2:
    tipo_pesos = 'Argentinos'
    valor_dolar = 110
    conversor(tipo_pesos, valor_dolar)

elif option == 3:
    tipo_pesos = 'Mexicanos'
    valor_dolar = 20
    conversor(tipo_pesos, valor_dolar)

else:
    print('tu opcion no es valida')




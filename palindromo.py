def run():
    palabra = input('ingresa tu palabra, y te dire si es palindromo o no: ')
    palabra = palabra.lower().replace(' ','')

    if palabra == palabra[::-1]:
        print('tu palabra es un palindromo')
    else:
        print('tu palabra no es un palindromo')


if __name__ == '__main__':
    run()

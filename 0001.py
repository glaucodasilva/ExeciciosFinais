#** Próximo Número Primo ** - Peça ao programa para encontrar números primos até que o usuário opte por parar de perguntar pelo próximo.

def proxprimo():
    x = 0
    listaprimo = [2]
    while True:
        primo = True
        x += 1
        if x > 2:
            for p in listaprimo:
                if x % p == 0:
                    primo = False
                    break
        if primo:
            if x > 2:
                listaprimo.append(x)
            yield x

def main():
    g = proxprimo()
    while True:
        novo = ''
        print(next(g))
        while novo.upper() != 'S' and novo.upper() != 'N':
            print('Deseja gerar um novo número prímo? Digite S para Sim e N para Não.')
            novo = input()
        if novo.upper() == 'N':
            break

if __name__ == '__main__':
   main()

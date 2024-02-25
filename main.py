def inserir_numeros():
    controle = True
    numeros = []
    while(controle):
        print('insira um número ou digite s para sair: \n')
        num = input()
        if num == 's' or num == 'S':
            return numeros
        numeros.append(int(num))
        

def soma():
    numeros = inserir_numeros()
    soma = 0
    for i in numeros:
        soma += i
    print(f"\nResultado: {soma}")
        
def subtrai():
    numeros = inserir_numeros()
    pass
def multiplica():
    numeros = inserir_numeros()
    pass
def divide():
    numeros = inserir_numeros()
    pass



def menu() -> int:
    print("escolha uma opção: \n1-somar: \n2-subtrair: \n3-multiplicar: \n4-dividir: \nopção:")
    escolha:int = int(input())
    return escolha

def main():
    escolha:int = menu()
    match escolha:
        case 1:
            soma()
        case 2:
            subtrai()
        case 3:
            multiplica()
        case 4:
            divide()

if __name__ == "__main__":
    main()
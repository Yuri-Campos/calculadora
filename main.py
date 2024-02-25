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
    soma = numeros[0]
    for i in numeros[1:]:
        soma += i
    print(f"\nResultado: {soma}")
        
def subtrai():
    numeros = inserir_numeros()
    sub = numeros[0]
    for i in numeros[1:]:
        sub -= i
    print(f"\nResultado: {sub}")
        
def multiplica():
    numeros = inserir_numeros()
    multiplica = numeros[0]
    for i in numeros[1:]:
        multiplica *= i
    print(f"\nResultado: {multiplica}")
        
def divide():
    numeros = inserir_numeros()
    divide = numeros[0]
    for i in numeros[1:]:
        divide /= i
    print(f"\nResultado: {divide}")
        



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
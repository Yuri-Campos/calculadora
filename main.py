def menu() -> int:
    print("escolha uma opção: \n1-somar: \n2-subtrair: \n3-multiplicar: \n4-dividir: \nopção:")
    escolha = int(input())
    return escolha

def main():
    menu()

if __name__ == "__main__":
    main()
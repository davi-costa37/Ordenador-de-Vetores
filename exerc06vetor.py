def fcarrega():
    vetor = []
    print("Digite 20 números inteiros:")
    for i in range(20):
        num = int(input(f"vetor[{i}]: "))
        vetor.append(num)
    return vetor

def fclassifica(vetor):
    n = len(vetor)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vetor[i] > vetor[j]:
                vetor[i], vetor[j] = vetor[j], vetor[i]
    return vetor

def pmostrar(vetor):
    print("Vetor:")
    for i, v in enumerate(vetor):
        print(f"vetor[{i}] = {v}")

def main():
    vetor = [0] * 20
    opc = 0

    while opc != 9:
        print("\nMENU")
        print("1 - Carregar vetor")
        print("2 - Classificar vetor")
        print("3 - Mostrar vetor")
        print("9 - Encerrar")
        try:
            opc = int(input("Digite uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue

        if opc == 1:
            vetor = fcarrega()
        elif opc == 2:
            vetor = fclassifica(vetor)
            print("Vetor classificado com sucesso.")
        elif opc == 3:
            pmostrar(vetor)
        elif opc == 9:
            print("Encerrando o programa.")
        else:
            print("Opção inválida.")

# Executa o programa
main()

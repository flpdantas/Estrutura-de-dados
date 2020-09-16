def main():
    n1 = float(input('Digite a nota da 1ª avaliação:'))
    while n1 > 10 or n1 < 0:
        print("Nota inválida!")
        n1 = float(input('Digite a nota da 1ª avaliação:'))

    n2 = float(input('Digite a nota da 2ª avaliação:'))
    while n2 > 10 or n2 < 0:
        print("Nota inválida")
        n2 = float(input('Digite a nota da 2ª avaliação:'))

    print("A media do aluno é:",(n1+n2)/2)

main()
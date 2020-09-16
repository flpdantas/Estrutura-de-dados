def main():
    n1 = int(input('Digite o valor 1:'))
    n2 = int(input('Digite o valor 2:'))

    while n2 == 0:
        print('Digite um valor diferente de ZERO!')
        n2 = int(input('Digite o valor 2:'))

    print('A divisão é:', n1/n2)
main()
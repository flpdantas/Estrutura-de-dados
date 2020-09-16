def main():
    n1 = int(input('Digite o valor 1:'))
    n2 = int(input('Digite o valor 2:'))



    for i in range(0,1):
        if n2 == 0:
             print('Digite um valor diferente de ZERO!')
             n2 = int(input('Digite o valor 2:'))
             print('A divisão é:', n1/n2)


        elif n2 != 0:
            print('A divisão é:', n1/n2)
main()
def main():
    print('-----NOTAS DO ALUNO-----')
    aluno= int(input('Digite o código do aluno:'))

    n1 = float(input('Digite o valor da primeira nota:'))
    n2 = float(input('Digite o valor da segunda nota:'))
    n3 = float(input("Digite o valor da terceira nota:"))

    p1 = 4
    p2 = 3
    p3 = 3

    media1 = ((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3)
    media2 = ((n1*p2) + (n2*p1) + (n3*p3)) /(p1+p2+p3)
    media3 = ((n1*p2) + (n2*p3) + (n3*p1)) / (p1+p2+p3)

    print('Aluno:', aluno)
    print('1ª Nota:', n1)
    print('2ª Nota:', n2)
    print('3ª Nota:', n3)

    if n1>n2 or n1>n3:
        print('A média ponderada do aluno',aluno,"é:", media1 )
    elif n2>n1 or n2>n3:
        print('A média ponderada do aluno', aluno, "é:", media2)
    elif n3>n1 or n3>n2:
        print('A média ponderada do aluno', aluno, "é:", media3)
    print('------------------------')
main()
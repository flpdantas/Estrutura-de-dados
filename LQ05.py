def main():
    print('-----MERCADO-----')
    qtd= int(input("Qual a quantidade de maçãs que desejas:"))
    print("A quantidade de maçãs compradas:", qtd)

    if qtd>= 12:
        print("O valor da compra foi:", qtd*1,"Reais")
    elif qtd< 12:
        print("O valor da compra foi:", qtd*1.3,"Reais")
    print('-----------------')
main()
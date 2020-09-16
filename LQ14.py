def main():
    conjunto = []
    for i in range(0, 10):
        numero = int(input("Número " + str (i + 1) + ":"))
        conjunto.append(numero)
    print(conjunto)

    soma = sum(conjunto)
    print('A soma de todos os número é:', soma)



main()
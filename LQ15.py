def main():
    estoque = int(input("Digite a quantidade total de mercadorias:"))

    for i in range (0, estoque):
        mercadoria = float(input("Qual o valor da mercadoria" + str ( 1 + i ) + " : "))
    print("O valor em estoque é:", estoque*mercadoria)
    print("O valor médio das mercadorias é:", estoque*mercadoria/estoque)

main()
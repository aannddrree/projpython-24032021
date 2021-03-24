nomes = []

while True:
    opcao = input("Opção - 1-Inserir / 2-Listar / 0 - Sair: ")
    if (opcao == "1"):
        nome = input("qual é o seu nome: ")
        nomes.append(nome)
    if (opcao == "2"):
        for d in nomes:
            print(d)
    if (opcao == "0"):
        break

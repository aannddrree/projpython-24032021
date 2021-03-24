arq = open('C:\\python\\aula4\\arqTeste2.txt', 'r')
linhas = arq.readlines()

nomes = []

for linha in linhas:
    nomes.append(linha[2:9])

nomesOrdenados = sorted(nomes)

#IMPRIMINDO OS DADOS
for nome in nomesOrdenados:
    print(nome)

arq.close()

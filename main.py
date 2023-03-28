#Armazena na variavel file1 o conteúdo do arquivo estoqueB+.txt
with open("C:\\Users\\Usefr\\Desktop\\Estoque\\estoqueB+.txt") as t1:
    file1 = t1.readlines()
#Armazena na variavel file2 o conteúdo do arquivo IDsFC.txt
with open("C:\\Users\\Usefr\\Desktop\\Estoque\\IDsFC.txt") as t2:
    file2 = t2.readlines()
#Cria o arquivo estoquefinal.txt
with open("C:\\Users\\Usefr\\Desktop\\Estoque\\estoquefinal.txt", "w+") as t3:
        pass


#Cria um dicionário que armazena como keys as ids e como value as quantidades do arquivo estoqueB+.txt
dict1 = {}
for line in file1:
    dict1[line[0:7].strip()] = line[7:].strip()

#Cria uma lista que armazena as ids do arquivo IDsFC.txt
l1 = []
for line in file2:
    l1.append(line.strip())

#Olha se a quantidade de IDs entre os arquivos é diferente
if len(dict1) != len(l1):
    print(f"A quantidade de IDs entre os arquivos é diferente: Arquivo 1: {dict1} != Arquivo 2: {l1}" )


#Olha se cada id da lista l1 corresponde com um id no dicionario dict1, se existir, é colocado no arquivo
#estoquefinal.txt a quantidade correspondente ao id, se não existir, o id será mostrado no terminal
for id in l1:
    if id in dict1:
        with open("C:\\Users\\Usefr\\Desktop\\Estoque\\estoquefinal.txt", "a") as t3:
            t3.write(dict1[id])
            t3.write("\n")
    else:
        print("Produto NÃO encontrado: ", id)
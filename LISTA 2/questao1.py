import time

def counting_sort_de_strings(lista, tamanho, col, base, tamanho_max):

    saida   = [0]*tamanho
    contagem    = [0]*(base + 1)
    min_base = ord('a')-1 

    for item in lista: 
        letra = ord(item[col])-min_base if col<len(item) else 0
        contagem[letra]+=1
        

    for i in range(len(contagem)-1): 
        contagem[i + 1] += contagem[i]

    for item in reversed(lista):
        letra = ord(item[col])-min_base if col<len(item) else 0
        saida[contagem[letra]-1] = item
        contagem[letra]-=1
    return saida

def radix_sort_letters(lista, max_col = None):

    if not max_col:
        max_col = len(max(lista, key=len)) # caso radix_sort seja chamado sem max_col a maior string da lista passada no primeiro argumento será pêga


    for col in range(max_col - 1, -1, -1):  # vai diminuindo o valor de max_col em -1 a cada nova iteração da função
        lista = counting_sort_de_strings(lista, len(lista), col, 26, max_col)
    return lista

#main
with open('dna_seq.txt') as initialfile:
    
    contents = initialfile.read()
    dna = (list(contents.replace('\n','').split(' '))) #pega os dados do arquivo .txt separados por ' ' e os transforma em uma lista
    time.sleep(2)
    print("\nagora demonstrando no console a sequencia ordenada!\n")
    time.sleep(1)
    print(radix_sort_letters(dna))
    print("\nagora, criando arquivo com a sequencia ordenada!\n")
    time.sleep(2)
    finalfile = open("dna_seq_ordenado.txt","w+")
    finalfile.write(str(radix_sort_letters(dna)))
    time.sleep(1)
    print("aquivo criado!!")
    finalfile.close()
initialfile.close()
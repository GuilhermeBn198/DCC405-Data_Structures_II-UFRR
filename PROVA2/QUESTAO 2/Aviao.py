#recolhe os inputs
brabo = input('').split(' ')

#separa os inputs
n_fileiras = int(brabo[0]) #numero de fileiras no aviao
n_posi = int(brabo[1]) #quantidade de posições em cada fileira
n_primefileira = int(brabo[2]) #numero da primeira fileira da classe economica
n_posiembarque = int(brabo[3]) #numero da posição de embarque de Su Zuki


#faz um dicionario para as letras das fileiras do aviao
aviao = {
			1: "A", 2: "B",
			3: "C", 4: "D",
			5: "E", 6: "F",
			7: "G", 8: "H",
   			9: "I", 10: "J",
			11: "K", 12: "L",
			13: "M", 14: "N",
			15: "O", 16: "P",
			17: "Q", 18: "R",
			19: "S", 20: "T",
			21: "U", 22: "V",
			23: "W", 24: "X",
			25: "Y", 26: "Z",
		}

# se o nuemro de fileiras menos a primeira fileira da classe economica vezes o numero de posições 
# por fileira for maior que o numero da posição de embarque de Su Zuki então:
if (n_fileiras - n_primefileira)*n_posi > n_posiembarque:
    print((n_posiembarque // n_posi + n_primefileira),aviao.get(n_posiembarque % n_posi))
    # o algoritmo printa a posição de embarque dividida pelo numero de posições por fileira mais o numero da primeira fileira
    # da classe economica arredondado pra cima e a gnt pega no dicionario a posição de embarque mod numero de posições de cada fileira
else:
    print("PROXIMO VOO")
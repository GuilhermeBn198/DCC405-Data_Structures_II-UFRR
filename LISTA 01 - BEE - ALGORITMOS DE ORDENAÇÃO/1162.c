#include <stdio.h>

unsigned ordena(unsigned int vetor[], unsigned int size){
	unsigned i, j, counter = 0, aux;
  
	while (size != 0){
		for (i = 0, j = 1; i < size; i++, j++){
			if (vetor[i] > vetor[j]){	//verifica se o primeiro vagao eh maior q o segundo
				counter++; //aumenta o contador
				aux = vetor[i]; 
				vetor[i] = vetor[j];
				vetor[j] = aux;  //com ajuda da variavel auxiliar fazemos a troca dos vagoes
			}
		}
		size--;
	}
	return counter;
}
int main (){

	unsigned int casos, tamTrem; //cria-se variaveis p definir numero de casos e tamanho dos trems
	unsigned int i; //uma variavel auxiliar

	scanf("%u", &casos); //scanneia os casos

	while (casos != 0){ //enquanto os casos forem maiores que 1
		scanf("%u", &tamTrem); //scaneia o tamanho do trem
		unsigned int vagoes[tamTrem];

		for (i = 0; i < tamTrem; i++) {
			scanf("%d", &vagoes[i]);
		}
		printf("Optimal train swapping takes %u swaps.\n", ordena(vagoes, tamTrem));
		casos--;
	}
return (0);
}

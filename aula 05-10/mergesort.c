//exemplo de ordenação por intercalação multithread
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

void merge (int arr[], int inicio, int meio, int fim) {
	//Cria dois vetores L <- A[inicio..meio] e R <- A[meio+1..fim]
	int lsize = meio - inicio + 1;
	int rsize = fim - meio;
	int L[lsize], R[rsize];
	for (int i = 0; i<lsize; i++) L[i] = arr[inicio+1];
	for(int j = 0; j<rsize; j++) R[j] = arr[meio+1+j];

	//mantém o indice corrente of sub-arrays and main array
	int topo_left, topo_right, k;
	topo_left = 0;
	topo_right = 0;
	k = inicio;

	//até chegarmos a qualquer extremidade de L ou R, escolha o maior entre os elementos L e R e coloque-os na posição correta em arr[inicio..fim]
	while( topo_left < lsize && topo_right < rsize){
		if( L[topo_left] <= R[topo_right]) {
			arr[k] = L[topo_left];
			topo_left++;
		} else {
			arr[k] = R[topo_right];
			topo_right++;
		}
		k++;
	}

	// Quanto ficarmos sem elementos erm L ou R, pegue os elementos restantes e coloque em 
}

void mergesort(int arr[], int inicio, int fim) {
	if (inicio < fim) {
		int meio = inicio + (fim - inicio / 2); //evita overflow
		mergesort(arr, inicio, fim);
		mergesort(arr, meio + 1, fim);
		merge(arr, inicio, meio, fim);
	}
}
void printArray(int arr[], int size) {
	for (int i = 0; i<size;i++) printf("%d ", arr[i]);
	puts (" ");
}

int main(){
	int arr[] = {30, 8, 7, 55, 19, 4};
	int size = sizeof(arr) / sizeof(arr[0]);
	
	printf("%d\n", sizeof(arr));
	printf("%d\n", sizeof(arr[0]));

	printArray(arr, size);
	mergesort(arr, 0, size);
	printArray(arr, size);
  
	return 0;
}
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
	int NC, Npessoas, altura, primeiro, alturas[231];

	printf("digite o numero de casos:\n");
	scanf("%d", &NC);

	for (int k = 0; k < NC; ++k){ 
		memset(alturas, 0, sizeof(alturas));
		
		printf("digite agora o numero de pessoas da cidade\n");
		scanf("%d", &Npessoas);//para identificar a quantidade de pessoas

		printf("agora digite a altura das pessoas");
        for (int i = 0; i < Npessoas; ++i){
            scanf("%d", &altura); //para identificar a altura das pessoas
            alturas[altura]++;
        }

        primeiro = 1;
		
        for (int i = 20; i < 231; ++i){
            for (int j = 0; j < alturas[i]; ++j){ //printa em ordem crescente de altura
                if (primeiro) {
                    primeiro = 0;
				}
                else{
                    printf(" ");
				}
                printf("%d", i);
            }
        }
        printf("\n");
    }
    return 0;
}
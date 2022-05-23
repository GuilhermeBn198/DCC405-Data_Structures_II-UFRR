#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>

#define TAM 21
// ------------------ definição da estrutura!------------------
typedef struct Aluno{
	char nome[TAM];
}Aluno;

int comp(const void *p1,const void *p2){
	Aluno *i=(Aluno *)p1,*j=(Aluno *)p2;
	return strcmp(i->nome,j->nome);
}

int main(int argc,char *argv[]){

	int x,n,k;
	scanf("%d %d",&n,&k);
	Aluno Aluno[n];
	for (x=0;x<=n;x++){
	scanf(" %s",Aluno[x].nome);
	}
	qsort(Aluno,n,sizeof(Aluno[0]),comp);
	// puts("-------------------");
	// puts("o vencedor é:\n");
	printf("%s\n",Aluno[k-1].nome);
	return 0;
}
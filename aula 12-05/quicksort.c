//é o algoritmo de ordenação interna mais rápido que se conhece para uma ampla
//variedade de situações, provavelmente mais utilizado e tem a ideia básica de
//dividir o problema de ordenar um conjunto com n itens em dois problemas
//menores. Os problemas menores são ordenados independentemente e ao final eles
//são combinados para produzir a solução final.

#include <stdio.h>

void quicksort(int number[25], int first, int last) {
  int i, j, pivot, temp;

  if (first < last) {
    pivot = first;
    i = first;
    j = last;

    while (i < j) {
      while (number[i] <= number[pivot] && i < last) i++;
      	while (number[j] > number[pivot]) j--;
      	if (i < j) {
        temp = number[i];
        number[i] = number[j];
        number[j] = temp;
      }
    }

    temp = number[pivot];
    number[pivot] = number[j];
    number[j] = temp;
    quicksort(number, first, j - 1);
    quicksort(number, j + 1, last);
  }
}

int main() {
  int i, count, number[25];
  printf("Enter some elements (Max. - 25): ");
  scanf("%d", &count);
  printf("Enter %d elements: ", count);

  for (i = 0; i < count; i++) scanf("%d", &number[i]);
  quicksort(number, 0, count - 1);
  printf("The Sorted Order is: ");
  for (i = 0; i < count; i++) printf(" %d", number[i]);
  return 0;
}
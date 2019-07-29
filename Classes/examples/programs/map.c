#include <stdio.h> 

int square(int a){
	return a*a; 
} 
int* map(int* list, int size, int (* func)(int)){
	for (int i = 0; i < size; i++){
		*(list + i) = func(*(list + i));  
	} 
} 
int main(int argc, char* argv[]){ 
	int arr1[10]; 
 
	for (int i = 0; i < 10; i++){
		arr1[i] = i; 
	}
        map(arr1, 10, &square); 
	
	for (int i = 0; i < 10; i++){
		printf("%d\n", *(arr1 + i)); 
	} 	
	
	
	return 0; 
} 

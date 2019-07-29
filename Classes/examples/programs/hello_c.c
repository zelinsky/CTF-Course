#include <stdio.h> 
int add(int a, int b){
	return a + b; 
} 
int multiply(int a, int b){
	return a*b; 
} 
int main(){ 
	int sum = 0; 
	for (int i = 0; i < 10; i++){
		if (i % 2){
			sum = multiply(sum, i); 
		} 
		else{
			sum = add(sum, i); 
		} 
	} 

	printf("%d\n", sum); 
} 

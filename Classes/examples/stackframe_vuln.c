#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
void win(){
	printf("how'd you get here\n"); 
} 
int myFunc(int a, int b, int c){
	int d; 
	int e; 
	int f; 
	char buf[15]; 
	d = 5; 
	e = 6; 
	f = 7;
	fgets(buf, 0x150, stdin);
        printf("%s\n", buf);
	
	if(f == 0xdeadbeef){
		win();
	} 
	printf("a = %d, b = %d, c = %d\n", a, b, c); 
        printf("d = %d; e = %d; f = %d\n", d, e, f); 	

	return (a*d + b*e + c*f); 
} 
int main(){
	myFunc(1, 2, 3); 
} 

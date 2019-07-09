#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define FLAGSIZE_MAX 64

char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig) {
  fprintf(stderr, "%s\n", flag);
  fflush(stderr);
  exit(1);
}

void vuln(char *input){
  char buf[16];
  strcpy(buf, input);
}

int main(int argc, char **argv){

  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Could not open flag file.\n");
    exit(0);
  }
  fgets(flag,FLAGSIZE_MAX,f);                                                                                              
  signal(SIGSEGV, sigsegv_handler);                                                                                        


  if (argc > 1) {                                                                                                          
    vuln(argv[1]);                                                                                                         
    printf("Thanks! Received: %s\n", argv[1]);                                                                               
  }                                                                                                                        
  else                                                                                                                     
    printf("This program takes 1 argument.\n");                                                                            
  return 0;                                                                                                                
}      

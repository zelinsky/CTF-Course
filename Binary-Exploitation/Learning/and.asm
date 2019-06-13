section .text
   global _start            ;must be declared for using gcc
	
_start:                     ;tell linker entry point
   mov   ax,   8h           ;getting 8 in the ax 
   and   ax, 1              ;and ax with 1
   jz    evnn
   mov   eax, 4             ;system call number (sys_write)
   mov   ebx, 1             ;file descriptor (stdout)
   mov   ecx, odd_msg       ;message to write
   mov   edx, len2          ;length of message
   int   0x80               ;call kernel
   jmp   outprog

evnn:   
  
   mov   ah,  09h
   mov   eax, 4             ;system call number (sys_write)
   mov   ebx, 1             ;file descriptor (stdout)
   mov   ecx, even_msg      ;message to write
   mov   edx, len1          ;length of message
   int   0x80               ;call kernel

outprog:

   mov   eax,1              ;system call number (sys_exit)
   int   0x80               ;call kernel

section   .data
even_msg  db  'Even Number!' ;message showing even number
len1  equ  $ - even_msg 
   
odd_msg db  'Odd Number!'    ;message showing odd number
len2  equ  $ - odd_msg

all: asm

asm: x86_template.o 
	ld -m elf_i386 -s -o asm x86_template.o 

x86_template.o: x86_template.asm 
	nasm -f elf x86_template.asm 


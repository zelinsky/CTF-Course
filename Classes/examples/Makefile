all: asm 

asm: template.o 
	ld -m elf_i386 -s -o asm template.o 

template.o: x86_template.asm 
	nasm -f elf x86_template.asm 


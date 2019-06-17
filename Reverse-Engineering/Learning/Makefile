SRCS = $(wildcard *.asm)
OBJS = $(SRCS:.asm=.o)
EXECS = $(SRCS:.asm=)

all: $(EXECS)

$(OBJS): %.o: %.asm
	nasm -f elf $^

$(EXECS): %: %.o
	ld -m elf_i386 -s -o $@ $^

clean:
	rm -rf $(EXECS) $(OBJS) *~


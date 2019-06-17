# A byte

## Description

Just one byte makes all the difference.

[a-byte](a-byte)

## Solution

Looking the assembly code by r2. In the main function, the input message is checked whether the strlen is 0x23=35.

```
0x0000078e      e85dfeffff     call sym.imp.strlen         ; size_t strlen(const char *s)
0x00000793      8945c4         mov dword [local_3ch], eax
0x00000796      837dc423       cmp dword [local_3ch], 0x23 ; '#'
```

Next, it is xored by 1 per byte

```
.---> 0x000007a5      8b45c0         mov eax, dword [local_40h]
:||   0x000007a8      4863d0         movsxd rdx, eax
:||   0x000007ab      488b45c8       mov rax, qword [local_38h]
:||   0x000007af      4801d0         add rax, rdx                ; '('
:||   0x000007b2      0fb608         movzx ecx, byte [rax]
:||   0x000007b5      8b45c0         mov eax, dword [local_40h]
:||   0x000007b8      4863d0         movsxd rdx, eax
:||   0x000007bb      488b45c8       mov rax, qword [local_38h]
:||   0x000007bf      4801d0         add rax, rdx                ; '('
:||   0x000007c2      83f101         xor ecx, 1
:||   0x000007c5      89ca           mov edx, ecx
:||   0x000007c7      8810           mov byte [rax], dl
:||   0x000007c9      8345c001       add dword [local_40h], 1
:||   ; CODE XREF from main (0x7a3)
:|`-> 0x000007cd      8b45c0         mov eax, dword [local_40h]
:|    0x000007d0      3b45c4         cmp eax, dword [local_3ch]
`===< 0x000007d3      7cd0           jl 0x7a5
```

Finally, it is compared with the following string.

```
|   :  |    0x000007d5      c645d069       mov byte [local_30h], 0x69  ; 'i'
|   :  |    0x000007d9      c645d172       mov byte [local_2fh], 0x72  ; 'r'
|   :  |    0x000007dd      c645d262       mov byte [local_2eh], 0x62  ; 'b'
|   :  |    0x000007e1      c645d375       mov byte [local_2dh], 0x75  ; 'u'
|   :  |    0x000007e5      c645d467       mov byte [local_2ch], 0x67  ; 'g'
|   :  |    0x000007e9      c645d57a       mov byte [local_2bh], 0x7a  ; 'z'
|   :  |    0x000007ed      c645d676       mov byte [local_2ah], 0x76  ; 'v'
|   :  |    0x000007f1      c645d731       mov byte [local_29h], 0x31  ; '1'
|   :  |    0x000007f5      c645d876       mov byte [local_28h], 0x76  ; 'v'
|   :  |    0x000007f9      c645d95e       mov byte [local_27h], 0x5e  ; '^'
|   :  |    0x000007fd      c645da78       mov byte [local_26h], 0x78  ; 'x'
|   :  |    0x00000801      c645db31       mov byte [local_25h], 0x31  ; '1'
|   :  |    0x00000805      c645dc74       mov byte [local_24h], 0x74  ; 't'
|   :  |    0x00000809      c645dd5e       mov byte [local_23h], 0x5e  ; '^'
|   :  |    0x0000080d      c645de6a       mov byte [local_22h], 0x6a  ; 'j'
|   :  |    0x00000811      c645df6f       mov byte [local_21h], 0x6f  ; 'o'
|   :  |    0x00000815      c645e031       mov byte [local_20h], 0x31  ; '1'
|   :  |    0x00000819      c645e176       mov byte [local_1fh], 0x76  ; 'v'
|   :  |    0x0000081d      c645e25e       mov byte [local_1eh], 0x5e  ; '^'
|   :  |    0x00000821      c645e365       mov byte [local_1dh], 0x65  ; 'e'
|   :  |    0x00000825      c645e435       mov byte [local_1ch], 0x35  ; '5'
|   :  |    0x00000829      c645e55e       mov byte [local_1bh], 0x5e  ; '^'
|   :  |    0x0000082d      c645e676       mov byte [local_1ah], 0x76  ; 'v'
|   :  |    0x00000831      c645e740       mov byte [local_19h], 0x40  ; segment.PHDR
|   :  |    0x00000835      c645e832       mov byte [local_18h], 0x32  ; '2'
|   :  |    0x00000839      c645e95e       mov byte [local_17h], 0x5e  ; '^'
|   :  |    0x0000083d      c645ea39       mov byte [local_16h], 0x39  ; '9'
|   :  |    0x00000841      c645eb69       mov byte [local_15h], 0x69  ; 'i'
|   :  |    0x00000845      c645ec33       mov byte [local_14h], 0x33  ; '3'
|   :  |    0x00000849      c645ed63       mov byte [local_13h], 0x63  ; 'c'
|   :  |    0x0000084d      c645ee40       mov byte [local_12h], 0x40  ; segment.PHDR
|   :  |    0x00000851      c645ef31       mov byte [local_11h], 0x31  ; '1'
|   :  |    0x00000855      c645f033       mov byte [local_10h], 0x33  ; '3'
|   :  |    0x00000859      c645f138       mov byte [local_fh], 0x38   ; '8'
|   :  |    0x0000085d      c645f27c       mov byte [local_eh], 0x7c   ; '|'
|   :  |    0x00000861      c645f300       mov byte [local_dh], 0
```
```
|   :  |    0x00000873      e898fdffff     call sym.imp.strcmp         ; int strcmp(const char *s1, const char *s2)
|   :  |    0x00000878      85c0           test eax, eax
|   `=====< 0x0000087a      0f85e4feffff   jne 0x764
|      |    0x00000880      488d3dc20000.  lea rdi, qword str.Oof__ur_too_good ; 0x949 ; "Oof, ur too good"
|      |    0x00000887      e854fdffff     call sym.imp.puts           ; int puts(const char *s)
```
So I wrote a simple [script](solve.py) to xor the string back and yield the flag.

```
hsctf{w0w_y0u_kn0w_d4_wA3_8h2bA029}
```

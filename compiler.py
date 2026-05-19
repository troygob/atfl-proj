'''
compiler for Panalo (.pnl).
'''

import os
import sys

#read args
program_filepath = sys.argv[1]

print("[CMD] Parsing")

###
### Tokenize
###

program_lines = []
with open(program_filepath, 'r') as f:
    program_lines = [
        line.strip() 
            for line in f.readlines()
    ]

program = []
for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    # check for empty opcode
    if opcode == "":
        continue

    # store opcode token
    program.append(opcode)

    #HANDLE EACH OPcode
    if opcode == "PUSH":
        # expecting a number
        number = int(parts[1])
        program.append(number)
    elif opcode == "PRINT":
        # parse string literal
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
    elif opcode == "JUMP.EQ.0":
        # read label
        label = parts[1]
        program.append(label)
    elif opcode == "JUMP.GT.0":
        # read label
        label = parts[1]
        program.append(label)

#read program 
print(program)

'''
Book keep string literals.
'''
string_literals = []
for ip in range(len(program)):
    if program[ip]== "PRINT":
        string_literal = program[ip+1]
        program[ip+1] = len(string_literals)
        string_literals.append(string_literal)


'''
compile to assembly
'''

asm_filepath = program_filepath[:-4] + ".asm"
out = open(asm_filepath, 'w')

out.write(""";--- header --- 
bits 64
default rel 
""")

out.write(""";--- variables --- 
section .bss
""")

out.write(""";--- constants --- 
section .data
""")
for i, string_literal in enumerate(string_literals):
    out.write(f'string_literal_{i}: db "{string_literal}", 0\n')


out.write(""";--- Entry Point --- 
section .text
global main
extern ExitProcess
extern printf
extern scanf
          
main:
\tPUSH rbp
\tMOV rbp, rsp
\tSUB rsp, 32
""")

ip = 0
while ip< len(program):
    opcode = program[ip]
    ip += 1

    if opcode.endswith(":"):
        out.write(f" -- LabeL ---\n")
        out.write(f"{opcode}\n")
    elif opcode == "PUSH":
        number = program[ip]
        ip += 1

        out.write(f"\t; -- PUSH {number} ---\n")
        out.write(f"\tPUSH {number}\n")
    elif opcode == "POP":
        out.write(f"; -- POP ---\n")
        out.write(f"\tPOP\n")
    elif opcode == "ADD":
        out.write(f"; -- ADD ---\n")
        out.write(f"\tPOP rax\n")
        out.write(f"\tADD qword [rsp], rax\n")
    elif opcode == "SUB":
        out.write(f"; -- SUB ---\n")
        out.write(f"\tPOP rax\n")
        out.write(f"\tSUB qword [rsp], rax\n")
    elif opcode == "PRINT":
        string_literal = program[ip]
        ip += 1

        out.write(f"; -- PRINT ---\n")
        out.write(f"\tLEA rcx, [rel string_literal_{string_literal}]\n")
        out.write(f"\tXOR eax, eax\n")
        out.write(f"\tCALL printf\n")
    elif opcode == "READ":
        out.write(f"; -- READ ---\n")
        out.write(f"; NOT IMPLEMENTED \n")

    elif opcode == "JUMP.EQ.0":
        out.write(f"; -- JUMP.EQ.0 ---\n")
        out.write(f"\tCMP qword [rsp], 0\n")
        out.write(f"\tJE {label}\n")
    elif opcode == "JUMP.GT.0":
        label = program[ip]
        ip += 1

        out.write(f"; -- JUMP.GT.0 ---\n")
        out.write(f"\tCMP qword [rsp], 0\n")
        out.write(f"\tJG {label}\n")
    elif opcode == "HALT":
        out.write(f"; -- HALT ---\n")
        out.write(f"\tJMP EXIT_LABEL\n")

out.write("EXIT_LABEL:\n")
out.write("\tXOR rax, rax\n")
out.write("\tCALL ExitProcess\n")

out.close()

print("[CMD] Assembling")
os.system(f"nasm -f elf64 {asm_filepath}")
print("[CMD] Linking")
os.system(f"gcc -o {asm_filepath[:-4] + '.exe'} {asm_filepath[:-3]+'o'}")

print("[CMD] Running")
os.system(f"{asm_filepath[:-4] + '.exe'}")
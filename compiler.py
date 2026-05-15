'''
compiler for Panalo (.pnl).
'''

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

# '''
# compile to assembly
# '''

# asm_filepath = program_filepath[:-4] + ".asm"
# out = open(asm_filepath, 'w')

# out.write(""";---header---
#             bits 64
#           default rel 
#           """)
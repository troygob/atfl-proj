;--- header --- 
bits 64
default rel 
;--- variables --- 
section .bss
;--- constants --- 
section .data
string_literal_0: db "Negative", 0
string_literal_1: db "Not Divisible by 3", 0
string_literal_2: db "Divisible by 3", 0
string_literal_3: db "Zero", 0
;--- Entry Point --- 
section .text
global main
extern ExitProcess
extern printf
extern scanf
          
main:
	PUSH rbp
	MOV rbp, rsp
	SUB rsp, 32
; -- READ ---
; NOT IMPLEMENTED 
; -- JUMP.EQ.0 ---
	CMP qword [rsp], 0
	JE L0
; -- JUMP.GT.0 ---
	CMP qword [rsp], 0
	JG L0
; -- PRINT ---
	LEA rcx, [rel string_literal_0]
	XOR eax, eax
	CALL printf
; -- HALT ---
	JMP EXIT_LABEL
; -- LabeL ---
L0:
	; -- PUSH 3 ---
	PUSH 3
; -- SUB ---
	POP rax
	SUB qword [rsp], rax
; -- JUMP.EQ.0 ---
	CMP qword [rsp], 0
	JE L0
; -- JUMP.GT.0 ---
	CMP qword [rsp], 0
	JG L0
; -- PRINT ---
	LEA rcx, [rel string_literal_1]
	XOR eax, eax
	CALL printf
; -- HALT ---
	JMP EXIT_LABEL
; -- LabeL ---
L1:
; -- PRINT ---
	LEA rcx, [rel string_literal_2]
	XOR eax, eax
	CALL printf
; -- HALT ---
	JMP EXIT_LABEL
; -- LabeL ---
L2:
; -- PRINT ---
	LEA rcx, [rel string_literal_3]
	XOR eax, eax
	CALL printf
; -- HALT ---
	JMP EXIT_LABEL
EXIT_LABEL:
	XOR rax, rax
	CALL ExitProcess

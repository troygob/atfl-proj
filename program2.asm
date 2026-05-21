;--- header --- 
bits 64
default rel 
;--- variables --- 
section .bss
;--- constants --- 
section .data
string_literal_0: db "odd", 0
string_literal_1: db "even", 0
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
	JE L2
; -- LabeL ---
L2:
	; -- PUSH 2 ---
	PUSH 2
; -- SUB ---
	POP rax
	SUB qword [rsp], rax
; -- JUMP.EQ.0 ---
	CMP qword [rsp], 0
	JE L2
; -- JUMP.GT.0 ---
	CMP qword [rsp], 0
	JG L2
; -- PRINT ---
	LEA rcx, [rel string_literal_0]
	XOR eax, eax
	CALL printf
; -- HALT ---
	JMP EXIT_LABEL
; -- LabeL ---
L1:
; -- PRINT ---
	LEA rcx, [rel string_literal_1]
	XOR eax, eax
	CALL printf
; -- HALT ---
	JMP EXIT_LABEL
EXIT_LABEL:
	XOR rax, rax
	CALL ExitProcess

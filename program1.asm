;--- header --- 
bits 64
default rel 
;--- variables --- 
section .bss
;--- constants --- 
section .data
string_literal_0: db "not equal", 0
string_literal_1: db "equal", 0
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
; -- READ ---
; NOT IMPLEMENTED 
; -- SUB ---
	POP rax
	SUB qword [rsp], rax
; -- JUMP.EQ.0 ---
	CMP qword [rsp], 0
	JE L1
; -- PRINT ---
	LEA rcx, [rel string_literal_0]
	XOR eax, eax
	CALL printf
; -- HALT ---
	JMP EXIT_LABEL
 -- LabeL ---
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

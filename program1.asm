;--- header --- 
bits 64
default rel 
;--- variables --- 
section .bss
;--- constants --- 
section .data
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
; NOT IMPLEMENTED 
; -- HALT ---
	JMP EXIT_LABEL
 -- LabeL ---
L1:
; -- PRINT ---
; NOT IMPLEMENTED 
; -- HALT ---
	JMP EXIT_LABEL
EXIT_LABEL:
	XOR rax, rax
	CALL ExitProcess

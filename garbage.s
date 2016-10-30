	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 12
	.globl	_main
	.align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## BB#0:
	pushq	%rbp
Ltmp0:
	.cfi_def_cfa_offset 16
Ltmp1:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
Ltmp2:
	.cfi_def_cfa_register %rbp
	subq	$48, %rsp
	movl	$0, -4(%rbp)
	movl	%edi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	-16(%rbp), %rsi
	movq	8(%rsi), %rdi
	movb	$0, %al
	callq	_atoi
	movl	%eax, -20(%rbp)
	movq	-16(%rbp), %rsi
	movq	16(%rsi), %rdi
	movb	$0, %al
	callq	_atoi
	leaq	L_.str(%rip), %rdi
	movl	%eax, -24(%rbp)
	movl	-20(%rbp), %eax
	cltd
	idivl	-24(%rbp)
	cvtsi2ssl	%eax, %xmm0
	movss	%xmm0, -32(%rbp)
	movl	-20(%rbp), %esi
	movl	-24(%rbp), %eax
	cvtss2sd	-32(%rbp), %xmm0
	movl	%eax, %edx
	movb	$1, %al
	callq	_printf
	xorl	%edx, %edx
	movl	%eax, -36(%rbp)         ## 4-byte Spill
	movl	%edx, %eax
	addq	$48, %rsp
	popq	%rbp
	retq
	.cfi_endproc

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"%d/%d= %f\n"


.subsections_via_symbols

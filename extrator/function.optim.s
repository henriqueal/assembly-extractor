	.text
	.file	"function.optim.ll"
	.globl	DSP_autocor_c
	.align	4
	.type	DSP_autocor_c,@function
DSP_autocor_c:                          ! @DSP_autocor_c
! BB#0:
	save %sp, -128, %sp
	st %i0, [%fp+-4]
	st %i1, [%fp+-8]
	st %i2, [%fp+-12]
	st %i3, [%fp+-16]
	ba .LBB0_1
	st %g0, [%fp+-20]
.LBB0_5:                                !   in Loop: Header=BB0_1 Depth=1
	ld [%fp+-28], %i0
	srl %i0, 15, %i0
	ld [%fp+-20], %i1
	sll %i1, 1, %i1
	ld [%fp+-4], %i2
	sth %i0, [%i2+%i1]
	ld [%fp+-20], %i0
	add %i0, 1, %i0
	st %i0, [%fp+-20]
.LBB0_1:                                ! =>This Loop Header: Depth=1
                                        !     Child Loop BB0_3 Depth 2
	ld [%fp+-16], %i0
	ld [%fp+-20], %i1
	cmp %i1, %i0
	bge	 .LBB0_6
	nop
! BB#2:                                 !   in Loop: Header=BB0_1 Depth=1
	st %g0, [%fp+-28]
	ba .LBB0_3
	ld [%fp+-16], %i0
.LBB0_4:                                !   in Loop: Header=BB0_3 Depth=2
	ld [%fp+-20], %i0
	ld [%fp+-24], %i1
	sub %i1, %i0, %i0
	sll %i1, 1, %i1
	ld [%fp+-8], %i2
	ldsh [%i2+%i1], %i1
	sll %i0, 1, %i0
	ldsh [%i2+%i0], %i0
	smul %i1, %i0, %i0
	ld [%fp+-28], %i1
	add %i1, %i0, %i0
	st %i0, [%fp+-28]
	ld [%fp+-24], %i0
	add %i0, 1, %i0
.LBB0_3:                                !   Parent Loop BB0_1 Depth=1
                                        ! =>  This Inner Loop Header: Depth=2
	st %i0, [%fp+-24]
	ld [%fp+-16], %i0
	ld [%fp+-12], %i1
	add %i1, %i0, %i0
	ld [%fp+-24], %i1
	cmp %i1, %i0
	bge	 .LBB0_5
	nop
	ba .LBB0_4
	nop
.LBB0_6:
	ret
	restore
.Lfunc_end0:
	.size	DSP_autocor_c, .Lfunc_end0-DSP_autocor_c

	.ident	"clang version 3.7.1 (tags/RELEASE_371/final)"
	.section	".note.GNU-stack"

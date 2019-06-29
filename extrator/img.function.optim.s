	.text
	.file	"function.optim.ll"
	.globl	IMG_yc_demux_le16_c
	.align	4
	.type	IMG_yc_demux_le16_c,@function
IMG_yc_demux_le16_c:                    ! @IMG_yc_demux_le16_c
! BB#0:
	save %sp, -120, %sp
	st %i0, [%fp+-4]
	st %i1, [%fp+-8]
	st %i2, [%fp+-12]
	st %i3, [%fp+-16]
	st %i4, [%fp+-20]
	ba .LBB0_1
	st %g0, [%fp+-24]
.LBB0_2:                                !   in Loop: Header=BB0_1 Depth=1
	ld [%fp+-24], %i0
	sll %i0, 2, %i0
	ld [%fp+-8], %i1
	ldub [%i1+%i0], %i1
	ld [%fp+-12], %i2
	sth %i1, [%i2+%i0]
	ld [%fp+-24], %i0
	sll %i0, 2, %i0
	ld [%fp+-12], %i1
	add %i0, %i1, %i1
	ld [%fp+-8], %i2
	add %i0, %i2, %i0
	ldub [%i0+2], %i0
	sth %i0, [%i1+2]
	ld [%fp+-24], %i0
	sll %i0, 2, %i1
	ld [%fp+-8], %i2
	add %i1, %i2, %i1
	ldub [%i1+1], %i1
	sll %i0, 1, %i0
	ld [%fp+-16], %i2
	sth %i1, [%i2+%i0]
	ld [%fp+-24], %i0
	sll %i0, 2, %i1
	ld [%fp+-8], %i2
	add %i1, %i2, %i1
	ldub [%i1+3], %i1
	sll %i0, 1, %i0
	ld [%fp+-20], %i2
	sth %i1, [%i2+%i0]
	ld [%fp+-24], %i0
	add %i0, 1, %i0
	st %i0, [%fp+-24]
.LBB0_1:                                ! =>This Inner Loop Header: Depth=1
	ld [%fp+-4], %i0
	sra %i0, 1, %i0
	ld [%fp+-24], %i1
	cmp %i1, %i0
	bge	 .LBB0_3
	nop
	ba .LBB0_2
	nop
.LBB0_3:
	ret
	restore
.Lfunc_end0:
	.size	IMG_yc_demux_le16_c, .Lfunc_end0-IMG_yc_demux_le16_c


	.ident	"clang version 3.7.1 (tags/RELEASE_371/final)"
	.section	".note.GNU-stack"

ldi r1 15
ldi r2 3
ldi r3 0
.loop
sub r1 r1 r2
inc r3 r3
sub r0 r1 r2
cjp c0 .done
cjp c2 .done
jmp .loop
.done
inc r3 r3
hlt
ldi r0 0
ldi r1 0
ldi r2 1
ldi r3 0
ldi r4 12
.loop
    add r3 r1 r2
    add r1 r2 r0
    add r2 r3 r0
    dec r4 r4
    pst r3 p7
    cjp c2 .done
    jmp .loop
.done
hlt

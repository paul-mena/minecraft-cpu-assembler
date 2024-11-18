ldi r1 7
.main_loop
    pst r1 p7
    jmp .odd_even
    .odd_even_end
    # if value in r1 is even zero flag is set
    cjp !zero .3n+1
    rsh r1 r1
    .3n+1_end
    dec r3 r1
    cjp !zero .main_loop
pst r1 p7
hlt
# Functions
.odd_even
    rsh r3 r1
    add r3 r3 r3
    sub r3 r1 r3
    jmp .odd_even_end
.3n+1
    add r3 r1 r0
    add r1 r1 r1
    add r1 r1 r3
    inc r1 r1
    jmp .3n+1_end
    
ldi r1 7
.main_loop
    pst r1 p7
    jmp .mod
    .mod_end
    # Modulo of r1 and r2 left in r3
    add r3 r3 r3
    cjp !zero .3n+1
    rsh r1 r1
    .3n+1_end
    dec r3 r1
    cjp !zero .main_loop
pst r1 p7
hlt
# Functions
.mod
    ldi r2 2
    add r3 r1 r0
    .div_loop
        sub r3 r3 r2
        cjp !msb .div_loop
    add r3 r3 r2
    jmp .mod_end
.3n+1
    add r3 r1 r0
    add r1 r1 r1
    add r1 r1 r3
    inc r1 r1
    jmp .3n+1_end
    
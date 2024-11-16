ldi r1 10
.main_loop
    pst r1 p7
    jmp .mod
    .mod_end
    # Modulo of r1 and r2 left in r3
    add r3 r3 r3
    #pst r3 p7
    cjp !zero .3n+1
    rsh r1 r1
    .3n+1_end
    dec r3 r1
    #pst r3 p7
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
    ldi r3 3
    .mult_loop
        add r4 r4 r1
        dec r3 r3
        cjp !zero .mult_loop
    add r1 r4 r0
    inc r1 r1
    jmp .3n+1_end
    
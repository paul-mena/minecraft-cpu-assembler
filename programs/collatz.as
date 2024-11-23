ldi r1 7
ldi r2 254
.main_loop
    pst r1 p7
    bnt r0 r1 nor r2
    # if value in r1 is odd zero flag is set
    cjp zero .3n+1
    rsh r1 r1
    .3n+1_end
    dec r0 r1
    cjp !zero .main_loop
pst r1 p7
hlt
# Functions
.3n+1
    add r3 r1 r0
    add r1 r1 r1
    add r1 r1 r3
    inc r1 r1
    jmp .3n+1_end
    
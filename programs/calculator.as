ldi r2 10
.wait_for_input
    pld r1 p0
    sub r3 r1 r2
    cjp zero .wait_for_input
pst r1 p7
jmp .wait_for_input
hlt
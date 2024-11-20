ldi r5 10
ldi r1 0
ldi r2 0
ldi r3 0
ldi r4 0
.wait_for_input
    pld r1 p0
    sub r6 r1 r5
    cjp zero .wait_for_input
#
pst r1 p7
add r3 r1 r0
jmp .mult_ten
.mult_ten_end
add r2 r3 r4
pst r2 p7
jmp .wait_for_input
hlt
#Functions
#Multiplies value in r2 by 10 and stores it in r4
.mult_ten
    add r4 r2 r2
    add r2 r2 r2
    add r2 r2 r2
    add r2 r2 r2
    add r4 r4 r2
    jmp .mult_ten_end
    

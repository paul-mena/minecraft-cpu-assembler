pld r1 p0
pld r2 p1
ldi r3 0
.loop
    inc r3 r3
    sub r1 r1 r2
    cjp !msb .loop
dec r3 r3
pst r3 p7
#Compute Modulo
add r1 r1 r2
hlt

ldi r1 15
ldi r2 3
ldi r3 0
.loop
    inc r3 r3
    sub r1 r1 r2
    cjp !msb .loop
dec r3 r3
pst r3 p7
hlt

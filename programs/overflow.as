ldi r1 1
ldi r2 255
add r3 r1 r2
#stores first byte in r3 and second byte in r4
cjp carry .use2ndReg
pst r4 p7
hlt
.use2ndReg
    inc r4 r4
    pst r4 p7
    hlt
# Initialize two 2s Complement negative numbers
ldi r1 128 # -128
ldi r2 255 # -1
add r3 r1 r2
# Stores result in r3
cjp carry .showError
pst r4 p7
hlt
.showError
    # print 1 to io port 7 to indicate overflow
    ldi r4 1
    pst r4 p7
    hlt
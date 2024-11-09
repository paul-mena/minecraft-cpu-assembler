ldi r1 10
#
.loop
pst r1 p7
# Check if value in r1 is equal to zero
cjp zero .done
dec r1 r1
jmp .loop
#
.done
hlt
ldi r1 10
ldi r7 0
jmp .create_var
.created_var
ldi r1 0
ldi r7 0
mld r1
pst r1 p7
hlt
.create_var
mst r1
inc r7 r7
jmp .created_var

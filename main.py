from assembler import assemble
from emulator import run

#assemble('programs/fibsequence.as', 'machine_code.txt')
#run('machine_code.txt')
assemble('programs/division.as', 'machine_code.txt')
run('machine_code.txt')
#assemble('programs/countdown.as', 'machine_code.txt')
#run('machine_code.txt')
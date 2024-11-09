from assembler import assemble
from emulator import run

assemble('program.as', 'machine_code.txt')
run('machine_code.txt')
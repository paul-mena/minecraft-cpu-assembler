from assembler import assemble
from schematic import create_schematic
from emulator import run

assemble('programs/division.as', 'machine_code.txt')
run('machine_code.txt')
create_schematic('machine_code.txt')

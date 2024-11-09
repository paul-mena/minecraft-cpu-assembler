from assembler import assemble
from emulator import run
from emulator import resetEmulator

assemble('programs/fibsequence.as', 'machine_code.txt')
run('machine_code.txt')
resetEmulator()
assemble('programs/division.as', 'machine_code.txt')
run('machine_code.txt')
resetEmulator()
assemble('programs/countdown.as', 'machine_code.txt')
run('machine_code.txt')
from assembler import assemble
from schematic import create_schematic
from emulator import run

path = "C:/Users/paulm/AppData/Roaming/.minecraft/config/worldedit/schematics"
program = 'overflow'

def assemble_and_run(program):
    assemble('programs/' + program + '.as', 'programs/machine_code.txt')
    run('programs/machine_code.txt')

def assemble_and_make_schem(program, path):
    assemble('programs/' + program + '.as', 'programs/machine_code.txt')
    create_schematic('programs/machine_code.txt', path, program)

assemble_and_run(program)
#assemble_and_make_schem(program, path)

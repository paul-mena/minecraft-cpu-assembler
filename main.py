from assembler import assemble
from schematic import create_schematic
from emulator import run

path = "C:/Users/paulm/AppData/Roaming/.minecraft/config/worldedit/schematics"
program = 'fibsequence'

def assemble_and_run(program_file_path):
    assemble(program_file_path, 'machine_code.txt')
    run('machine_code.txt')

def assemble_and_make_schem(program, path):
    assemble('programs/' + program + '.as', 'machine_code.txt')
    create_schematic('machine_code.txt', path, program)

assemble_and_make_schem(program, path)

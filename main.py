import argparse
from assembler import assemble
from schematic import create_schematic
from emulator import run

#path = "C:/Users/paulm/AppData/Roaming/.minecraft/config/worldedit/schematics"
#program = 'overflow'

parser = argparse.ArgumentParser()

#parser.add_argument("schem_dir")
parser.add_argument("program")

args = parser.parse_args()

def assemble_and_run(program):
    assemble('programs/' + program + '.as', 'programs/machine_code.txt')
    run('programs/machine_code.txt')

def assemble_and_make_schem(program, path):
    assemble('programs/' + program + '.as', 'programs/machine_code.txt')
    create_schematic('programs/machine_code.txt', path, program)

assemble_and_run(args.program)
#assemble_and_make_schem(program, path)

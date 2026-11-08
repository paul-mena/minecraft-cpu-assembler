This is an asembler and emulator I made for an 8-bit computer I made in minecraft. It uses a custom instruction set since a minecraft computer ain't running x86. Currently don't have a full cli or the world uploaded so you can only run programs in the emulator. This is just an old project I made public for anyone curious.

If you want to attempt to use this proceed to the instructions below. 

# Usage
Clone the repo
```bash
git clone https://github.com/paul-mena/minecraft-cpu-assembler
```
Setup a Python virtual environment, try `python3` if `python` doesn't work
```bash
python -m venv venv
source venv/bin/activate
```
Install mcschematic
```bash
pip install mcschematic
```
Run a program from programs in the emualtor.
```bash
python main.py fibsequence
```
At the end of each run, the emulator will print a memory dump of all 32 bytes of memory and then the registers.

I don't have docs for the instruction set but feel free to take a look at the examples in `programs/`
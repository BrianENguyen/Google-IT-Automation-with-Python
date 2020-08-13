import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, 'w') as file:
        file.write('New file created\n')
else:
    print(f'Error, the file {filename} already exists')
    sys.exit(1)
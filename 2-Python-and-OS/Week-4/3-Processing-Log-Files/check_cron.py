import sys
import re

logfile = sys.argv[1]
with open(logfile) as file:
    for line in file:
        if 'CRON' not in line:
            # Tells loop to go to next line
            continue
        pattern = r'USER \((\w+)\)$'
        result = re.search(pattern, line)
        print(result[1])
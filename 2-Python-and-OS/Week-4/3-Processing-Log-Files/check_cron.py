import sys
import re
usernames = {}
logfile = sys.argv[1]
with open(logfile) as file:
    for line in file:
        if 'CRON' not in line:
            # Tells loop to go to next line
            continue
        pattern = r'USER \((\w+)\)$'
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)
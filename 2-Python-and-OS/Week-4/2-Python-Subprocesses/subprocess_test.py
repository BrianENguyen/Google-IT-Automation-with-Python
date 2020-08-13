import subprocess
subprocess.run(['date'])
subprocess.run(['sleep', '2'])

result = subprocess.run(['ls', 'this_nonexistent_file'])
print(result.returncode)
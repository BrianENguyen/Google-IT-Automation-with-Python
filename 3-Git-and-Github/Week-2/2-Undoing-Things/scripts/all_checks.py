import os, sys

def check_reboot():
    '''Returns true if the computer has a pending reboot'''
    return os.path.exists('/run/reboot-required')

def main():
    if check_reboot():
        print('Pending reboot')
        sys.exit(1)
    if disk_full():
        print('Disk full')
        sys.exit(1)
    print('Everything ok')
    sys.exit(0)
main()
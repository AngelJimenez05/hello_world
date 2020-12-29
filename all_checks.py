
import os
import  shutil
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_Gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * (du.free / du.total)
    # Calculate how many free Gb in disk
    gibabytes_free = du.free / 2**30 # There are 2**30 bytes/Gb (conversion)
    # Check
    if gibabytes_free < min_Gb or percent_free < min_percent:
        return True
    return False


def check_root_full():
    """Return True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_Gb=2, min_percent=10)


def main():
    if check_reboot():
        print("Pending reboot.")
        sys.exit(1)
    if check_root_full():
        print("Root partition full.")
        sys.exit(1)
        
    print("Everything ok.")
    sys.exit(0)

main()
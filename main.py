import sys
import re
import time
from colorama import Fore, Back, init

def main(executable):
    download_id = re.sub("[^0-9]", "", executable)
    print(Fore.GREEN + "Your download link is: " + Fore.RESET + f"http://directdl.xyz/dm.php?id={download_id}")
    print("\nClosing in 5 seconds...")
    time.sleep(5)
    return 0

# Start
if __name__ == '__main__':
    init() # Colorama.init() - Overwhise colors don't work
    if len(sys.argv) > 1:
        exe = sys.argv[1]
        main(exe)
    else:
        print(Fore.RED + "Error: No executable specified!" + Fore.RESET)
import sys
import re
import time
from colorama import Fore, Back, init
import pyperclip as pc
import requests

def bypass(download_id):
    bypass_request = requests.get("http://dlsft.com/callback/info.php?id=" + download_id)
    channel = bypass_request.text.split("**")[0]
    requests.post(f"http://dlsft.com/callback/?channel={channel}&id={download_id}&action=started")
    requests.post(f"http://dlsft.com/callback/?channel={channel}&id={download_id}&action=completed")

def main(executable):
    download_id = re.sub("[^0-9]", "", executable) 
    bypass(download_id)
    print(Fore.GREEN + "Your download link is: " + Fore.RESET + f"http://directdl.xyz/dm.php?id={download_id}")
    print("Copied to clipboard")
    pc.copy(f"http://directdl.xyz/dm.php?id={download_id}")
    print("\nClosing in 5 seconds...")
    time.sleep(5)

# Start
if __name__ == '__main__':
    init() # Colorama.init() - Overwhise colors don't work
    if len(sys.argv) > 1:
        exe = sys.argv[1]
        main(exe)
    else:
        print(Fore.RED + "Error: No executable specified!" + Fore.RESET)
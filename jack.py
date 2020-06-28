from termcolor import colored
from urllib.request import urlopen
from sys import argv, exit

__author__ = '4N7U'
print("")
print(colored("     (_) /   |     | |    ",'green'))
print(colored("      _ / /| | __ _| | __ ",'green'))
print(colored("     | / /_| |/ _` | |/ / ",'green'))
print(colored("     | \___  | (_| |   <  ",'green'))
print(colored("     | |   |_/\__,_|_|\_\ ",'green'))
print(colored("    _/ |                  ",'green'))
print(colored("   |__/                   ",'green'))
print("") 
print(colored("#     Develop by ArMan HoSSa!n     #", 'yellow'))
print(colored("#         Twitter:@antu1024        #", 'yellow'))
print(colored("#   Automatic ChickJacking Scanner #", 'yellow'))
print("")
def check(url):
    try:
        if "http" not in url: url = "http://" + url

        data = urlopen(url)
        headers = data.info()

        if not "X-Frame-Options" in headers: return True

    except: return False

def main():

    try: sites = open(argv[1], 'r').readlines()
    except: print(colored("[*] Usage: python(3) jack.py (file_name)",'cyan')); exit(0)

    for site in sites[0:]:
        print(colored("\n[+] Checking " + site,'cyan'))
        status = check(site)

        if status: 
        	print(colored(" [:-)] vulnerable == ",'red'),site)
        	f = open("vulnerable.txt",'a+')
        	f.write(str(site))
        	f.close()
        elif not status: print(colored(" [:-(] Website is not vulnerable!",'green'))
        else: print(colored('Every single thing is crashed, Python got mad, dude wtf you just did?','cyan'))

if __name__ == '__main__': main()
print("")
print(colored("#       CopyRight © antu1024      #", 'yellow'))
print("") 

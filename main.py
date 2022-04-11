from colorama import Fore
from functions import *

logo = Fore.GREEN + """d8888b. d8888b. d8b   db d888888b    .d8888.  .o88b. 
88  `8D 88  `8D 888o  88 `~~88~~'    88'  YP d8P  Y8 
88oodD' 88oobY' 88V8o 88    88       `8bo.   8P      
88~~~   88`8b   88 V8o88    88         `Y8b. 8b      
88      88 `88. 88  V888    88    db db   8D Y8b  d8 
88      88   YD VP   V8P    YP    VP `8888Y'  `Y88P' 
                                                     
                                                     
.d8888. d8b   db d888888b d8888b. d88888b d8888b.                     _    _    _
88'  YP 888o  88   `88'   88  `8D 88'     88  `8D                    |_)=A=0=A=(_|
`8bo.   88V8o 88    88    88oodD' 88ooooo 88oobY'    A____________ _____H___H___o    _____
  `Y8b. 88 V8o88    88    88~~~   88~~~~~ 88`8b     O____________<^       ====__~`\_/    /`~~| 
db   8D 88  V888   .88.   88      88.     88 `88.                 `\_________(_)>.  ___--'   | 
`8888Y' VP   V8P Y888888P 88      Y88888P 88   YD                                 \/   `-----' 
"""
options = Fore.WHITE +"""
 ---------------------------------------------------------------------------
|  Provide number of images to download and press [ENTER] to start sniping   |
 ---------------------------------------------------------------------------
    """
inputterminal = Fore.RED + "root@prntscsniper ~ % " + Fore.WHITE

def main():
    print(logo + options)
    number = input(inputterminal)
    start(number)

if __name__ == "__main__":
    main()

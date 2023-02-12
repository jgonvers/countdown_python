import time
import platform
import sys
from io import StringIO

from pynput import keyboard

if platform.system() == "Windows":   
    from colorama import just_fix_windows_console
    just_fix_windows_console()

is_running = False
first_line_or = "(s)tart/(s)top/(r)eset/(q)uit/(c)hange"
first_line = ""
second_line = ""

class Countdown:
    def __init__(self, hour=0,min=0,sec=0):
        self.set_start(hour,min,sec)

    def __str__(self):
        hour = self.current//3600
        min = (self.current%3600)//60
        sec = self.current%60
        return f"{hour}:{min}:{sec}"

    def __repr__(self):
        return f"start = {self.start}, current = {self.current}"

    def set_start(self,hour=0,min=0,sec=0):
        self.start = int(hour*3600 + min*60 + sec)
        self.current = self.start

    def restart(self):
        self.current = self.start

    def decrement(self):
        if self.current > 0:
            self.current -= 1
            return self.current != 0
        else:
            return False

def set_start(countdown):
    global second_line
    empty_screen()
    inp = input("give your timer in the format hours:minutes:seconds\n")
    try:
        inp = inp.strip().split(":")
        countdown.set_start(int(inp[0]), int(inp[1]), int(inp[2]))
    except:
        second_line = "wrong input"

def on_release(key):
    global is_running
    global countdown
    print(key.char)
    try:
        key.char
    except AttributeError:
        return
    match(key.char):
        case "s":
            is_running = not is_running
        case "r":
            is_running = False
            coutdown.restart()
        case "q":
            second_line = "quitting..."
            return False
        case "c":
            set_start(countdown)
    print_screen()
            

def empty_screen(n_lines=2):
    print(n_lines*"\033[F"+n_lines*(100*" "+"\n")[:-2]+n_lines*"\033[F")
    
def print_screen():
    global second_line
    global first_line
    empty_screen()
    if first_line:
        print(first_line)
        first_line = ""
    else:
        print(first_line_or)
    if second_line:
        print(second_line)
        second_line = ""
    else:
        print(countdown)

if __name__ == "__main__":
    countdown = Countdown()
    print("\n")
    with keyboard.Listener(on_release=on_release, supress=True) as listener:
        print_screen()
        while listener.is_alive():
            time.sleep(0.1)
            while is_running:
                time.sleep(1)
                if is_running and not countdown.decrement():
                    is_running = False
                else:
                    print_screen()
    #sys.stdin.read()

            
        

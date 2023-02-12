import time
import platform

if platform.system() == "Windows":
    # allow the use of ansi stuff in the console like \033[F
    # needed on windows
    from colorama import just_fix_windows_console

    just_fix_windows_console()

is_running = False
first_line_or = "(s)tart/(r)eset/(q)uit/(c)hange"
first_line_ru = (
    "countdown running, you can quit by CTRL+c like a barbarian if you want"
)
first_line = ""
second_line = ""


class Countdown:
    def __init__(self, hour=0, min=0, sec=0):
        self.set_start(hour, min, sec)

    def __str__(self):
        hour = self.current // 3600
        min = (self.current % 3600) // 60
        sec = self.current % 60
        return f"{hour}:{min}:{sec}"

    def __repr__(self):
        return f"start = {self.start}, current = {self.current}"

    def set_start(self, hour=0, min=0, sec=0):
        self.start = int(hour * 3600 + min * 60 + sec)
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


def input_action(input):
    global second_line
    global is_running
    match (input):
        case "s":
            is_running = not is_running
        case "r":
            is_running = False
            countdown.restart()
        case "q":
            second_line = "quitting..."
            return True
        case "c":
            set_start(countdown)
    print_screen()


def empty_screen(n_lines=2):
    print(
        n_lines * "\033[F"
        + n_lines * (100 * " " + "\n")[:-2]
        + n_lines * "\033[F"
    )


def print_screen():
    global second_line
    global first_line
    empty_screen()
    if first_line:
        print(first_line)
        first_line = ""
    else:
        print(first_line_ru if is_running else first_line_or)
    if second_line:
        print(second_line)
        second_line = ""
    else:
        print(countdown)


if __name__ == "__main__":
    countdown = Countdown()
    print("\n")  # generate the second line for the string
    while True:
        print_screen()
        if not is_running:
            inp = input("")
            empty_screen(1)
            if input_action(inp):
                break
        else:
            time.sleep(1)
            if not countdown.decrement():
                is_running = False
    print_screen()

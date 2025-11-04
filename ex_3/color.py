from colorama import Fore, Style

def color_directory(name):
    return f"{Fore.CYAN}{name}{Style.RESET_ALL}"

def color_file(name):
    return f"{Fore.YELLOW}{name}{Style.RESET_ALL}"

       
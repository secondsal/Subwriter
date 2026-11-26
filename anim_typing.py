from rich import print as fprint
import time

def print_line(text: str, typingMs: int, afterMs: int, color: str, fromNewLine: bool):
    try:
        speed = typingMs/len(text)
    except ZeroDivisionError:
        speed = 0
    
    textList = list(text)
    endChar = ""
    if fromNewLine == True:
        endChar = "\n"
    
    for i, ch in enumerate(textList):
        if i == len(textList)-1:
            fprint(f"[{color}]{ch}[/{color}]", end=endChar)
        else:
            fprint(f"[{color}]{ch}[/{color}]", end="")
        time.sleep(speed/1000)
    time.sleep(afterMs/1000)
    
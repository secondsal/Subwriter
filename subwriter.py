import csv
import pathlib
import sys
from rich import print as fprint
from scf import load_config, simple_conf_key_get, get_config
from anim_typing import print_line

SONG_CSV_VERSION = 0.1
VERSION = 0.2
AppDirectory = str(pathlib.Path().resolve()).replace('\\', '/')

lines = []

def strToBoolReal(x: str) -> bool:
    if x == "True":
        return True
    else:
        return False

# [Text, TypingMs, AfterMs, Color, FromNewLine]

LangStr = {
    "1": {
        "[1]": "[yellow]No song selected. Write the song .csv file name [/yellow]\n(Drop all .csv's in songs/ directory)",
        "[2]": "Enter song name (without '.csv' at the end) > ",
        "[3]": "[red]Song file not found[/red]",
        "[4]": "[red]Incompatible csv versions![/red]"
    },
    "2": {
        "[1]": "[yellow]Пісню не вибрано. Вкажіть .csv назви пісенного файлу [/yellow]\n(Всі .csv файли мають бути у папці songs/)",
        "[2]": "Вкажіть назву пісні (без '.csv' вкінці) > ",
        "[3]": "[red]Файл пісні не знайдено[/red]",
        "[4]": "[red]Не підтримувана версія csv![/red]"
    }
}


def BeforeWriteMenu(args):
    fprint(f"SuBwRiTer [green]v{VERSION}[/green]\n")
    fprint(simple_conf_key_get("langIndex", "[1]", LangStr),"\n\n")

    filename = input(simple_conf_key_get("langIndex", "[2]", LangStr))
    if pathlib.Path(f"{AppDirectory}/songs/{filename}.csv").exists():
        with open(f'{AppDirectory}/songs/{filename}.csv', 'r', encoding="utf-8-sig") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            for line in reader:
                lines.append(line)
            lines.pop(0)
            writeMenu()
    else:
        fprint(simple_conf_key_get("langIndex", "[3]", LangStr))

def writeMenu():
    for line in lines:
        if "<$$$>" in line[0]:
            continue
        if line[0] == "<Empty Line>" and len(line) == 1:
            # giving all the instructions
            line[0] = "\n"
            line.append("0")
            line.append("0")
            line.append("white")
            line.append("False")
        
        if line[0].lower() == "<using version>" and len(line) == 2:
            version = float(line[1])
            if SONG_CSV_VERSION <= version:
                fprint(simple_conf_key_get("langIndex", "[4]", LangStr))
                return
            continue
        
        try:
            print_line(line[0], int(line[1]), int(line[2]), str(line[3]), strToBoolReal(line[4]))
        except ValueError:
            print("Incorrect syntax.")

if __name__ == "__main__":
    load_config("subconf.scf")
    try:
        BeforeWriteMenu(sys.argv)
    except KeyboardInterrupt:
        print("\nProgram Ended")
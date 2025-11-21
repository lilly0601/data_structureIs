from time import sleep
from rich import print
from random import choice, uniform

def printLyrics():
    lines = [
        ("I wanna da-",0.06),
        ("I wanna dance in the lights",0.05),
        ("I wanna ro-",0.07),
        ("I wanna rock your body",0.08),
        ("I wanna go",0.08),
        ("I wanna go for a ride",0.068),
        ("Hop in the music and",0.07),
        ("Rock your body",0.08),
        ("Rock the body",0.069),
        ("Come on,come on",0.035),
        ("Rock that body",0.05),
        ("(Rock your body)",0.03),
        ("Rock that body",0.049),
        ("come on,come on",0.035),
        ("Rock your body",0.08)
    ]

    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

    print("[bold green]Скрипт запущен![/bold green]\n")

    for text, delay in lines:
        for char in text:
            color = choice(colors)
            print(f"[{color}]{char}[/{color}]", end="", flush=True)
            sleep(delay * uniform(0.8, 1.2))
        print()
        sleep(0.2)

if __name__ == "__main__":
    printLyrics()

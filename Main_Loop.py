from lists import *
from functions import *
from notes import *
import webbrowser
from URL import *

os.system("clear")

#Wish me function from functions.py:
wishMe()

while True:
    say("What would you like me to do?")
    command = input("What would you like me to do?")
    if "movies" in command or "netfli" in command or "film" in command:
        print("Here are some movies on netflix.")
        say("Here are some movies on netflix.")
        webbrowser.open(netflix)

    if "music" in command or "song" in command:
        print("Here are songs on Amazon music.")
        say("Here are songs on Amazon music.")
        webbrowser.open(music)

    if "time" in command or "cloc" in command or "date" in command:
        print(time)
        say(time)

    if "note" in command:
        print("Opening notepad.")
        say("Opening notepad.")
        notes()

    if "new" in command:
        print("Here is the latest news.")
        say("Here is the latest news.")
        webbrowser.open(news)

    if "shop" in command:
        print("Opening Amazon.")
        say("Opening amazon")
        webbrowser.open(shopping)

    if "mail" in command or "message" in command:
        email()

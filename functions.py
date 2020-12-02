#Code to be imported to main_code.py.
import os
import time
from os import system
import speech_recognition as sr
import datetime

#Fucttion for email:
def email():
    import smtplib
    server = smtplib.SMTP("smtp.outlook.com", 587)
    server.ehlo()
    server.starttls()
    server.login("fnariman@hotmail.com", "W!ldh0ney1")
    content = input("What would you like me to say?")
    server.sendmail("fnariman@hotmail.com", "freddy.nariman@gmail.com", content)
    server.close()

def alarm():
    import random
    import time
    import webbrowser
    import datetime
    from datetime import datetime
    from datetime import timedelta

    os.system('clear')
    url1 = "https://www.youtube.com/watch?v=y6Sxv-sUYtM"
    url2 = "https://www.youtube.com/watch?v=pRpeEdMmmQ0"
    url3 = "https://www.youtube.com/watch?v=OPf0YbXqDm0"
    url4 = "https://www.youtube.com/watch?v=09R8_2nJtjg"

    Time = time.strftime("%H:%M:%S")

    print("")
    print ("Currently it is:", Time)
    minutes_of_sleep = int(input("Enter the number of minutes you would like to sleep for:"))
    hours_of_sleep = int(input("Enter the number of hours you would like to sleep for:"))
    print("")

    Alarm = (datetime.now() + timedelta(hours=hours_of_sleep) + timedelta(minutes=minutes_of_sleep)).strftime('%H:%M:%S')
    print("You will be woken up at:", Alarm)
    yes_no = str(input("Would you like to set this alarm? [Y/N]")).lower()
    print("")

    while yes_no == "y" or yes_no == "yes":

        while Time != Alarm:
            print("It is currently:", time.strftime("%H:%M:%S"))
            Time = time.strftime("%H:%M:%S")
            time.sleep(1)
            if Time == Alarm:
                print("")
                print("Time to wake up!")
                url = random.choice([url1, url2, url3, url4])
                webbrowser.open(url)
                break

#Func for TTS:
def say(text):
    system("say {}".format(text))

#Func to obtain audio from the microphone:
def STT():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
			said = r.recognize_google(audio)
		except Exception as e:
			print("Exception:", str(e))

	return said.lower()

#Function for wishing with regard to time:
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning! ")

    elif hour>=12 and hour<17:
        say("Good Afternoon! ")

    elif hour>=17 and hour<24 :
        say("Good Evening! ")

#Define the time variable
time = time.ctime()

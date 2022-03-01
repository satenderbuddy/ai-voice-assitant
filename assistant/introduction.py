""" basic AI Voice Assistance Introduction """
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client

# from client.textui import progress
# from ecapture import ecapture as ec
from bs4 import BeautifulSoup

# import win32com.client as wincl
from urllib.request import urlopen


class Assistant:
    def __init__(self) -> None:
        """
        setting up class variables
        """        
        self.engine = pyttsx3.init()
        self.assname = "Kakulugia"
        voice_type,language = self.get_male_female_voice()
        if voice_type :
            self.change_voice(language, voice_type)


    def get_male_female_voice(self):
        """
        ask voice type from user
        """        
        self.speak("Please select my voice type")
        self.speak("For male voice please say 1")
        self.speak("For female voice please say 2")
        voice_type = self.takeCommand()
        print("voice selection = ",voice_type.lower())
        if voice_type.lower() in ['1',"one","van","ban"]:
            return "VoiceGenderMale","en_GB"
        elif voice_type.lower() in ["two","2","tu","to"]:
            return "VoiceGenderFemale","en_IN"
        return None,None

    def change_voice(self, language, gender="VoiceGenderFemale"):
        for voice in self.engine.getProperty("voices"):
            print(voice)
            print("==>",language, voice.languages)
            print(f"logic {language in voice.languages} and {gender == voice.gender}")
            if language in voice.languages and gender == voice.gender:
                self.engine.setProperty("voice", voice.id)
                print(voice.name)
                self.assname = voice.name
                print(self.assname)
                return True
        self.speak("default Voice is selected")
        self.engine.setProperty("voice", self.engine.getProperty("voices")[0])
        return False

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def wish_me(self):
        """ 
        greet User and introduce itself
        """        
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speak("Good Morning!")
        elif hour >= 12 and hour < 16:
            self.speak("Good Afternoon !")
        else:
            self.speak("Good Evening !")

        self.speak("I am your Assistant")
        self.speak(f"you can address me as {self.assname}")

    def username(self):
        """ 
        Ask for name from User
        save user name and return username by Voice
        """        
        self.speak("What should i call you")
        self.uname = self.takeCommand()
        self.speak(f"Welcome {self.uname}")
        # self.speak()
        columns = shutil.get_terminal_size().columns

        print("#####################".center(columns))
        print(f"Welcome {self.uname}".center(columns))
        print("#####################".center(columns))

        self.speak("How can i Help you?")

    def takeCommand(self) -> str:
        """initiate voice read and convert the same to text

        Returns:
            str: voice msg converted to string
        """
        r = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source,timeout=15)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"

        return query

    def sendEmail(to, content):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        # Enable low security in gmail
        my_gmail_id = "test@test.com"
        server.login(my_gmail_id, "test123")
        server.sendmail(my_gmail_id, to, content)
        server.close()

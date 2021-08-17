'''speech triggered bot
Libraries used : For speech recognition- speech_recognition
For the text to speech function : pyttsx library
'''
'''
What's the outcome :
Can do web browsing
Play youtube videos
Get real time updates on whether, covid cases etc
'''
print("Your Converstion with the bot will be written to a file.What would you like the file name to be?")
filename=input()
with open(str(filename)+'.txt', 'a') as f:
    f.write('Conversation between bot and the user:\n\n')

import speech_recognition as sr
import pyttsx3 as p
from web_automation import *

from web_auto_wiki import *
from web_auto_utube import *
from web_auto_movie import *
from web_auto_recom import *

#Talk in between BOT and SPEAKER
r1=sr.Recognizer()
engine=p.init()
start="Hola User! How are you doing today?"
engine.say(start)
with open(str(filename)+'.txt', 'a') as f:
    f.write("BOT: "+start+"\n")
engine.runAndWait()
with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source)
    text = r1.listen(source)   #to get voice input
    #using google cloud API to recognize the voice
    try:
        query=r1.recognize_google(text)
        with open(str(filename)+'.txt', 'a') as f:
            f.write("USER: "+query+"\n")
    except sr.UnknownValueError :
        print("Google speech Recognition could not understand audio")
        with open(str(filename)+'.txt', 'a') as f:
            f.write("Google speech Recognition could not understand audio\n")
    except sr.RequestError :
        print("Couldnt get the result from google speech recognition")
        with open(str(filename)+'.txt', 'a') as f:
            f.write("Couldnt get the result from google speech recognition\n")
#BOT asking for instruction
cue="How can I help you?"
engine.say(cue)
with open(str(filename)+'.txt', 'a') as f:
    f.write("BOT: "+cue+"\n")
engine.runAndWait()
r2=sr.Recognizer()
with sr.Microphone() as source:
    r2.adjust_for_ambient_noise(source)
    instn= r2.listen(source)   #to get voice input for user's instruction 
    #using google cloud API to recognize the voice
    try:
        query2=r2.recognize_google(instn)
        print("Instruction is " + query2)
        with open(str(filename)+'.txt', 'a') as f:
            f.write("USER: "+query2+"\n")
    except sr.UnknownValueError :
        print("Google speech Recognition could not understand audio")
        with open(str(filename)+'.txt', 'a') as f:
            f.write("Google speech Recognition could not understand audio\n")
    except sr.RequestError :
        print("Couldnt get the result from google speech recognition")
        with open(str(filename)+'.txt', 'a') as f:
            f.write("Couldnt get the result from google speech recognition\n")
#Information from wikipedia
r3=sr.Recognizer()
if "information" in query2:
    engine.say("Information about what?")
    with open(str(filename)+'.txt', 'a') as f:
        f.write("BOT: "+"Information about what?"+"\n")
    engine.runAndWait()
    with sr.Microphone() as source:
        audio_wiki=r3.listen(source)
        try:
             information=r3.recognize_google(audio_wiki)
             bot=info()
             bot.get_info(information)
             
             with open(str(filename)+'.txt', 'a') as f:
                f.write("USER: "+information+"\n")
                f.write("BOT: Reading out information from wikipedia about "+information)
        except sr.UnknownValueError :
            print("Google speech Recognition could not understand audio")
            with open(str(filename)+'.txt', 'a') as f:
                f.write("Google speech Recognition could not understand audio\n")
        except sr.RequestError :
            print("Couldnt get the result from google speech recognition")
            with open(str(filename)+'.txt', 'a') as f:
                f.write("Couldnt get the result from google speech recognition\n")

#Music from youtube
r4=sr.Recognizer()
if "music" in query2:
    engine.say("Could you tell me the title of the music?")
    with open(str(filename)+'.txt', 'a') as f:
        f.write("BOT: "+"Could you tell me the title of the music?"+"\n")
    engine.runAndWait()
    with sr.Microphone() as source:
        title=r4.listen(source)
        try:
             song=r4.recognize_google(title)
             bot=music()
             bot.play_music(song)
             with open(str(filename)+'.txt', 'a') as f:
                f.write("USER: "+song+"\n")
                f.write("BOT: Playing the youtube song "+song+"...")
        except sr.UnknownValueError :
            print("Google speech Recognition could not understand audio.")
            with open(str(filename)+'.txt', 'a') as f:
                f.write("Google speech Recognition could not understand audio.\n")
        except sr.RequestError :
            print("Couldnt get the result from google speech recognition.")
            with open(str(filename)+'.txt', 'a') as f:
                f.write("Couldnt get the result from google speech recognition.\n")
#Movie Recommendation
r5=sr.Recognizer()
if "recommendation" in query2:
    engine.say("Here is the list of movies that are recommended for you to watch.")
    engine.runAndWait()
    with open(str(filename)+'.txt', 'a') as f:
        f.write("BOT: "+"Here is the list of movies that are recommended for you to watch."+"\n")
        f.write("BOT: "+"Showing the IMDb movie recommendations to the user"+"\n")

    bot=recom()
    bot.give_recom()

#Movie reviews
r6=sr.Recognizer()
if "review" in query2:
    engine.say("Could you tell me the name of the movie?")
    with open(str(filename)+'.txt', 'a') as f:
        f.write("BOT: "+"Could you tell me the name of the movie?"+"\n")
    engine.runAndWait()
    with sr.Microphone() as source:
        title=r6.listen(source)
        try:
             movies=r6.recognize_google(title)
             bot=movie()
             bot.movie_review(movies)
             with open(str(filename)+'.txt', 'a') as f:
                f.write("USER: "+movies+"\n")
                f.write("BOTShowing movies reviews for the movie "+movie+"...")
        except sr.UnknownValueError :
            print("Google speech Recognition could not understand audio.")
            with open(str(filename)+'.txt', 'a') as f:
                f.write("Google speech Recognition could not understand audio.\n")
        except sr.RequestError :
            print("Couldnt get the result from google speech recognition.")
            with open(str(filename)+'.txt', 'a') as f:
                f.write("Couldnt get the result from google speech recognition.\n")
    


# import pyttsx3
# import speech_recognition as sr
# from django.templatetags.i18n import language
# import pyaudio

# engine=pyttsx3.init('sapi5')
# voices=engine.getProperty("voices")
# engine.setProperty('voices',voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     print(audio)
#     engine.runAndWait()

# def takecommand():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening......")
#         r.pause_threshold =1
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source,timeout=3,phrase_time_limit=7)
#     try:
#         print("Recongning......")
#         query=r.recognize_google(audio,language='en-IN')
#         print(f"user said:{query}")
#     except sr.WaitTimeoutError:
#         print("Listening timed out while waiting for a phrase to start")
#         speak("Listening timed out, please try again.")
#         return "none"
#     except sr.UnknownValueError:
#         print("Sorry, I did not understand that.")
#         speak("Sorry, I did not understand that. Please say that again.")
#         return "none"
#     except sr.RequestError as e:
#         print(f"Could not request results from Google Speech Recognition service; {e}")
#         speak("Could not connect to the speech recognition service.")
#         return "none"
#     return query

# if __name__ == "__main__":
#     #speak("Hello Sir")
#     takecommand()




# from sys import exception

# import pyttsx3
# import speech_recognition as sr
# from django.contrib.admin.templatetags.admin_list import results
# from django.templatetags.i18n import language
# import pyaudio
# import datetime
# import os
# import cv2
# import random
# from requests import get
# import wikipedia
# import webbrowser
# import pywhatkit as kit
# import smtplib

# engine=pyttsx3.init('sapi5')
# voices=engine.getProperty("voices")
# engine.setProperty('voice',voices[0].id)

# #text to voice
# def speak(audio):
#     engine.say(audio)
#     print(audio)
#     engine.runAndWait()

# #to convert voice into text
# def takecommand():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening......")
#         r.pause_threshold =1
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source,timeout=5,phrase_time_limit=10)
#     try:
#         print("Recongning......")
#         query=r.recognize_google(audio,language='en-IN')
#         print(f"user said:{query}")
#     except sr.WaitTimeoutError:
#         print("Listening timed out while waiting for a phrase to start")
#         speak("Listening timed out, please try again.")
#         return "none"
#     except sr.UnknownValueError:
#         print("Sorry, I did not understand that.")
#         speak("Sorry, I did not understand that. Please say that again.")
#         return "none"
#     except sr.RequestError as e:
#         print(f"Could not request results from Google Speech Recognition service; {e}")
#         speak("Could not connect to the speech recognition service.")
#         return "none"
#     return query

# def wishs():
#     hour=int(datetime.datetime.now().hour)

#     if hour>=0 and hour<=12:
#         speak("Good Morning")
#     elif hour>12 and hour<18 :
#         speak("Good Afternoon")
#     else:
#         speak("Good Evening")

# def sendEmail(to,content):
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('annyabhudke@gmail.com','abc987654')
#     server.sendmail('annyabhudke@gmail.com',to,content)
#     server.close()

# if __name__ == "__main__":
#     #speak("Hello Sir")
#     wishs()
#     # while True:

#     query=takecommand().lower()

#     #logic building for task

#     if "open notepad" in query:
#         npath="C:\\Windows\\System32\\notepad.exe"
#         os.startfile(npath)
#     elif "open cmd" in query:
#         os.system("start cmd")
#     elif "open camera" in query:
#         cap=cv2.VideoCapture(0)
#         while True:
#             ret,img=cap.read()
#             cv2.imshow('webcam',img)
#             k=cv2.waitKey(50)
#             if k==27:
#                 break;
#         cap.release()
#         cv2.destroyAllWindows()

#         # elif "play music" in query:
#         #     music_dir="path"
#         #     songs=os.listdir(music_dir)
#          #    rd=random.choice(songs)
#          #      for song in songs:
#          #          if song.endswith('.mp3'):
#          #              os.startfile(os.path.join(music_dir,song))

#     elif "ip address" in query:
#         ip=get('https://api.ipify.org').text
#         speak(f"your IP address is {ip}")

#     elif "wikipedia" in query:
#         speak("searching wikipedia......")
#         query=takecommand().lower()
#         try:
#             if query:
#                 search_results = wikipedia.search(query)
#                 if search_results:
#                     top_result=search_results[0]
#                     speak(f"Showing results for {top_result}")
#                     results =wikipedia.summary(top_result,sentences=2)
#                     speak("according to wikipedia")
#                     speak(results)
#                     print(results)
#                 else:
#                     speak("Sorry, I couldn't find any results on Wikipedia.")
#             else:
#                 speak("please specify what you want on wikipedia.")
#         except wikipedia.exceptions.DisambiguationError as e:
#             speak("There are multiple results for your search. Please specify further.")
#         except wikipedia.exceptions.PageError:
#             speak("The page does not exist on Wikipedia.")
#         except Exception as e:
#             speak(f"An error occurred: {str(e)}")

#     elif "open youtube" in query:
#         webbrowser.open("https://www.youtube.com")

#     elif "open facebook" in query:
#         webbrowser.open("https://www.facebook.com")

#     elif "open google" in query:
#         speak("sir, what Should i search on google")
#         cm=takecommand().lower()
#         webbrowser.open(f"{cm}")

#     elif "send message" in query:
#         try:
#             # Define the recipient's phone number in correct format (without '+')
#             phone_number = "+917776819028"  # Replace with the recipient's phone number

#             # Message to send
#             message = "This is a testing protocol"

#             # Time to send the message
#             current_time = datetime.datetime.now()
#             hour = current_time.hour
#             minute = current_time.minute + 2  # Scheduling 2 minutes ahead

#             # Send the message using pywhatkit
#             kit.sendwhatmsg(phone_number, message, hour, minute)

#             print(f"Message sent successfully to {phone_number} at {hour}:{minute}")

#         except Exception as e:
#             print(f"An error occurred: {str(e)}")

#     elif " songs youtube" in query:
#         kit.playonyt("see you again")

#     elif "email" in query:
#         try:
#             speak("What should i say?")
#             content=takecommand().lower()
#             to="nagre.gajanan777@gmail.com"
#             sendEmail(to,content)
#             speak("Email has been sent successfully..!")
#         except Exception as e:
#             print(e)
#     elif "no thanks" in query:
#         speak("thanks for using me sir,have a good day.")
#         sys.exit()

    
#date-27-2-2025
# from sys import exception

# import pyttsx3
# import speech_recognition as sr
# from django.contrib.admin.templatetags.admin_list import results
# from django.templatetags.i18n import language
# import pyaudio
# import datetime
# import os
# import cv2
# import random
# from requests import get
# import wikipedia
# import webbrowser
# import pywhatkit as kit
# import smtplib

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty("voices")
# engine.setProperty('voice', voices[0].id)


# # text to voice
# def speak(audio):
#     engine.say(audio)
#     print(audio)
#     engine.runAndWait()


# # to convert voice into text
# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening......")
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source, timeout=5, phrase_time_limit=10)
#     try:
#         print("Recongning......")
#         query = r.recognize_google(audio, language='en-IN')
#         print(f"user said:{query}")
#     except sr.WaitTimeoutError:
#         print("Listening timed out while waiting for a phrase to start")
#         speak("Listening timed out, please try again.")
#         return "none"
#     except sr.UnknownValueError:
#         print("Sorry, I did not understand that.")
#         speak("Sorry, I did not understand that. Please say that again.")
#         return "none"
#     except sr.RequestError as e:
#         print(f"Could not request results from Google Speech Recognition service; {e}")
#         speak("Could not connect to the speech recognition service.")
#         return "none"
#     return query


# def wishs():
#     hour = int(datetime.datetime.now().hour)

#     if hour >= 0 and hour <= 12:
#         speak("Good Morning")
#     elif hour > 12 and hour < 18:
#         speak("Good Afternoon")
#     else:
#         speak("Good Evening")


# def sendemail(tos, contents):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('annyabhudke@gmail.com', 'jsfk cvug fjij vzju')
#     server.sendmail('annyabhudke@gmail.com', tos, contents)
#     server.close()


# if __name__ == "__main__":
#     # speak("Hello Sir")
#     wishs()
#     while True:

#         query = takecommand().lower()

#     # logic building for task

#         if "open notepad" in query:
#             npath = "C:\\Windows\\System32\\notepad.exe"
#             os.startfile(npath)
#         elif "open cmd" in query:
#             os.system("start cmd")
#         elif "open camera" in query:
#             cap = cv2.VideoCapture(0)
#             while True:
#                 ret, img = cap.read()
#                 cv2.imshow('webcam', img)
#                 k = cv2.waitKey(50)
#                 if k == 27:
#                     break;
#             cap.release()
#             cv2.destroyAllWindows()

#         # elif "play music" in query:
#         #     music_dir="path"
#         #     songs=os.listdir(music_dir)
#         #    rd=random.choice(songs)
#         #      for song in songs:
#         #          if song.endswith('.mp3'):
#         #              os.startfile(os.path.join(music_dir,song))

#         elif "ip address" in query:
#             ip = get('https://api.ipify.org').text
#             speak(f"your IP address is {ip}")

#         elif "wikipedia" in query:
#             speak("searching wikipedia......")
#             query = takecommand().lower()
#             try:
#                 if query:
#                     search_results = wikipedia.search(query)
#                     if search_results:
#                         top_result = search_results[0]
#                         speak(f"Showing results for {top_result}")
#                         results = wikipedia.summary(top_result, sentences=2)
#                         speak("according to wikipedia")
#                         speak(results)
#                         print(results)
#                     else:
#                         speak("Sorry, I couldn't find any results on Wikipedia.")
#                 else:
#                     speak("please specify what you want on wikipedia.")
#             except wikipedia.exceptions.DisambiguationError as e:
#                 speak("There are multiple results for your search. Please specify further.")
#             except wikipedia.exceptions.PageError:
#                 speak("The page does not exist on Wikipedia.")
#             except Exception as e:
#                 speak(f"An error occurred: {str(e)}")

#         elif "open youtube" in query:
#             webbrowser.open("https://www.youtube.com")

#         elif "open facebook" in query:
#             webbrowser.open("https://www.facebook.com")

#         elif "open google" in query:
#             speak("sir, what Should i search on google")
#             cm = takecommand().lower()
#             webbrowser.open(f"{cm}")

#         elif "send message" in query:
#             try:
#                 # Define the recipient's phone number in correct format (without '+')
#                 phone_number = "+917776819028"  # Replace with the recipient's phone number

#             # Message to send
#                 message = "This is a testing protocol"

#             # Time to send the message
#                 current_time = datetime.datetime.now()
#                 hour = current_time.hour
#                 minute = current_time.minute + 2  # Scheduling 2 minutes ahead

#             # Send the message using pywhatkit
#                 kit.sendwhatmsg(phone_number, message, hour, minute)

#                 print(f"Message sent successfully to {phone_number} at {hour}:{minute}")

#             except Exception as e:
#                 print(f"An error occurred: {str(e)}")

#         elif " songs youtube" in query:
#             kit.playonyt("see you again")

#         elif "email" in query:
#             try:
#                 speak("What should i say?")
#                 content = takecommand().lower()
#                 to = "bhudkea@gmail.com"
#                 sendemail(to, content)
#                 speak("Email has been sent successfully..!")
#             except Exception as e:
#                 print(e)
#         elif "no thanks" in query:
#             speak("thanks for using me sir,have a good day.")
#             sys.exit()

#             speak('Do you want any')


#date=28-02-2024

from sys import exception

import pyttsx3
import speech_recognition as sr
from django.contrib.admin.templatetags.admin_list import results
from django.templatetags.i18n import language
import pyaudio
import datetime
import os
import cv2#camera sathi aahe
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


# text to voice
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=3, phrase_time_limit=7)
    try:
        print("Recongning......")
        query = r.recognize_google(audio, language='en-IN')
        print(f"user said:{query}")
    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for a phrase to start")
        speak("Listening timed out, please try again.")
        return "none"
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that. Please say that again.")
        return "none"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("Could not connect to the speech recognition service.")
        return "none"
    return query

#according time you can wish
def wishs():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")


def sendemail(tos, contents):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('annyabhudke@gmail.com', 'jsfk cvug fjij vzju')
    server.sendmail('annyabhudke@gmail.com', tos, contents)
    server.close()


if __name__ == "__main__":
    # speak("Hello Sir")
    wishs()
    # while True:

    query =takecommand().lower()

    # logic building for task

    if "open notepad" in query:
        npath = "C:\\Windows\\System32\\notepad.exe"
        os.startfile(npath)

    elif "open cmd" in query:
        os.system("start cmd")

    elif "open camera" in query:
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(50)
            if k == 27:
                break;
        cap.release()
        cv2.destroyAllWindows()

        # elif "play music" in query:
        #     music_dir="path"
        #     songs=os.listdir(music_dir)
        #    rd=random.choice(songs)
        #      for song in songs:
        #          if song.endswith('.mp3'):
        #              os.startfile(os.path.join(music_dir,song))

    elif "ip address" in query:
        ip = get('https://api.ipify.org').text
        speak(f"your IP address is {ip}")

    elif "wikipedia" in query:
        speak("searching wikipedia......")
        query = takecommand().lower()
        try:
            if query:
                search_results = wikipedia.search(query)
                if search_results:
                    top_result = search_results[0]
                    speak(f"Showing results for {top_result}")
                    results = wikipedia.summary(top_result, sentences=5)
                    speak("according to wikipedia")
                    speak(results)
                    print(results)
                else:
                    speak("Sorry, I couldn't find any results on Wikipedia.")
            else:
                speak("please specify what you want on wikipedia.")
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results for your search. Please specify further.")
        except wikipedia.exceptions.PageError:
            speak("The page does not exist on Wikipedia.")
        except Exception as e:
            speak(f"An error occurred: {str(e)}")

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in query:
        webbrowser.open("https://www.facebook.com")

    elif "open google" in query:
        speak("sir, what Should i search on google")
        cm = takecommand().lower()
        webbrowser.open(f"{cm}")

    elif "send message" in query:
        try:
            # Define the recipient's phone number in correct format (without '+')
            phone_number = "+917776819028"  # Replace with the recipient's phone number

            # Message to send
            message = "This is a testing protocol"

            # Time to send the message
            current_time = datetime.datetime.now()
            hour = current_time.hour
            minute = current_time.minute + 2  # Scheduling 2 minutes ahead

            # Send the message using pywhatkit
            kit.sendwhatmsg(phone_number, message, hour, minute)

            print(f"Message sent successfully to {phone_number} at {hour}:{minute}")

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    elif " songs youtube" in query:
        kit.playonyt("see you again")

    elif "mail" in query:
        try:
            speak("What should i say?")
            content = takecommand().lower()
            to = "sanikawaghmare813@gmail.com8"
            sendemail(to, content)
            speak("Email has been sent successfully..!")
        except Exception as e:
            print(e)
    elif "no thanks" in query:
        speak("thanks for using me sir,have a good day.")
        sys.exit()

    elif "close notepad" in query:
        speak("Okay sir ,plz wait closing notepad")
        os.system("C:\\Windows\\System32\\notepad.exe")

    elif "set alarm " in query:
        nn=int(datetime.datetime.now().hour)
        if nn==22:
            music_dir="C:\\Users\\bhudk\\Music"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

    speak('Do you want to other work')


















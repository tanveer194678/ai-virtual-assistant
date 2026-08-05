import speech_recognition as sr
import pywhatkit
import pyttsx3                                     # Python text to speech library
import datetime
import webbrowser
import wikipedia

engine = pyttsx3.init()                             # Initiating the engine | engine is object
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
recognizer = sr.Recognizer()                        # Initiating the speech recoganization library

currassistant = 0                                    # If 1 then Feamle, else if 0 then Male
currcommand = ''

def Fun():
    global currassistant
    global command                                   # Declare command as global here
    go = True
    count = 1
    command = ''                                      # Initialize command here
    while go:
        with sr.Microphone() as source:
            if count == 1:
                engine.say('\n How Can I Help You .... \n')
                engine.runAndWait()
                print('\n How Can I Help You ? \n')
                count += 1

            elif count == -1:
                engine.say('Sorry . Can you repeat please  ')
                engine.runAndWait()
                print('\n Sorry . Can you repeat please  \n')

            else:
                count += 1
                engine.say('Are you satisfied with the result')
                engine.runAndWait()
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                currenrec = recognizer.listen(source)

                try:
                    currcommand = recognizer.recognize_google(currenrec, language='en_US')
                    currcommand = currcommand.lower()
                    print('Searching Result:', format(currcommand))

                except Exception as ex:
                    print(ex)

                if 'yes' in currcommand:
                    engine.say("Yay")
                elif 'no' in currcommand:
                    engine.say("Sorry for the inconvenience.....")

                engine.runAndWait()
                engine.say('What to do next? ')
                engine.runAndWait()

            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recordedaudio = recognizer.listen(source)
            print('Done recording')

        try:
            command = recognizer.recognize_google(recordedaudio, language='en_US')
            command = command.lower()
            print('Your message: ', format(command))

        except Exception as ex:
            print(ex)

        if 'lms' in command:
            c = 'Opening LMS'
            engine.say(c)
            engine.runAndWait()
            webbrowser.open('https://staloysius.edu.in/')

        elif 'amazon' in command:
            c = 'Opening Amazon'
            engine.say(c)
            engine.runAndWait()
            webbrowser.open('https://www.amazon.in/')

        elif 'google' in command:
            c = 'Opening Google'
            engine.say(c)
            engine.runAndWait()
            webbrowser.open('www.google.com')

        elif 'ticket' in command or 'movie' in command:
            c = 'Opening Bookmyshow'
            engine.say(c)
            engine.runAndWait()
            webbrowser.open('https://in.bookmyshow.com/explore/home/ahmedabad')

        elif 'play' in command:
            a = 'opening youtube..'
            engine.say(a)
            engine.runAndWait()
            pywhatkit.playonyt(command)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            engine.say(time)
            engine.runAndWait()

        elif 'youtube' in command:
            b = 'opening youtube'
            engine.say(b)
            engine.runAndWait()
            webbrowser.open('www.youtube.com')

        elif 'bank' in command:
            c = 'Opening HDFC Bank Netbanking'
            engine.say(c)
            engine.runAndWait()
            webbrowser.open('https://www.hdfcbank.com/')

        elif 'name' in command:                                            # Name of Voice Assistant
            if currassistant == 0:
                engine.say("I am John Your Virtual Assistant")
            else:
                engine.say("I am Luci your Virtual Assistant")
            engine.runAndWait()

        elif 'assistant' in command:                                      # Change Voice Assistant
            if currassistant == 0:
                currassistant = 1
            else:
                currassistant = 0
            engine.setProperty('voice', voices[currassistant].id)
            engine.say("Changes applied")

        elif 'exit' in command:                                     # Exit voice assistant
            go = False

        elif 'search' in command:                                   # Searching on WikiPedia
            try:    
                #print('Printing your message...Please wait')
                text = recognizer.recognize_google(recordedaudio, language='en-US')
                # print('Your Message:{}', format(text))
            except Exception as ex:
                print(ex)

            wikisearch = wikipedia.summary(text)
            val = wikisearch.split(".")
            engine.say(val[0])
            engine.runAndWait()

        else:
            count = -1


while True:                 # function call

    print("\n")
    print("---------------------------------------")
    print("|                                     |")
    print("|  1 - Connect to Assistant           |")
    print("|  2 - Exit                           |")
    print("|                                     |")
    print("--------------------------------------")
    print("\n")
    userinput = int(input("Enter your input :- "))
    if userinput == 1:
        Fun()
    elif userinput == 2:
        break


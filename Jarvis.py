import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 170)
engine.setProperty('voice', voices[0].id)


def talk(text,pause_duration =0.2):
    engine.say(text)
    engine.runAndWait()
    time.sleep(pause_duration)

def extract_person(query):
    # Assuming the query structure is "information about [person]"
    # Extracting the person's name after "information about"
    keyword = 'information about'
    index = query.find(keyword)
    if index != -1:
        person = query[index + len(keyword):].strip()
        return person
    else:
        return None


def take_command():
    try:
        talk("Hey, I am Jarvis. How may I help you,sir?")
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            query = listener.recognize_google(voice)
            query = query.lower()
            print(query)
            return(query)





    except Exception as e:
        print(f"An error occurred: {e}")
        query = ""  # Set query to an empty string in case of an error
    return query


def run_jarvis():
    try:
        query = take_command()
        if 'play' in query:
            song = query.replace('play', '').strip()
            print("I am Playing the song for you, Sir")
            talk('I am playing the song for you sir ' )
            pywhatkit.playonyt(song)
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Right now it is'+ time + 'Sir')
        elif 'information' in query:
            person = extract_person(query)
            if person:
                info = wikipedia.summary(person,2)
                print(info)
                talk('Here is the Information Sir', pause_duration=0.2)
                talk(info)
        elif 'date' in query:
            current_date = datetime.datetime.now().strftime('%d %B %Y')
            print(current_date)
            talk(f"Today's date is {current_date}, sir.")
        elif 'open' in query:
            website_keywords = {'google':'https://www.google.com/',
                                'youtube':'https://www.youtube.com/',
                                'linkedin':'https://www.linkedin.com/feed/',
                                'instagram':'https://www.instagram.com/',
                                'whatsapp':'https://web.whatsapp.com/',
                                'jiocinema':'https://www.jiocinema.com/',
                                'gmail':'https://mail.google.com/mail/u/0/#inbox'}
            opened_website = None

            for keyword in website_keywords:
                if keyword in query:
                    opened_website = keyword
                    break
            if opened_website:
                print(f"I am opening {opened_website} for you,sir")
                talk(f"I am opening {opened_website} for you,sir")
                webbrowser.open(website_keywords[opened_website])
        elif 'take rest' in query:
            print('Goodbye Sir! Jarvis is Taking rest')
            talk('Goodbye Sir! Jarvis is Taking rest')




    except Exception as e:
        print(f"An error occurred: {e}")

run_jarvis()

'''while True:
    query = take_command()
    run_jarvis()

    if 'take rest' in query:
        print('Goodbye Sir! Jarvis is Taking the rest')
        talk('Goodbye Sir! Jarvis is Taking the rest')
        break'''

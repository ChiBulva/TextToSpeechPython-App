# Get the first 5 hits for "google 1.9.1 python" in Google Pakistan
#from googlesearch import search
import os
import speech_recognition as sr

def PrintBox(sentence, phrase):
    print("________________________________")
    print("|                               |")
    print("|    "+str(phrase)+": "+str(sentence))
    print("|_______________________________|")

def GetSpeechToText(r, source):
    while(True):
        print("> Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)

			#print("You said : {}".format(text))
            if('print' in text.lower()):
                text = text.lower().replace('print ', '')
                print(text)

            elif('exit' in text.lower()):
                text = "Thank you for Trying... exiting the Tool!!"
                PrintBox(text, '')
                return 'exit'

            elif('call' in text.lower()):
                text = text.lower().replace('call ', '')
                text = "Add call function here()"
                PrintBox(text, 'Calling!!!!')


            elif('Google' in text.lower()):
                text = text.lower().replace('Google ', '')
                print("Googleing Disabled...")
                #for url in search(text, tld='com.pk', lang='es', stop=5):
                #    print(url)

            elif('open' in text.lower()):
                text = text.lower().replace('open ', '')
                #ProgramList = os.listdir(r'C:\Users\User\Desktop\SpeechTpTextApp\Commands\OpenShortcuts')
                text = text.replace(' ', '')
                #Finaltext = text

                try:
                    Finaltext = text + ".lnk"
                    print("opening -> " + str(Finaltext.lower()))
                    open = r'C:\Users\User\Desktop\SpeechTpTextApp\Commands\OpenShortcuts\\ '+str(Finaltext.lower())
                    open = open.replace('\ ', '')
                    print(open)
                    os.startfile(open)
                except:
                    trial = 1

                if(trial==1):
                    try:
                        Finaltext = text + ".bat"
                        print("opening -> " + str(Finaltext.lower()))
                        open = r'C:\Users\User\Desktop\SpeechTpTextApp\Commands\OpenShortcuts\\ '+str(Finaltext.lower())
                        open = open.replace('\ ', '')
                        print(open)
                        os.system(open)
                    except:
                        print("Nothing found"
                        )
            elif('new open' in text.lower()):
                text = text.lower().replace('new open ', '')

                #if('print' in text):
                print("new open")


            else:
                #Prints Line that was just read into the machine.
                #
                PrintBox(text, 'You said')

            return(text)

        except:
            print("> Sorry could not recognize what you said")
            #open = r'C:\Users\User\Desktop\SpeechTpTextApp\Commands\OpenShortcuts\\ '+str(text)
            #open = open.replace('\ ', '')
            #print(open)


def SpeechToCodeModule():
    #TODO: 1. get voice
    #TODO: 2. eval
    #

    r = sr.Recognizer()

    with sr.Microphone() as source:
        while(True):
            #Get Speech to Text
            text = GetSpeechToText(r, source)
            if(text=='exit'):
                return(0)


def main():
    SpeechToCodeModule()

main()

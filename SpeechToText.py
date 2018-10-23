# Get the first 5 hits for "google 1.9.1 python" in Google Pakistan
from googlesearch import search
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
            if('print' in text):
                text = text.replace('print ', '')
                print(text)

            elif('exit' in text):
                text = "Thank you for Trying... exiting the Tool!!"
                PrintBox(text, '')
                return 'exit'

            elif('call' in text):
                text = text.replace('call ', '')
                text = "Add call function here()"
                PrintBox(text, 'Calling!!!!')

				
            elif('Google' in text):
                text = text.replace('Google ', '')
                print("Googleing...")
                for url in search(text, tld='com.pk', lang='es', stop=5):
                    print(url)

            else:
                #Prints Line that was just read into the machine.
                #
                PrintBox(text, 'You said')			
            
            return(text)
                        
        except:
            print("> Sorry could not recognize what you said")

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

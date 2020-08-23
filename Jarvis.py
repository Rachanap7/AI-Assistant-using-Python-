import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import wikipedia
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

def speak(audio):	
	engine.say(audio)
	engine.runAndWait()

def time():
	time = datetime.datetime.now().strftime("%I:%M:%S")
	speak(time)

def date():
	year = (datetime.datetime.now().year)
	month = (datetime.datetime.now().month)
	date = (datetime.datetime.now().day)
	speak("todays date is")
	speak(date)
	speak(month)
	speak(year)

def greetings():
	speak("Hello there, welcome")
	
	hour =  datetime.datetime.now().hour

	if hour>= 6 and hour<12:
		speak("good morning have a nice day")
	elif hour>=12 and hour<16:
		speak("good afternoon")
	elif hour>=16 and hour<=24:
		speak("good evening")
	else:
		speak("good night")
	

	speak("How can I help you")

def mail(to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("rachana.parkar711@gmail.com","R@p_192667")
        server.sendmail("parkar.rachana@gmail.com",to,content)
        server.close()

def ss():
        image = pyautogui.screenshot()
        image.save("C:\\Users\\Rachana Parkar\\Desktop\\Jarvis\\image.png")

def cpuinfo():
        usage = str(psutil.cpu_percent())
        speak("cpu is at"+usage)
        battery = psutil.sensors_battery()
        speak("battery is at")
        speak(battery.percent)

def telljokes():
        speak(pyjokes.get_joke())

def usercommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

        try:
                print("Recognizing...")
                command = r.recognize_google(audio,language='en-US')
                print(command)
        except Exception as e:
                print(e)
                print("Can you please say that again")

                return "None"
        return command

if __name__ == "__main__":
        greetings()

        while True:
                query = usercommand().lower()
                print(query)

                if "time" in query:
                        time()
                elif "date" in query:
                        date()
                elif "offline" in query:
                        speak("Good bye")
                        quit()
                elif "wikipedia" in query:
                        speak("Searching...")
                        query = query.replace("wikipedia","")
                        result = wikipedia.summary(query, sentences = 2)
                        speak(result)
                elif "send email" in query:
                        try:
                                speak("what should i say?")
                                content = usercommand()
                                to = "parkar.rachana@gmail.com"
                                mail(to,content)
                                speak("mail sent successfully")
                        except Exception as e:
                                speak(e)
                                speak("sorry unable to send")
                elif "search in chrome" in query:
                        speak("what should i search")
                        search = usercommand().lower()
                        chromepath ="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
                        #wb.register('chrome', None,wb.BackgroundBrowser(chromepath))
                        wb.get(chromepath).open_new_tab(search+ ".com")

                elif "logout" in query:
                        os.system("shutdown - l")
                        
                elif "shutdown" in query:
                        os.system("shutdown /s /t 1")

                elif "restart" in query:
                        os.system("shutdown /r /t 1")

                elif "play songs" in query:
                        songsdir = "D:\MyMusic"
                        songs= os.listdir(songsdir)
                        os.startfile(os.path.join(songsdir,songs[0]))
                elif "remember this" in query:
                        speak("what should i remember")
                        data = usercommand()
                        speak("you said me to remember" +data)
                        text = open("content.txt",'w')
                        text.write(data)
                        text.close()
                elif "do you remember anything" in query:
                        text = open("content.txt","r")
                        speak("you said me to remember that" +text.read())
                elif "screenshot" in query:
                        ss()
                        speak("screenshot saved succssfully")
                elif "cpu" in query:
                        cpuinfo()
                elif "jokes" in query:
                        telljokes()
                
                        
                
                
        

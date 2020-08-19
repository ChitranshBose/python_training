import pyttsx3 as py
import os
ch="y" 
while ch=="y"or ch=="yes":
    py.speak("enter the task")
    p=input("enter the task.....").lower()
    if (("run" in p or "execute" in p or "open" in p) and ("editor" in p or "writing editor" in p or"notepad" in p)):
        if "notepad" in p:
            py.speak("opening notepad")
            os.system("notepad")
        else:
            py.speak("which editor you want to open? sublime or notepad")
            p1=input("name of editor: \n")
            py.speak("opening"+ p1)
            if "sublime" in p1:
                os.system("sublime_text")
            elif "notepad" in p1:
                os.system("notepad")
    elif (("run" in p or "execute" in p or "open" in p) and ("music player" in p or "media player" in p or "video player" in p)):
        py.speak("which media player you want to open? vlc or windows media player")
        p1=input("name of media player: \n")
        py.speak("opening"+p1)
        if "wmplayer" in p1 or "windows" in p1:
            os.system("wmplayer")
        elif "vlc" in p1:
            os.system("vlc")
    elif (("run" in p or "execute" in p or "open" in p) and ("chrome" in p or "browser" in p)):
        if "chrome" in p:
            py.speak("opening chrome")
            os.system("chrome")
        else:
            py.speak("which browser you want to open? chrome, firefox or edge")
            p1=input("name of browser: \n")
            if "chrome" in p1:
                py.speak("opening chrome")
                os.system("chrome")
            elif "firefox" in p1 or "fire fox" in p1:
                py.speak("opening firefox")
                os.system("firefox")
            elif "edge" in p1:
                py.speak("opening edge")
                os.system("msedge")
    elif(("run" in p or "execute" in p or "open" in p) and ("eclipse" in p )):
        py.speak("opening eclipse")
        os.system("eclipse")
    elif(("run" in p or "execute" in p or "open" in p) and ("anydesk" in p)):
        py.speak("opening anydesk")
        os.system("AnyDesk")
    elif(("run" in p or "execute" in p or "open" in p) and ("power point" in p or "ppt" in p or "power pnt" or "powerpoint" in p)):
        py.speak("opening power point ")
        os.system("powerpnt")
    elif(("run" in p or "execute" in p or "open" in p) and ("word" in p or "winword" in p or "ms word")):
        py.speak("opening word")
        os.system("winword")
    
    elif(("run" in p or "execute" in p or "open" in p) and ("note" in p or "onenote" in p or "one note" in p)):
        py.speak("opening one note") 
        os.system("onenote")
    elif(("run" in p or "execute" in p or "open" in p) and ("excel" in p)):
        py.speak("opening excel")
        os.system("excel")     
    else:
        py.speak(" your choice is invalid try again!!")
    py.speak("you want to continue?")
    ch=input("Yes or No? \n").lower().strip()
py.speak("Program closing. Have a good day!!"); 
    

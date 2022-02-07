import datetime
import requests
import urllib.request

class Time:
    def Time24hr():
        return datetime.datetime.now().strftime("%H:%M:%S")
    
    def Time12hr():
        AMPM = ''
        Hour = None
        Minute = datetime.datetime.now().strftime("%M")
        Second = datetime.datetime.now().strftime("%S")

        if int(datetime.datetime.now().strftime("%H")) > 12:
            AMPM = 'PM'
            Hour = int(datetime.datetime.now().strftime("%H")) - 12
        else:
            AMPM = 'PM'
            Hour = datetime.datetime.now().strftime("%H")

        return f"{Hour}:{Minute}:{Second} {AMPM}"
    
    def Timecheck(time, selection):
        if selection.lower() == "h" or "m" or "s":
            return str(time) == datetime.datetime.now().strftime(f"%{str(selection.upper())}")

        elif selection.lower() == "m":
            return str(time) == datetime.datetime.now().strftime("%M")

        elif selection.lower() == "s":
            return str(time) == datetime.datetime.now().strftime("%S")

        elif selection.lower() == "hm":
            return str(time) == datetime.datetime.now().strftime("%H:%M")

        elif selection.lower() == "hms":
            return str(time) == datetime.datetime.now().strftime("%H:%M:%S")

class Post:
    def Websiteping(website):
        return urllib.request.urlopen(website).getcode()

    def Discord_webhook(url, msg):
        Message = {"content": f"{str(msg)}"}
        try:
            requests.post(str(url), data=Message)
            return "Message succesfully sent."
        except requests.exceptions.ConnectionError as error:
            return "ERROR: Please connect to the internet."
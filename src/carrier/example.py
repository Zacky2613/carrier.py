import carrier
import time

while True:
    if carrier.Timecheck("22:30", "HM") == True: 
        print("It is 22:30 aka 10:30 PM.")
        exit()
    else:
        print("It is not 22:30 aka 10:30PM.")
    
    time.sleep(1) 
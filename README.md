# carrier.py
carrier.py is a Python package/module that's used to save time when programming, it helps with functions such as 24 and 12 hour time, Discord webhooks, etc. These are all mainly things that I've been annoyed by because I keep forgetting the code and so I've just bundle it up into carrier.py 

# Version
carrier.py is currently in 0.0.2 -change some function names to be more snake case.

# Installation
You will need Python 3.6+

```
# Linux/macOS
python3 -m pip install carrier.py==0.0.2

# Windows
py -3 -m pip install carrier.py==0.0.2
```

# Example
```py
import carrier
import time

while True:
    if carrier.Timecheck("22:30", "HM") == True: 
        print("It is 22:30 aka 10:30 PM.")
        exit()
    else:
        print("It is not 22:30 aka 10:30PM.")
    
    time.sleep(1) 
```

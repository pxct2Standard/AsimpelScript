from datetime import datetime
import time
import os

while True:
    zeit_unformatet = datetime.now()
    zeit_formatet = zeit_unformatet.strftime("%H:%M")
    print(zeit_formatet)

    if zeit_formatet == '11:45':
        print("Achtung in 5 Min acht geben!")
    elif zeit_formatet == '11:50':
        print("Du must jetzt aufpassen")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif zeit_formatet == '18:05':
        print("Achtung in 5 Min acht geben!")
    elif zeit_formatet == "18:10":
        print("Du must jetzt aufpassen")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    time.sleep(60)
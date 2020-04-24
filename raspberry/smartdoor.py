import serial
import time
import threading
import os

port = "/dev/ttyACM0"

lastData = ""
lastDistance = 0
beforeDistance = 0
currentDistance = 0

print("[INFO] Starting serial monitor...")
arduino = serial.Serial(port, 9600)
time.sleep(1)

def monitor():

    global lastData, arduino

    time.sleep(1)

    while True:
        rawString = arduino.readline()
        lastData = rawString.decode().replace("\n", "")


def printer():
    global lastData, lastDistance, beforeDistance, currentDistance

    time.sleep(1)

    while True:
        print(lastData)
        if (lastData != ""):
            scrapedData = int(lastData.replace("Distance: ", ""))
            if (scrapedData >= 5):
                lastDistance = scrapedData
        if (beforeDistance != lastDistance):
            if (beforeDistance - lastDistance <= 5):
                currentDistance = lastDistance
                print("[INFO] New Distance: " + str(currentDistance))
                os.system("sudo echo " + str(currentDistance) + " >> /var/www/html/distances.txt")
        beforeDistance = lastDistance
        time.sleep(0.1)


def closer():

    global arduino

    input()
    input()
    input()


    print("[INFO] Closing serial and exiting...")
    arduino.close()
    os._exit(1)

threading.Thread(target=monitor).start()
print("[INFO] Started monitor thread")
threading.Thread(target=printer).start()
print("[INFO] Started printer thread")
threading.Thread(target=closer).start()
print("[INFO] Started closer thread")
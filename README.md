# SmartDoor
SmartDoor using arduino + raspberry pi

## Physical Setup
I used a RaspberryPi Zero W and an Arduino Mega to set it up:
![Circuit Setup](setup/circuit.png)
![Door Setup](setup/scheme.png)

## How to Setup
First you'll have to upload the arduino program on the arduino folder to your arduino.
Yen you can use this commands to set it up.
```shell
git clone https://github.com/iByNiki/SmartDoor/
cd SmartDoor
chmod -R 777 *
sudo apt-get install python3
python3 -m pip3 install PySerial
sudo apt-get install apache2
sudo apt-get install php libapache2-mod-php
cd website
mv * /var/www/html/
cd ../raspberry
screen -S SmartDoor
python3 smartdoor.py
```

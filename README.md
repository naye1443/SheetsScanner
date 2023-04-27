# Raspberry pi HID magstrip scanner

## Project Description
---

This script reads HID magstrip data then stores append the data onto a google sheet. 

## How to setup
---

- Firstly, create a new google sheet or use an already existing one.

- Create a service account or use an already existing service account. Make sure when you create the service account to share to it on the google sheet. You have to share the sheet with the service account email for it to have access to read and write to it.

- Take the .env file and change the needed params to fit the new google sheet.

- retrieve the .json key from the GCP console and store in project directory.

- upload these three files to the raspberrypi
    - credentials.json
    - test.py
    - requirements.txt
    - .env
    - README.md (incase you need later)

- ssh into raspberrypi and install python3 and needed dependencies from requirements.txt

- store command to run script into .bashrc file so that the script starts when the raspberry pi starts.


## Commands to help navigate raspberry pi
---

to shh into raspberry from local computer use command 
> ```ssh ${username}@${Ipaddress}}```

to send a file from local computer to raspberry using scp use command

> ```scp ${filename} ${username}@${Ipaddress}:/home/${username}```

when installing python packges uses ```sudo``` before pip.
unsure of why this is needed.

### Authentication
---

To authenticate to google spreadsheets a service account is used. Hence, if credentials need to be upgraded create a new service account and then create a service account file. Rename service account file to credentials.json.

more details on how to authenticate [here](https://denisluiz.medium.com/python-with-google-sheets-service-account-step-by-step-8f74c26ed28e)

## pinlayout
---

![alt text](./RasPiB-GPIO_reference.png)

command ```pinout``` prints all GPIO pins on arduino

### pizo Buzzer
---

- GPIO15 (pin 10) -> VCC
- GND (pin 6) -> Ground

used GPIO 15 instead of 14. This is because GPIO 14 is a TX pin and is set to high durring boot sequence. Hence, using GPIO 15 (RX) instead as pizo buzzer positive.

### RGBLED
---

- GPIO2 (pin 3) -> GREEN for LED
- GPIO3 (pin 5) -> RED for LED
- GPIO4 (pin 7) -> BLUE for LED
- GND (pin 39) -> Ground for LED

### Hostnames for SSH:
---

- Unmarked = 10.12.165.35

### Username and password to account
---
Will be on google doc's sheet 

### possible problems
---

You have to add the command ```python3 test.py``` to the end of the .bashrc file. This is so when the raspberry pi starts up. It starts the program. You HAVE to use ```python3```. This is because ```python``` does not support ```input()``` or the dotenv pacakge.
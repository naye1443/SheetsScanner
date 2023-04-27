import pickle
from os import path
import os
from datetime import datetime
import time

# Authenticaion
from googleapiclient import discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from os import popen

# imports env variables
from dotenv import load_dotenv

# GPIO
import RPi.GPIO as GPIO
# using Revision 3 \\ https://elinux.org/RPi_HardwareHistory

# load env variables into scope
load_dotenv()


class Sheets_Logging:
   # The ID and range of a sample spreadsheet.
   SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
   RANGE_NAME = os.getenv('RANGE_NAME')
   # If modifying these scopes, delete the file token.pickle.
   SCOPES = ['https://www.googleapis.com/auth/spreadsheets',# See, edit, create and delete all your Google Sheets spreadsheets
             'https://www.googleapis.com/auth/drive.file', # see, edit, create, and delete only the specific Google Drive files you use with this app
             'https://www.googleapis.com/auth/drive'] # see,edit, create, and delete all google Drives files
   SERVICE_ACCOUNT_FILE = path.join(os.getcwd(), 'credentials.json')

   def __init__(self):
       self.credentials = self.auth()
       self.service = discovery.build('sheets', 'v4', credentials=self.credentials)

# Authorizes Client
   def auth(self):
       creds = None

       if not creds or not creds.valid:
           if creds and creds.expired and creds.refresh_token:
               creds.refresh(Request())
           else:
               creds = service_account.Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)

       return creds

   def read_data(self):
       # Call the Sheets API
       service = self.service
       sheet = service.spreadsheets()
       result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                   range=self.RANGE_NAME).execute()
       values = result.get('values', [])
       if not values:
           print('No data found.')
           return None
       else:
           return values

   def write_data(self, data):
       service = self.service
       values = [data]
       body = {
           'values': values
       }
       range_name = 'Sheet1'
       result = service.spreadsheets().values().append(
           spreadsheetId=self.SPREADSHEET_ID, range=range_name,
           valueInputOption='USER_ENTERED', body=body).execute()
       print('{0} cells appended.'.format(result \
                                          .get('updates') \
                                          .get('updatedCells')))

def measure_temp():
    temp = popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=","").replace('\n', ''))

def gen_data():
    data = str(input("SWIPE"))
    date = datetime.now() 
    return [str(date).split('.')[0],str(data).split('.')[0]]

# Pin 39 goes to ground for RGB LED
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)     # Controls Blue
    GPIO.setup(3, GPIO.OUT)     # Controls Red
    GPIO.setup(2, GPIO.OUT)     # Controls Green
    GPIO.setup(15,GPIO.OUT)     # setup pin output for buzzer
    buzzer = GPIO.PWM(15, 500)   # setup PWM with buzzer

    GPIO.output(2, GPIO.LOW)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(3, GPIO.HIGH)

    doc = Sheets_Logging()
    while (1):
        GPIO.output(2, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(3, GPIO.HIGH)
        data = gen_data()
        GPIO.output(3, GPIO.LOW)#RED
        GPIO.output(2, GPIO.LOW) #GREEN
        GPIO.output(4, GPIO.HIGH)
        doc.write_data(data=data)
        # Buzzes for 1 second
        buzzer.start(100)
        time.sleep(0.5)
        buzzer.stop()

        GPIO.output(2, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(2, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(2, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(3, GPIO.LOW)
        time.sleep(0.2)
    GPIO.cleanup()  # Clean up ports

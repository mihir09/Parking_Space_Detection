import glob



# import  requests
# import json
#
# def send_sms(number, message):
#     url = "https://www.fast2sms.com/dev/bulk"
#
#     prams = {
#         "authorization" : "KZPwfWStEiTno7bJaNC5zHuX4lYyIB3jdGFLse1DkQg0vRUx98n3Ye9vmc4luR6QSijwCM8KDkZ72fFs",
#         "sender_id" : "FSTSMS",
#         "route" : "p",
#         "language" : "unicode",
#         "numbers" : number,
#         "message" : message
#     }
#     response = requests.get(url, params= prams)
#     dic = response.json()
#     print(dic)
#
# send_sms(9426060538, "Thai gayu")
#
#
#
#
# # import requests
# # resp = requests.post('https://textbelt.com/text', {
# #   'phone': '+919426060538',
# #   'message': 'Hello world',
# #   'key': 'textbelt',
# # })
# # print(resp.json())
# # # python script for sending message update
# #
# # import time
# # from time import sleep
# # from sinchsms import SinchSMS
# #
# # import clx.xms
# #
# # # function for sending SMS
# # client = clx.xms.Client('{my-service-plan-id}', '{my-token}')
# #
# # try:
# #     batch_params = clx.xms.api.MtBatchTextSmsCreate()
# #     batch_params.sender = '12345'
# #     batch_params.recipients = ['9426060538', '123456789', '567894321']
# #     batch_params.body = 'Hello, ${name}!'
# #     batch_params.parameters = {
# #             'name': {
# #                 '987654321': 'Mary',
# #                 '123456789': 'Joe',
# #                 'default': 'valued customer'
# #             }
# #         }
# #
# #     batch = client.create_text_batch(batch_params)
# #     print('The batch was given ID %s' % batch.batch_id)
# # except Exception as ex:
# #     print('Error creating batch: %s' % str(ex))
# #
# #
#
#
#
#
#
#
# # import datetime
# # import subprocess
# # import sys
# # import time
# # import webbrowser
# # import cv2
# #
# #
# # import pyttsx3
# # import requests
# # import wolframalpha
# #
# #
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# # from PyQt5.uic import loadUi
# # import speech_recognition as sr
# # from wikipedia import wikipedia
# #
# # first_time = True
# #
# #
# # engine = pyttsx3.init('sapi5')
# # voices = engine.getProperty('voices')
# # engine.setProperty('voice', 'voices[0].id')
# #
# #
# # class AideUI(QMainWindow):
# #
# #     def __init__(self):
# #         super(AideUI, self).__init__()
# #         loadUi('aide.ui', self)
# #
# #         self.listen = self.findChild(QPushButton, 'listen')
# #         self.listen.clicked.connect(self.listen_command)
# #
# #         self.show()
# #
# #     def speak(self, text):
# #         engine.say(text)
# #         engine.runAndWait()
# #
# #     def wishMe(self):
# #         hour = datetime.datetime.now().hour
# #         if hour>=0 and hour<12:
# #             self.speak("Hello, Good Morning, I'm Aide")
# #             print("Hello, Good Morning, I'm Aide")
# #         elif hour>=12 and hour<16:
# #             self.speak("Hello, Good Afternoon, I'm Aide")
# #             print("Hello, Good Afternoon, I'm Aide")
# #         elif hour>=16 and hour<19:
# #             self.speak("Hello, Good Evening , I'm Aide")
# #             print("Hello, Good Evening, I'm Aide")
# #         else:
# #             self.speak("Hello, I'm Aide")
# #             print("Hello, I'm Aide")
# #
# #
# #
# #     def take_command(self):
# #         r = sr.Recognizer()
# #         with sr.Microphone() as source:
# #             print("Listening...")
# #             audio = r.listen(source)
# #
# #             try:
# #                 statement = r.recognize_google(audio, language='en-in')
# #                 print(f"user said:{statement}\n")
# #             except Exception as e:
# #                 self.speak("Pardon me, Please say that again")
# #                 return "None"
# #             return statement
# #
# #
# #     def listen_command(self):
# #         while True:
# #             global first_time
# #             if first_time == True:
# #                 self.speak("Loading your AI Personal Assistant Aide")
# #                 self.wishMe()
# #                 first_time = False
# #
# #             self.speak("Tell me how can I help you now?")
# #
# #             statement = self.take_command().lower()
# #             if statement == 0:
# #                 continue
# #
# #             if "good bye" in statement or "ok bye" in statement or "bye" in statement or "stop" in statement:
# #                 self.speak('Your personal assistant Aide is shutting down,Good bye')
# #                 print('Your personal assistant Aide is shutting down,Good bye')
# #                 self.close()
# #                 break
# #
# #             if 'wikipedia' in statement:
# #                 self.speak('What to search in Wikipedia...')
# #                 statement = self.take_command().lower()
# #                 results = wikipedia.summary(statement, sentences=3)
# #                 self.speak("According to Wikipedia")
# #                 print(results)
# #                 self.speak(results)
# #
# #
# #             elif 'open youtube' in statement:
# #                 webbrowser.open_new_tab("https://www.youtube.com")
# #                 self.speak("Youtube is open now")
# #                 time.sleep(5)
# #
# #             elif 'open google' in statement:
# #                 webbrowser.open_new_tab("https://www.google.com")
# #                 self.speak("Google chrome is open now")
# #                 time.sleep(5)
# #
# #             elif 'open gmail' in statement:
# #                 webbrowser.open_new_tab("https://www.gmail.com")
# #                 self.speak("Google Mail open now")
# #                 time.sleep(5)
# #
# #             elif "weather" in statement:
# #                 api_key = "8ef61edcf1c576d65d836254e11ea420"
# #                 base_url = "https://api.openweathermap.org/data/2.5/weather?"
# #                 self.speak("whats the city name")
# #                 city_name = self.take_command()
# #                 complete_url = base_url + "appid=" + api_key + "&q=" + city_name
# #                 response = requests.get(complete_url)
# #                 x = response.json()
# #                 if x["cod"] != "404":
# #                     y = x["main"]
# #                     current_temperature = y["temp"]
# #                     current_humidity = y["humidity"]
# #                     z = x["weather"]
# #                     weather_description = z[0]["description"]
# #                     self.speak(" Temperature in kelvin unit is " +
# #                                str(current_temperature) +
# #                                "\n humidity in percentage is " +
# #                                str(current_humidity) +
# #                                "\n description  " +
# #                                str(weather_description))
# #                     print(" Temperature in kelvin unit = " +
# #                           str(current_temperature) +
# #                           "\n humidity (in percentage) = " +
# #                           str(current_humidity) +
# #                           "\n description = " +
# #                           str(weather_description))
# #                 else:
# #                     self.speak(" City Not Found ")
# #
# #             elif 'time' in statement:
# #                 str_time = datetime.datetime.now().strftime("%H:%M:%S")
# #                 self.speak(f"the time is {str_time}")
# #
# #             elif 'who are you' in statement or 'what can you do' in statement:
# #                 self.speak('I am Aide version 1 point O your persoanl assistant. I am programmed to minor tasks like'
# #                            'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,'
# #                            'search wikipedia,predict weather '
# #                            'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
# #
# #             # elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
# #             #     self.speak("I was built by Nidhi, Prutha, Nikhil")
# #             #     print("I was built by Nidhi, Prutha, Nikhil")
# #
# #             elif "open stackoverflow" in statement or "open stack overflow" in statement:
# #                 webbrowser.open_new_tab("https://stackoverflow.com/login")
# #                 self.speak("Here is stackoverflow")
# #
# #             elif 'news' in statement:
# #                 webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
# #                 self.speak('Here are some headlines from the Times of India,Happy reading')
# #                 time.sleep(6)
# #
# #             elif "camera" in statement or "take a photo" in statement:
# #                 cam = cv2.VideoCapture(0)
# #                 cv2.namedWindow("test")
# #                 img_counter = 0
# #
# #                 while True:
# #                     ret, frame = cam.read()
# #                     if not ret:
# #                         print("failed to grab frame")
# #                         break
# #                     cv2.imshow("test", frame)
# #
# #                     k = cv2.waitKey(1)
# #                     if k % 256 == 27:
# #                         # ESC pressed
# #                         print("Escape hit, closing...")
# #                         break
# #                     elif k % 256 == 32:
# #                         # SPACE pressed
# #                         img_name = "opencv_frame_{}.png".format(img_counter)
# #                         cv2.imwrite(img_name, frame)
# #                         print("{} written!".format(img_name))
# #                         img_counter += 1
# #
# #                 cam.release()
# #
# #                 cv2.destroyAllWindows()
# #
# #             elif 'search' in statement:
# #                 self.speak('What you want to search?')
# #                 statement = self.take_command().lower()
# #                 webbrowser.open_new_tab(statement)
# #                 time.sleep(5)
# #
# #             elif 'ask' in statement:
# #                 self.speak(
# #                     'I can answer to computational and geographical questions and what question do you want to ask now')
# #                 question = self.take_command()
# #                 client = wolframalpha.Client('R2K75H-7ELALHR35X')
# #                 res = client.query(question)
# #                 answer = next(res.results).text
# #                 self.speak(answer)
# #                 print(answer)
# #
# #             elif "log off" in statement or "sign out" in statement:
# #                 self.speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
# #                 subprocess.call(["shutdown", "/l"])
# #
# #         time.sleep(1)
# #
# #
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     UIWindow = AideUI()
# #     app.exec_()

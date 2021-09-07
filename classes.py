import time
import requests
# Monday
classes_0 = [   
    {"time_hour" : "9", "time_min": "0" , "message" : "Class: ,\n Meet Link: https://meet.google.com/sar-awhh-ydy ,\n GCR link:"},
    ]

print(classes_0)

print(time.localtime())

print(time.localtime().tm_wday)

print(classes_0[0]["time_hour"])

base_url = 'https://api.telegram.org/bot1975468404:AAF8tX79VN2DY9MiG-VFdysjjBVpsR9H08I/sendMessage?chat_id=-442028738&text="{}"'.format(classes_0[0]["message"]) 
# print(base_url)
requests.get(base_url)
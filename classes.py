import time
import requests

# Monday
classes_0 = [   
    {"time_hour" : "9", "time_min": "0" , "message" : "Class: ,\n Meet Link: https://meet.google.com/sar-awhh-ydy"},
    {"time_hour" : "9", "time_min": "0" , "message" : "Class: ,\n Meet Link: https://meet.google.com/sar-awhh-ydy"},
    ]
# Tuesday
classes_1 = [   
    {"time_hour" : "9", "time_min": "0" , "message" : "Class: ,\n Meet Link: https://meet.google.com/sar-awhh-ydy"},
    {"time_hour" : "9", "time_min": "0" , "message" : "Class: ,\n Meet Link: https://meet.google.com/sar-awhh-ydy"},
    ]
# Wednesday
classes_2 = [   
    {"time_hour" : "9", "time_min": "0" , "message" : "Class: ,\n Meet Link: https://meet.google.com/sar-awhh-ydy"},
    {"time_hour" : "9", "time_min": "0" , "message" : "Class: ,\n Meet Link: https://meet.google.com/sar-awhh-ydy"},
    ]

# print(classes_0)

# print(time.localtime())

# print(time.localtime().tm_wday)

# print(classes_0[0]["time_hour"])


def sendMessage(msg):
    base_url = 'https://api.telegram.org/bot1975468404:AAF8tX79VN2DY9MiG-VFdysjjBVpsR9H08I/sendMessage?chat_id=-442028738&text="{}"'.format(msg) 
    requests.get(base_url)


def checker():
    week_day=time.localtime().tm_wday
    time_hour=time.localtime().tm_hour
    time_min=time.localtime().tm_min

    # print(time_hour,time_min,week_day)

    if ( time_hour==9 & time_min==0 ):
        
        if (week_day==0):
            sendMessage(classes_0[0]["message"])
        elif (week_day==1):
            sendMessage(classes_0[0]["message"])
        elif (week_day==2):
            sendMessage(classes_0[0]["message"])
        elif (week_day==3):
            sendMessage(classes_0[0]["message"])
        elif (week_day==4):
            sendMessage(classes_0[0]["message"])

    if ( time_hour==10 & time_min==9 ):
        
        if (week_day==0):
            sendMessage(classes_0[1]["message"])
        elif (week_day==1):
            sendMessage(classes_0[1]["message"])
        elif (week_day==2):
            sendMessage(classes_0[1]["message"])
        elif (week_day==3):
            sendMessage(classes_0[1]["message"])
        elif (week_day==4):
            sendMessage(classes_0[1]["message"])

    if ( time_hour==11 & time_min==9 ):
        
        if (week_day==0):
            sendMessage(classes_0[2]["message"])
        elif (week_day==1):
            sendMessage(classes_0[2]["message"])
        elif (week_day==2):
            sendMessage(classes_0[2]["message"])
        elif (week_day==3):
            sendMessage(classes_0[2]["message"])
        elif (week_day==4):
            sendMessage(classes_0[2]["message"])

    if ( time_hour==12 & time_min==9 ):
        
        if (week_day==0):
            sendMessage(classes_0[3]["message"])
        elif (week_day==1):
            sendMessage(classes_0[3]["message"])
        elif (week_day==2):
            sendMessage(classes_0[3]["message"])
        elif (week_day==3):
            sendMessage(classes_0[3]["message"])
        elif (week_day==4):
            sendMessage(classes_0[3]["message"])

    if ( time_hour==13 & time_min==49 ):
        
        if (week_day==0):
            sendMessage(classes_0[4]["message"])
        elif (week_day==1):
            sendMessage(classes_0[4]["message"])
        elif (week_day==2):
            sendMessage(classes_0[4]["message"])
        elif (week_day==3):
            sendMessage(classes_0[4]["message"])
        elif (week_day==4):
            sendMessage(classes_0[4]["message"])

    if ( time_hour==14 & time_min==39 ):
        
        if (week_day==0):
            sendMessage(classes_0[5]["message"])
        elif (week_day==1):
            sendMessage(classes_0[5]["message"])
        elif (week_day==2):
            sendMessage(classes_0[5]["message"])
        elif (week_day==3):
            sendMessage(classes_0[5]["message"])
        elif (week_day==4):
            sendMessage(classes_0[5]["message"])



def main():
    # Loop here
    checker()
    time.sleep(60)

while True:
    sendMessage("I'm ON ! Your Friendly Neighbourhood Class Reminder 😁")
    main()


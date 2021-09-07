import time
from datetime import datetime    
import pytz    
import calendar
import requests

tz_IN = pytz.timezone('Asia/Kolkata')   
datetimeIN = datetime.now(tz_IN)  

# Monday
classes_0 = [   

    {"time_hour" : "9", "time_min": "10" , "message" : "Class: Data Mining and Analytics\nMeet Link: https://meet.google.com/jun-cauh-iyw"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Computer Networks\nMeet Link: https://meet.google.com/odu-ypiw-ewp"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Formal Language and Automata\nMeet Link: https://meet.google.com/zif-minn-uzr"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Class: Mathematics\nMeet Link: https://meet.google.com/ddk-tvgf-qkf"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: MOOC\nMeet Link: https://meet.google.com/jun-cauh-iyw"},

    ]

# Tuesday
classes_1 = [   

    {"time_hour" : "9", "time_min": "10" , "message" : "Neuro Fuzzy : Meet Link: https://meet.google.com/sph-ckrv-atc\nInformation : https://meet.google.com/ufe-nzaw-iuj"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: VALUE EDUCATION\n Meet Link: https://meet.google.com/ezv-ywed-tux"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Mathematics\nMeet Link: https://meet.google.com/ddk-tvgf-qkf"},
    {"time_hour" : "12", "time_min": "10" , "message" : "Class: Computer Networks\nMeet Link: https://meet.google.com/odu-ypiw-ewp"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Class: Formal Language and Automata\nMeet Link: https://meet.google.com/zif-minn-uzr"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: Competative Skills\nMeet Link: https://meet.google.com/fof-kfhm-xcx"},

    ]

# Wednesday
classes_2 = [   

    {"time_hour" : "9", "time_min": "10" , "message" : "Class: Data Mining and Analytics\nMeet Link: https://meet.google.com/jun-cauh-iyw"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Ardunio\nMeet Link: https://meet.google.com/nbj-ukpw-duv"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Quants Aptitude\nMeet Link: https://meet.google.com/tfy-gxxm-otb"},
    {"time_hour" : "12", "time_min": "10" , "message" : "Class: Computer Networks\nMeet Link: https://meet.google.com/odu-ypiw-ewp"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Class: Mathematics\nMeet Link: https://meet.google.com/ddk-tvgf-qkf"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: Arduino Lab\nMeet Link 1 : https://meet.google.com/nbj-ukpw-duv\nMeet Link 2 : https://meet.google.com/kyz-yhrn-jsc"},
    ]

# Thursday
classes_3 = [   
    {"time_hour" : "9", "time_min": "10" , "message" : "Neuro Fuzzy : Meet Link: https://meet.google.com/sph-ckrv-atc\nInformation : https://meet.google.com/ufe-nzaw-iuj"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Mathematics\nMeet Link: https://meet.google.com/ddk-tvgf-qkf"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Ardunio\nMeet Link: https://meet.google.com/nbj-ukpw-duv"},
    {"time_hour" : "12", "time_min": "10" , "message" : "Class: Quants Aptitude\nMeet Link: https://meet.google.com/tfy-gxxm-otb"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Class: Formal Language and Automata\nMeet Link: https://meet.google.com/zif-minn-uzr"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: Computer Networks Lab\nMeet Link : https://meet.google.com/odu-ypiw-ewp (Not Confirmed Yet)"},
    ]

# Friday
classes_4 = [   
    {"time_hour" : "9", "time_min": "10" , "message" : "Class: Data Mining and Analytics\nMeet Link: https://meet.google.com/jun-cauh-iyw"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Formal Language and Automata\nMeet Link: https://meet.google.com/zif-minn-uzr"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Mathematics\nMeet Link: https://meet.google.com/ddk-tvgf-qkf"},
    {"time_hour" : "12", "time_min": "10" , "message" : "Class: Formal Language and Automata\nMeet Link: https://meet.google.com/zif-minn-uzr"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Neuro Fuzzy : Meet Link: https://meet.google.com/sph-ckrv-atc\nInformation : https://meet.google.com/ufe-nzaw-iuj"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: Computer Networks\nMeet Link: https://meet.google.com/odu-ypiw-ewp"},
    ]

# print(classes_0)

# print(time.localtime())

# print(time.localtime().tm_wday)

# print(classes_0[0]["time_hour"])


def sendMessage(msg):
    base_url = 'https://api.telegram.org/bot1975468404:AAF8tX79VN2DY9MiG-VFdysjjBVpsR9H08I/sendMessage?chat_id=-442028738&text="{}"'.format(msg) 
    requests.get(base_url)


def checker():
    week_day=calendar.weekday( datetimeIN.year, datetimeIN.month, datetimeIN.day)
    time_hour=datetimeIN.time().hour
    time_min=datetimeIN.time().minute

    # print(time_hour,time_min,week_day)

    if ( time_hour==15 & time_min==10 ):
        
        if (week_day==0):
            sendMessage(classes_0[0]["message"])
        elif (week_day==1):
            sendMessage(classes_1[0]["message"])
        elif (week_day==2):
            sendMessage(classes_2[0]["message"])
        elif (week_day==3):
            sendMessage(classes_3[0]["message"])
        elif (week_day==4):
            sendMessage(classes_4[0]["message"])

    if ( time_hour==15 & time_min==11 ):
        
        if (week_day==0):
            sendMessage(classes_0[1]["message"])
        elif (week_day==1):
            sendMessage(classes_1[1]["message"])
        elif (week_day==2):
            sendMessage(classes_2[1]["message"])
        elif (week_day==3):
            sendMessage(classes_3[1]["message"])
        elif (week_day==4):
            sendMessage(classes_4[1]["message"])

    if ( time_hour==15 & time_min==12 ):
        
        if (week_day==0):
            sendMessage(classes_0[2]["message"])
        elif (week_day==1):
            sendMessage(classes_1[2]["message"])
        elif (week_day==2):
            sendMessage(classes_2[2]["message"])
        elif (week_day==3):
            sendMessage(classes_3[2]["message"])
        elif (week_day==4):
            sendMessage(classes_4[2]["message"])

    if ( time_hour==15 & time_min==13 ):
        
        if (week_day==0):
            sendMessage(classes_0[3]["message"])
        elif (week_day==1):
            sendMessage(classes_1[3]["message"])
        elif (week_day==2):
            sendMessage(classes_2[3]["message"])
        elif (week_day==3):
            sendMessage(classes_3[3]["message"])
        elif (week_day==4):
            sendMessage(classes_4[3]["message"])

    if ( time_hour==15 & time_min==14 ):
        
        if (week_day==0):
            sendMessage(classes_0[4]["message"])
        elif (week_day==1):
            sendMessage(classes_1[4]["message"])
        elif (week_day==2):
            sendMessage(classes_2[4]["message"])
        elif (week_day==3):
            sendMessage(classes_3[4]["message"])
        elif (week_day==4):
            sendMessage(classes_4[4]["message"])

    if ( time_hour==15 & time_min==15 ):
        
        if (week_day==0):
            sendMessage(classes_0[5]["message"])
        elif (week_day==1):
            sendMessage(classes_1[5]["message"])
        elif (week_day==2):
            sendMessage(classes_2[5]["message"])
        elif (week_day==3):
            sendMessage(classes_3[5]["message"])
        elif (week_day==4):
            sendMessage(classes_4[5]["message"])


sendMessage("I'm ON ! Your Friendly Neighbourhood Class Reminder😁")

def main():
    # Loop here
    print("checker is running",time.localtime().tm_wday
    ,time.localtime().tm_hour
    ,time.localtime().tm_min)
    checker()
    time.sleep(60)

while True:
    main()


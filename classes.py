import time
import requests

# Monday
classes_0 = [   

    {"time_hour" : "9", "time_min": "10" , "message" : "Class: Data Mining and Analytics\nFaculty : Rajiva Divivedi\nMeet Link: https://meet.google.com/jun-cauh-iyw\nGCR Link : https://bit.ly/DataMiningAnalytics"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Computer Networks\nFaculty : Shiva Soni\nMeet Link: https://meet.google.com/odu-ypiw-ewp\nGCR Link : https://bit.ly/ComputerNetworksGCR"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Formal Language and Automata\nFaculty : Abhishek Singh\nMeet Link: https://meet.google.com/zif-minn-uzr\nGCR Link : https://bit.ly/AutomataGCR"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Class: Mathematics\nFaculty : Shikha Bansal\nMeet Link: https://meet.google.com/ddk-tvgf-qkf\nGCR Link : https://bit.ly/MathematicsGCR"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: MOOC\nFaculty : Rajiva Divivedi\nMeet Link: https://meet.google.com/jun-cauh-iyw\nGCR Link : https://bit.ly/DataMiningAnalytics"},


    ]

# Tuesday
classes_1 = [   

    {"time_hour" : "9", "time_min": "10" , "message" : "1. Neuro Fuzzy (Faculty - Nidhi Pandey) : Meet Link: https://meet.google.com/sph-ckrv-atc\nGCR Link : https://bit.ly/NeuroFuzzy\n2. Information Storage (Faculty - Medhavi Malik) : https://meet.google.com/ufe-nzaw-iuj\n GCR Link : https://bit.ly/InformationGCR"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Indian Traditional Knowledge\nFaculty : Shalini Sharma\nMeet Link: https://meet.google.com/ezv-ywed-tux\nGCR Link : https://bit.ly/ValueGCR"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Mathematics\nFaculty : Shikha Bansal\nMeet Link: https://meet.google.com/ddk-tvgf-qkf\nGCR Link : https://bit.ly/MathematicsGCR"},
    {"time_hour" : "12", "time_min": "10" , "message" : "Class: Computer Networks\nFaculty : Shiva Soni\nMeet Link: https://meet.google.com/odu-ypiw-ewp\nGCR Link : https://bit.ly/ComputerNetworksGCR"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Class: Formal Language and Automata\nFaculty : Abhishek Singh\nMeet Link: https://meet.google.com/zif-minn-uzr\nGCR Link : https://bit.ly/AutomataGCR"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: Competitive Professional Skills - II\nFaculty : Chandra Shekher Tyagi\nMeet Link: https://meet.google.com/fof-kfhm-xcx\nGCR Link : https://bit.ly/CPSGCR"},

    ]

# Wednesday
classes_2 = [   

    {"time_hour" : "9", "time_min": "10" , "message" : "Class: Data Mining and Analytics\nFaculty : Rajiva Divivedi\nMeet Link: https://meet.google.com/jun-cauh-iyw\nGCR Link = https://bit.ly/DataMiningAnalytics"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Ardunio\nFaculty : Manoj K Vishnoi\nMeet Link: https://meet.google.com/nbj-ukpw-duv\nGCR Link : https://bit.ly/ESDAGCR"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Quantative Aptitude\nFaculty : Avinash Singh\nMeet Link: https://meet.google.com/tfy-gxxm-otb\nGCR Link : https://bit.ly/QuantsGCR"},
    {"time_hour" : "12", "time_min": "10" , "message" : "Class: Computer Networks\nFaculty : Shiva Soni\nMeet Link: https://meet.google.com/odu-ypiw-ewp\nGCR Link : https://bit.ly/ComputerNetworksGCR"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Class: Mathematics\nFaculty : Shikha Bansal\nMeet Link: https://meet.google.com/ddk-tvgf-qkf\nGCR Link : https://bit.ly/MathematicsGCR"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: Arduino Lab\nFaculty : Prashant Mani\nMeet Link 1 : https://meet.google.com/nbj-ukpw-duv\nMeet Link 2 : https://meet.google.com/kyz-yhrn-jsc\nGCR Link : https://bit.ly/ESDALab"},
    
    ]

# Thursday
classes_3 = [
    
    {"time_hour" : "9", "time_min": "10" , "message" : "1. Neuro Fuzzy (Faculty - Nidhi Pandey) : Meet Link: https://meet.google.com/sph-ckrv-atc\nGCR Link : https://bit.ly/NeuroFuzzy\n2. Information (Faculty - Medhavi Malik) : https://meet.google.com/ufe-nzaw-iuj\n GCR Link : https://bit.ly/InformationGCR"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Mathematics\nFaculty : Shikha Bansal\nMeet Link: https://meet.google.com/ddk-tvgf-qkf\nGCR Link : https://bit.ly/MathematicsGCR"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Ardunio\nFaculty : Manoj K Vishnoi\nMeet Link: https://meet.google.com/nbj-ukpw-duv\nGCR Link : https://bit.ly/ESDAGCR"},
    {"time_hour" : "12", "time_min": "10" , "message" : "Class: Quantative Aptitude\nFaculty : Avinash Singh\nMeet Link: https://meet.google.com/tfy-gxxm-otb\nGCR Link : https://bit.ly/QuantsGCR"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Class: Formal Language and Automata\nFaculty : Abhishek Singh\nMeet Link: https://meet.google.com/zif-minn-uzr\nGCR Link : https://bit.ly/AutomataGCR"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: Computer Networks Lab\nFaculty : Shiva Soni\nMeet Link: https://meet.google.com/odu-ypiw-ewp (Not Confirmed Yet)\nGCR Link : https://bit.ly/ComputerNetworksGCR"},
    
    ]

# Friday
classes_4 = [   
    
    {"time_hour" : "9", "time_min": "10" , "message" : "Class: Data Mining and Analytics\nFaculty : Rajiva Divivedi\nMeet Link: https://meet.google.com/jun-cauh-iyw\nGCR Link = https://bit.ly/DataMiningAnalytics"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Formal Language and Automata\nFaculty : Abhishek Singh\nMeet Link: https://meet.google.com/zif-minn-uzr\nGCR Link : https://bit.ly/AutomataGCR"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Mathematics\nFaculty : Shikha Bansal\nMeet Link: https://meet.google.com/ddk-tvgf-qkf\nGCR Link : https://bit.ly/MathematicsGCR"},
    {"time_hour" : "12", "time_min": "10" , "message" : "Class: Formal Language and Automata\nFaculty : Abhishek Singh\nMeet Link: https://meet.google.com/zif-minn-uzr\nGCR Link : https://bit.ly/AutomataGCR"},
    {"time_hour" : "13", "time_min": "50" , "message" : "1. Neuro Fuzzy (Faculty - Nidhi Pandey) : Meet Link: https://meet.google.com/sph-ckrv-atc\nGCR Link : https://bit.ly/NeuroFuzzy\n2. Information (Faculty - Medhavi Malik) : https://meet.google.com/ufe-nzaw-iuj\n GCR Link : https://bit.ly/InformationGCR"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: Computer Networks\nFaculty : Shiva Soni\nMeet Link: https://meet.google.com/odu-ypiw-ewp\nGCR Link : https://bit.ly/ComputerNetworksGCR"},
    
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


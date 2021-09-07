import time
import requests

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

print(classes_0)

print(time.localtime())

print(time.localtime().tm_wday)

print(classes_0[0]["time_hour"])

base_url = 'https://api.telegram.org/bot1975468404:AAF8tX79VN2DY9MiG-VFdysjjBVpsR9H08I/sendMessage?chat_id=-442028738&text="{}"'.format(classes_0[0]["message"]) 
# print(base_url)
requests.get(base_url)

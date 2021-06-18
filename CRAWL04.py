#    ,ad8888ba,   88888888ba          db    I8,        8        ,8I  88           ,a8888a,             ,d8    
#   d8"'    `"8b  88      "8b        d88b   `8b       d8b       d8'  88         ,8P"'  `"Y8,         ,d888    
#  d8'            88      ,8P       d8'`8b   "8,     ,8"8,     ,8"   88        ,8P        Y8,      ,d8" 88    
#  88             88aaaaaa8P'      d8'  `8b   Y8     8P Y8     8P    88        88          88    ,d8"   88    
#  88             88""""88'       d8YaaaaY8b  `8b   d8' `8b   d8'    88        88          88  ,d8"     88    
#  Y8,            88    `8b      d8""""""""8b  `8a a8'   `8a a8'     88        `8b        d8'  8888888888888  
#   Y8a.    .a8P  88     `8b    d8'        `8b  `8a8'     `8a8'      88         `8ba,  ,ad8'            88    
#    `"Y8888Y"'   88      `8b  d8'          `8b  `8'       `8'       88888888888  "Y8888P"              88
# Made by Samuel Lomas
# https://github.com/slomas04/

###### IMPORTS ######
import urllib.request
import re

###### GET TARGET SITE ######

def geturl():
    while True: ### This little section verifies that the website is running and valid
        targeturl = input("Enter your FULL target URL\t(type 'exit' to exit)\n>>> ")
        if targeturl == 'exit':
            exit()
            
        try:
            x = (urllib.request.urlopen(targeturl).getcode())
            if int(x) == 200: # Make sure that website returns the correct code
                print("URL is valid!")
                return targeturl
        except:
            print("URL is either invalid or website is down!")
            
###### GET SITE HTML ######
            
def gethtml(url):
    return(urllib.request.urlopen(url).read()) #returns whole site data as HTML

###### SCAN SITE DATA FOR MORE URLS ######

def scan(data):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    # Absolutely disgusting and awful regex line
    urls = re.findall(regex,data)      
    return [x[0] for x in urls]
    

###### MAINLOOP ######

targeturl = geturl()
        
input("Your target URL is " + targeturl + "\nPress enter to start iteration 1...")

data = (gethtml(targeturl)).decode("utf-8")
urllist = scan(data)

file = open('', 'w')

for i in range(len(urllist)):
    print(urllist[i])





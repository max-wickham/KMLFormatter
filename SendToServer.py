import requests
import random 
import json
def GetPlaceCases(data):
    num1 = 0
    num2 = 0
    inname = False
    output = {}
    for i in range(len(data)):
        if data[i] == "{" and (data[i-1] != ")" or i < 2):

            print("found place")
            inname = True
            num1 = i
        if data[i] == "," and inname:
            inname = False
            num2 = i
            output[data[num1+2:num2-1]] = str(random.randint(1,100))
    return output

def send(data):
    url = 'http://192.168.1.16:5000/add_location'
    myobj = data
    print(data)

    x = requests.post(url, json = myobj)

    print(x.text) 


#url = 'https://www.w3schools.com/python/demopage.php'
#myobj = {'somekey': 'somevalue'}

#x = requests.post(url, data = myobj)

#print(x.text)


f = open("DictionaryFormat.txt","r")
x = f.read()
f.close()
Response = GetPlaceCases(x)
send(Response)
#g = open("Cases.txt","w")
#g.write(str(Response))
#g.close




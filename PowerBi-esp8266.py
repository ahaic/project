# visualize data with power bi from esp8266 sensor generated data
# devices: esp8266 , soil moisture sensor  , DHT11 
# date: 21 April 2020


import time,requests,sys,json
from datetime import datetime

REST_API_URL = "https://api.powerbi.com/beta/a385e20d-a6e7-4ee3-9068-269f93dd9494/datasets/764bff2d-e399-41b2-8542-ff4cb7545eb2/rows?\
key=IUzr7BmYnE0wL%2BNLkXB6vQAnkfDWKev%2BLMa8uk%2B9fBQNattCvP0NtSdWshti9VBCmCjHXiCkOQ680FOKqU9fKA%3D%3D"



def sensor():
    global data
    resp = requests.get('http://192.168.1.108/json')
    sensor = resp.json()
    
    moisture= sensor['Sensors'][0]['TaskValues'][0]['Value']
    
    temp= sensor['Sensors'][1]['TaskValues'][0]['Value']              
    humid = sensor['Sensors'][1]['TaskValues'][1]['Value']
    
    data = '[{{ "timestamp": "{0}","moisture": {1:0.2f},"temperature":{2:0.1f},"humidity":{3:0.1f} }}]'.\
           format(datetime.now().strftime("%Y-%m-%dT%H:%M:%S%Z"), moisture,temp,humid)
    

    return data
    
    


while True:
    try:
        #print(json.dumps(data))
        req = requests.post(REST_API_URL, data=sensor())  # make HTTP POST request to Power BI REST API
        print(data)
        print(req.status_code)
        print('----------------------------')
        print(req.text)
    

        time.sleep(60)
        
    except Exception as e:
        print('error ...')
        print("General Exception: {0}".format(e))
        print('error time',datetime.now())
        time.sleep(30)
  


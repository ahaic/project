#coding=utf-8

import http.client
import urllib.request
import sqlite3
import smtplib

from time import sleep,ctime,strftime
class A:


    global API_KEY
    API_KEY="6fdb2f7d7a8706bd3da6017c346b13bc"
        
   
    def get_rate(self):
        try:
            response=urllib.request.urlopen("http://m.cmbchina.com/Rate/FxRealrateDetail.aspx?name=%b0%c4%d4%aa")
            data=response.read().decode('GBK')
            s=data.index('卖出价')+55
            
            
            e=s+6
            
            A.current_rate = data[s:e]
            
            print('AUD/CNY:  '+ A.current_rate)
            self.post_data(644.47,2162,2847) 
        
        except Exception as e:
            
            sleep(3)
            print(e)
            print('refresh data after 15 sec\n')
            self.get_rate()
            
        
    def post_data(self,data,device_id, sensor_id):
        d = '{"value": %f}' % data
        h = {"U-ApiKey": API_KEY}
        p = "/v1.0/device/%d/sensor/%d/datapoints" % (device_id, sensor_id)

        conn = http.client.HTTPConnection("api.yeelink.net")
        conn.request("POST", p, d, h)
        response = conn.getresponse()
        return response.status
            


    
object = A()


while True:
    object.get_rate()
    
    
#    print('-------------'+ ctime() +'--------------')
    
#    print(' wait another 15 seconds \n')
    sleep(1)






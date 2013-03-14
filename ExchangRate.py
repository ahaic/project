#coding=utf-8


import urllib.request
import sqlite3
import smtplib

from time import sleep,ctime,strftime
class A:
    store_location="/Users/ahaic/Dropbox/workspace/test.db"
    current_rate=0
    target_rate=0
    count = 0
    
    def __init__(self,x):
        
        A.target_rate = x
#        self.get_rate()    
        print("initializing")
        print("target_price:", A.target_rate)     
    def get_rate(self):
        try:
            response=urllib.request.urlopen("http://m.cmbchina.com/Rate/FxRealrateDetail.aspx?name=%b0%c4%d4%aa")
            data=response.read().decode('GBK')
            A.current_rate =  data[3098:3104]
            
            print('AUD/CNY:  '+ A.current_rate)
        
        except:
            
            sleep(3)
            print('-----------------exception incurrs ---------------')
            print('refresh data after 15 sec\n')
            self.get_rate()
            
        
        
        if float(A.current_rate) < float(A.target_rate):
            
            A.target_rate = A.current_rate  # send mail once
            print('the target rate is now updated to', A.target_rate)
            print("sending mail")
            #self.sendmail()
        else:
            print('email not activited')
            
            
            
    def store_data(self):
        
        
        try:
            params = (A.current_rate,strftime('%d-%m-%Y'),strftime('%H:%M:%S'))
            print(type(params),params)
            
            conn = sqlite3.connect(A.store_location)  #create database if not exist   ~/Dropbox/
           # print("connecting database")
        
            
            
            c=conn.cursor()
        
          #c.execute('create table exchange_rate (AUDCNY,Date,Time)' )
            c.execute('INSERT INTO exchange_rate VALUES (?,?,?)', params)        
            conn.commit()
            print("connected and inserting data...")
        except:
            print("cannot connect to database")
                
    def sendmail(self):
        mail_server = "smtp.qq.com"
        send_from="562620123@qq.com"
        mail_to="hansoncao@hotmail.com"
        msg =self.current_rate
        mail = smtplib.SMTP(mail_server)
        mail.login("562620123@qq.com", "881025")
        mail.sendmail(send_from,mail_to,msg)
        print ("mail over")
        
        
    def analysis(self):
        pass
    
object = A(663)


while True:
    object.get_rate()
    object.store_data()    
    A.count = A.count+1
    
    print(A.count)
    
    print('-------------'+ ctime() +'--------------')
    
    print(' wait another 15 seconds \n')
    
    sleep(15)

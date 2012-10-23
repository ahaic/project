#  create to get Dynamic IP
#add time + ip  written in txt
import socket
import os
from time import sleep,ctime,strftime
import time

class GetIp(object):

    
    
    global TIME
#    global path
#    path = '/Users/ahaic/Desktop/ip_log.txt'

    def __init__(self,url,path):

        self.url=url
        self.ip=''
        self.path = path
        
        self.record_ip()

        

    def get_ip(self):
        global IP

        try:

            IP=str(socket.gethostbyname_ex(self.url)[2][0])
            
            print(IP)
            
        except socket.error as e:

            print('socket error: %s ' % e)
            sleep(100)
            self.get_ip()

    def record_ip(self):
        while True:
            self.get_ip()
            
        
            if os.path.isfile(self.path) !=True:

                print('file does not exists ')
                
                try:
                    ip_log = open(self.path,'w')

                except IOError:
                    print('IO Error ')
                    exit()
                    
               
            else:
                try:
                    
                    ip_log=open(self.path,'a')
                except:
                    print(' open file failed in a mode')
                else:
                    print('file open successfully')
                    
            try:
                self.output()
                ip_log.write('%s \n %s ' % (self.row1,self.row2))
                ip_log.write('\n')
                ip_log.close()
    
                
            except Exception as e:             # catch all exception
                print('written failed :', e)
                print('stop running')
                break
            else:
                print('written  \n waiting for next writting')
                

            sleep(3600)
    
    def set_time(self):

        pass
    
    
        
    def output(self):

        li = 18 -len(IP)
        ip="  "+IP+(li*" ")

        time =   strftime('%d-%m-%Y')+ " " +strftime('%H:%M:%S')
        lt = 18-len(time)
        time="  "+time+(lt*" ")
    
        self.row1 =(22*'-')+'+'+(22*'-')
    
        self.row2='|'+ip+'|'+time+'|'

 #       return self.row1
        



        
            

        
obj = GetIp('paksila.xicp.net','/home/python/ip_log.txt')

#obj = GetIp('paksila.xicp.net','/Users/ahaic/Desktop/ip_log.txt')

print('ip address: ', IP)
        
    
    

#  create to get Dynamic IP
#add time + ip  written in txt
import socket
import os
from time import sleep,ctime,strftime
import time

class GetIp(object):

    
#    global path
#    path = '/Users/ahaic/Desktop/ip_log.txt'

    def __init__(self,url,path):

        self.url=url
        self.ip=''
        self.path = path
        
        self.record_ip()

        

    def get_ip(self):

        self.ip=socket.gethostbyname_ex(self.url)

    def record_ip(self):
        while True:
            self.get_ip()
            
        
            if os.path.isfile(self.path) !=True:

                print('file does not exists ')
                try:
                    ip_log = open(self.path,'w')

                except IOError:
                    print('fucked')
               
            else:
                try:
                    
                    ip_log=open(self.path,'a')
                except:
                    print(' open file failed in a mode')
                else:
                    print('file open successfully')
                    
            try:
                ip_log.write('%s <----> %s %s ' % (self.ip[2],strftime('%d-%m-%Y'),strftime('%H:%M:%S')))
                ip_log.write('\n')
                ip_log.close()
    
                
            except:
                print('written failed')
            else:
                print('written')

            sleep(3600)
    
    def set_time(self):

        pass        

        
            

        
obj = GetIp('paksila.xicp.net','/Users/ahaic/Desktop/ip_log.txt')


print('ip address: ', obj.ip[2])
        
    
    

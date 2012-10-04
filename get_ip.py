#  create to get Dynamic IP
import socket
import os
class GetIp(object):

    
    global path
    path = '/Users/ahaic/Desktop/ip_log.txt'

    def __init__(self,url):

        self.url=url
        self.ip=''
        self.get_ip()
        self.record_ip()

    def get_ip(self):

        self.ip=socket.gethostbyname_ex(self.url)

    def record_ip(self):
        
        
            
        if os.path.isfile(path) !=True:

            print('file does not exists ')
            try:
                ip_log = open(path,'w')

            except IOError:
                print('fucked')
               
        else:
            try:
                
                ip_log=open(path,'a')
            except:
                print(' open file failed in a mode')
            else:
                print('file open successfully')

        ip_log.writelines(self.ip[2])
        ip_log.write('\n')
        ip_log.close()

        print('written')

        
obj = GetIp('paksila.xicp.net')


print('ip address: ', obj.ip[2])
        
    
    

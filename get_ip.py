#  create to get Dynamic IP
import socket

class GetIp(object):

    
    store_path = ''

    def __init__(self,url):

        self.url=url
        self.ip=''

    def get_ip(self):

        self.ip=socket.gethostbyname_ex(self.url)

    def record_ip(self):

        pass


obj = GetIp('paksila.xicp.net')

output_ip = obj.get_ip()



print('ip address: ', obj.ip[2])
        
    
    

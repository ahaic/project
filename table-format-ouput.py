'''

format table output  21 Oct 2012

example

--------------------- + ----------------------
| 192.168.1.23         | 21 Oct 2012 14:28    |
---------------------- + ----------------------

'''
    
def output(ip,time):

    li = 20 -len(ip)
    ip=ip+(li*" ")


    lt = 20-len(time)
    time=time+(lt*" ")
    
    print(22*'-','+',22*'-',)
    print('|',ip,'|',time,'|')
    print(22*'-','+',22*'-')
        
output('192.168.1.23','21 Oct 2012 14:28')


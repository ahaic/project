
import binascii
import os

class jgs(object):

    buju=[]

    results = {}

    def __init__(self):

        self.l0=[]
        self.l1=[]
        self.l2=[]
        self.l3=[]
        self.l4=[]
        self.l5=[]
        self.l6=[]
        self.l9=[]
        self.l10=[]

    def read_file(self):
        count = 0
                
        for root, dirs, files in os.walk('/Users/ahaic/Dropbox/Tencent/JQ/'):
            print(len(files))
            for jgs in files:
                
                f=open(os.path.join(root,jgs),'rb')
                
                data = f.read()
                hex=binascii.b2a_hex(data)
                data_up = hex[120:180]
                data_down = hex[296:356]
                data_left = hex[472:532]
                data_right = hex[648:708]

                buju = data_down,data_right,data_up,data_left  # type: tuple
               
                self.analysis(buju)


        m = {'junqi':'02','dilei':'03','zhadan':'04','siling':'05','jun':'06','shi':'07',\
             'lv':'08','tuan':'09','ying':'0a','lian':'0b','pai':'0c','bing':'0d','junying':'00'}
        for i in m:
            
            print(i,self.l9.count(m[i]))
        print('number',len(self.l9))
        
        print('done')
                
        
                
    def to_hex(self):
        pass

    def analysis(self,buju):
    
        i=0        

        data=[]
        for n in buju:
            
            data.append(bytes.decode(n))

 #       print(data)

        kk=[]

        for ii in data:
            while i<30:
                kk.append(ii[2*i:2*i+2])
                i=i+1
            self.l0.append(kk[0])
            self.l4.append(kk[4])
            self.l5.append(kk[5])
            self.l6.append(kk[6])
            self.l9.append(kk[9])

        #print(len(self.l0))


            
       # for k in kk:            
#            self.l0.append(k)

        

        
    
obj = jgs()


obj.read_file()
    




'''
m = ['02','03','04','05','06','07','08','09','0a','0b','0c','0d','00']
>>> for i in m:
	obj.l0.count(i)

	'''


import random,itertools,base64,time,multiprocessing
from collections import Iterator,Iterable
from urllib import request,parse
from bs4 import BeautifulSoup
from tqdm import *

def company(rego):

    headers = {
          'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
          'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
          'Connection': 'keep-alive'
     }

    url = 'http://www.czgsj.gov.cn/baweb/show/shiju/details.jsp?reg_no='
     # base64 digest of a string
    key=['biz_name','biz_rego','biz_rep','biz_est','biz_type','biz_DateApproved',
         'biz_capital','reg_add','biz_duration','biz_start','biz_end','biz_scope']
    value=[]
    encoded = base64.b64encode(rego.encode())
    r = url+encoded.decode("utf-8")  # covert bytes to string with decode func
    #print(r)    # generate request url
    req = request.Request(r)
    response = request.urlopen(req)
    page = response.read().decode('utf-8')
    #分析单独页面数据
    soup = BeautifulSoup(page,"html.parser")
    for i in soup.find_all("input",attrs={"class":"input_text"}):
        #print(i["value"])
        value.append(i["value"])
    for i in soup.find_all("textarea",attrs={}):
        #print(i.text)
        value.append(i.text)
    #print(value)
    if value[0]!='':
        print(dict(zip(key,value)))
'''
Generate valid rego number
formular to generate last digit that is verifying code
C: giving 17 digits code             320412MA1NC3U8X1
 C18 = 31 - MOD ( ∑Ci * Wi ，31) (1)  MOD  表示求余函数；
 i    表示代码字符从左到右位置序号； Ci   表示第i位置上的代码字符的值，采用附录A“代码字符集”所列字符；
 C18  表示校验码； Wi   表示第i位置上的加权因子，其数值如下表：
  i 1 2 3 4  5  6  7  8  9  10 11 12 13 14 15 16 17
 Wi 1 3 9 27 19 26 16 17 20 29 25 13  8 24 10 30 28
 当MOD函数值为0（即 C18 = 31）时，校验码用数字0表示。
91320404MA1NC33L4
'''
def verify(C):
    s = 0   # sum of list elements
    CiWi=[]
    #C = list('91350100M000100Y4')
 #   C = input('input 17 codes\n')
    C_new = list(C)
    #C = list('91320411MA1NC32Q9')
    dic = {
        'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,
           'H':17,'J':18,'K':19,'L':20,'M':21,'N':22,'P':23,
           'Q':24,'R':25,'T':26,'U':27,'W':28,'X':29,'Y':30
        }
    Wi = [1,3,9,27,19,26,16,17,20,29,25,13,8,24,10,30,28]
    for i in C_new:
        if i.isalpha()==True:
            a=dic[i]
            b=C_new.index(i)
            C_new[b]=a
    res = list(map(int, C_new))
    #print(res)
    prod = list(map(lambda a,b:a*b, res,Wi))
    #print(prod)
    for i in prod:
        s+=i
#    print('total: ',s)
    last_digit = 31- s%31
#    print(last_digit)


    if 0< last_digit <10:
#        print(C,last_digit)
        company(C+str(last_digit))
    elif last_digit==30:
#        print(C,'Y')
        company(C+'Y')
    elif last_digit==31:
#        print(C,0)
        company(C+'0')
    else:
#        print(C,list(dic.keys())[list(dic.values()).index(last_digit)])
        company(C+list(dic.keys())[list(dic.values()).index(last_digit)])
#'''
# parameters
''' code genernator'''

'''
while 1:
    p = op+''.join(map(str,(a.__next__())))
    #print(next(a))
    verify(p)
    for i in tqdm(range(100)):
        verify(p)
'''

if __name__ == '__main__':
    dep_no = '9'
    type_no = '1'
    city_zip = '320411'
    org_no = 'MA1NE'   # keep first 6 and permuate last 3 digits
    ver_no = ''
    op = dep_no+type_no+city_zip+org_no
    pool1 = ['G','W',3,'F','C','B','R','D',6,'E',2,'H','J',4,5,'K','L','M','A',1,'N','P',7,0,'Q','T',9,'U','X','Y',8]
    pool2 = ['W',3,'F','C','B','R','D',6,'E',2,'G','H','J',4,5,'K','L','M','A',1,'N','P',7,0,'Q','T',9,'U','X','Y',8]
    pool3 = ['D','W',3,'F','C','B','R',6,'E',2,'G','H','J',4,5,'K','L','M','A',1,'N','P',7,0,'Q','T',9,'U','X','Y',8]
    pool4 = ['C',3,'F','B','R','D',6,'E',2,'G','H','J',4,5,'K','L','M','A',1,'N','P',7,0,'Q','T',9,'U','X','Y',8]

    a1= itertools.permutations(pool1,4)
    a2= itertools.permutations(pool2,4)
    a3= itertools.permutations(pool3,4)
    a4= itertools.permutations(pool4,4)

    try:
        print('start time',time.strftime('%H:%M:%S'))

        while True: #    print(next(a))
#            for status in tqdm(range(200000)):

            #multiprocessing.set_start_method('spawn')
            #q=multiprocessing.Queue()

            p_code1 = op+''.join(map(str,(a1.__next__())))
            p_code2 = op+''.join(map(str,(a2.__next__())))
            p_code3 = op+''.join(map(str,(a3.__next__())))
            p_code4 = op+''.join(map(str,(a4.__next__())))

        #    print(p)

            p1 = multiprocessing.Process(target=verify, args=(p_code1,))
            p2 = multiprocessing.Process(target=verify, args=(p_code2,))
            p3 = multiprocessing.Process(target=verify, args=(p_code3,))
            p4 = multiprocessing.Process(target=verify, args=(p_code4,))
            p1.start()
            p2.start()
            p3.start()
            p4.start()
#                print(q.get())
#                p1.join()
#                p2.join()
#                p3.join()
#                p4.join()
            #    verify(p_code)

    except StopIteration:
        print('CPU number:' + str(multiprocessing.cpu_count()))
        for p in multiprocessing.active_children():
            print('Child process name: ' + p.name + ' id: ' + str(p.pid))
        print('Process Ended')

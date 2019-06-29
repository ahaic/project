#coding:utf8
#29 June 2019
# for the purpsoe of scanning all video names and making schedule

import os,csv
import sys



print('current dir:', os.getcwd())

path=os.getcwd()
f = []
for (dirpath, dirnames, filenames) in os.walk(path):
    f.extend(filenames)
    break

print(type(f))



with open('output.csv', 'w',newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)

#    writer.writerows([f])

    for row in f:
    #    print(row)
    #    print(type(row))


        writer.writerow([row])

    print('finish')

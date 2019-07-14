#coding:utf8
#29 June 2019
# for the purpsoe of scanning all video names and making schedule
# list filenames and video durations 
# 缘由：学习时期，很多视频资料要看，为了做学习计划和学习进度表，因此写了程序分析视频时长, 方便安排学习进度

import os,csv
import sys,cv2
import subprocess


def get_video_duration(filename):
    try:
      cap = cv2.VideoCapture(filename)
      if cap.isOpened():
        rate = cap.get(5)
        frame_num =cap.get(7)
        #print(frame_num,rate)
        duration = frame_num/rate/60
        return duration
    except cv2.error as e:
        print('not video file,ingore',e)


print('current dir:', os.getcwd())
path=os.getcwd()

f = dict()
for (dirpath, dirnames, filenames) in os.walk(path):
#    f.extend(filenames)
    for i in filenames:
        f[i]=get_video_duration(os.path.join(dirpath,i))
#    print(f)
    break


with open('output.csv', 'w',newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    for (key,value) in f.items():
        writer.writerow([key,value])
    print('finish')

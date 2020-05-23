#coding:utf8
#version 1: 29 June 2019
#version 2: 20 Sept. 2019   :support directory scan
#version 3: 28 Nov. 2019 : read all files but only display duration for video files \
#                          and you can choose which format you want to read for duration
#                          duration now show in minutes and round to two decimals
#version 4: 23 May 2020 : place in the directory and run 
# for the purpsoe of scanning all video names and making schedule
# list filenames and video durations
# 缘由：学习时期，很多视频资料要看，为了做学习计划和学习进度表，因此写了程序分析视频时长, 方便安排学习进度
#!/usr/bin/env python

__author__      = "ahaic"


import os,csv
import sys,cv2
import subprocess

file_extension = ['.mp4','.avi','.mkv']

def get_video_duration(file):
    try:
      cap = cv2.VideoCapture(file)
      if cap.isOpened():
        rate = cap.get(5)
        frame_num =cap.get(7)
        #print(frame_num,rate)
        duration = frame_num/rate/60    # 分钟

        return round(duration,2)
        #print(round(duration,2))

    except cv2.error as e:
        print('cannot read video file,ingore',e)
        return('N/A')


print('current dir:', os.getcwd())

path= os.getcwd()

lsdir = os.listdir(path)

global data   # data in to csv foramt
data = dict()


def list_of_files():

    for (dirpath, dirnames, filenames) in os.walk(path):
        for i in sorted(filenames):
            #print(os.path.join(dirpath,i))
            data[i]=get_video_duration(os.path.join(dirpath,i))
    print(data)

#get_video_duration(list_of_files())

#print(list_of_files())

with open('output.csv', 'w',newline='', encoding='utf-8-sig') as file:
    list_of_files()
    writer = csv.writer(file)
    for (key,value) in data.items():
        print(key,value)
        writer.writerow([key,value])

    print('finish')

#coding:utf8
#version 1: 29 June 2019
#version 2: 20 Sept. 2019   :support directory scan
#version 3: 28 Nov. 2019 : read all files but only display duration for video files \
#                          and you can choose which format you want to read for duration
#                          duration now show in minutes and round to two decimals

# for the purpsoe of scanning all video names and making schedule
# list filenames and video durations
# 缘由：学习时期，很多视频资料要看，为了做学习计划和学习进度表，因此写了程序分析视频时长, 方便安排学习进度
#!/usr/bin/env python

__author__      = "ahaic"


import os,csv
import sys,cv2
import subprocess

file_extension = ['.mp4','.avi','.mkv']

def get_video_duration(filename):
    try:
      cap = cv2.VideoCapture(filename)
      if cap.isOpened():
        rate = cap.get(5)
        frame_num =cap.get(7)
        #print(frame_num,rate)
        duration = frame_num/rate/60    # 分钟
        return round(duration,2)
    except cv2.error as e:
        print('cannot read video file,ingore',e)


print('current dir:', os.getcwd())

path= os.getcwd()

lsdir = sorted(os.listdir(path))

with open('output.csv', 'w',newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)

    for directory in lsdir:
        writer.writerow([directory])

        #print(directory)
        f = dict()

        f[directory]=''
        for (dirpath, dirnames, filenames) in os.walk(os.path.join(path,directory)):
        #    f.extend(filenames)

            for i in sorted(filenames):
                #print(os.path.splitext(i))
                if os.path.splitext(i)[1] in file_extension:   # [1] extract extension only

                    f[i]=get_video_duration(os.path.join(dirpath,i))
                else:
                    f[i] = 'N/A'

            for (key,value) in f.items():
                print(key,value)
                writer.writerow([key,value])

    print('finish')

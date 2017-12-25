#!/usr/bin/env python
# coding=utf-8
import os
import shutil
titles = ['美 女1','美女2','美女3','美女4','美女5','美 女6','美女7','美女9',]
for title in titles:
	title = title.strip()
	#os.makedirs("D:\\temp\\pic\\jiumei\\"+title)
	shutil.rmtree("D:\\temp\\pic\\jiumei\\"+title)
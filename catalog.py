#!coding:utf-8
#Author By Arice
import os
import sys
from termcolor import cprint
from pyExcelerator import *
'''获取文件夹和文件名
def file_name(file_dir):
	for root,dirs,files in os.walk(file_dir):
		print(root)
		print(dirs)
		print(files)

if __name__ =='__main__':
	file_name(sys.argv[1])
'''
#只获取文件名
'''
for filename in os.listdir(r'test'):
	print filename
'''
def processDirectory(args,dirname,filenames):
	cprint( '文件夹：'+dirname,'green')
	dirr.append(dirname)
	print dirr
	for filename in filenames:
		name.append(filename)
		print name	
		cprint('文件名'+filename,'red')
	#w = Workbook()
	num()
def num():
	w = Workbook()
	ws = w.add_sheet('sheet1')
	for i in range(len(name)):
		#w = Workbook()
		#ws = w.add_sheet('sheet1')
		ws.write(i,0,name[i].decode('utf-8'))
	for j in range(len(dirr)):
		ws.write(j,1,dirr[j].decode('utf-8'))
	w.save('ex.xls')

if __name__ == '__main__':
	dirr = []
	name = []
	os.path.walk(sys.argv[1],processDirectory,None)

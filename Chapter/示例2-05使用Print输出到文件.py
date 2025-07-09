fp=open('print-file.md','w') #打开文件 w->write

print('Python 您好！',file=fp) #将'Python！'输出到print-file.md文件中

fp.close()#关闭文件
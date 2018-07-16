import os,shutil
import random

 
def mymovefile(srcfile,dstfile):
    
    # fpath,fname=os.path.split(dstfile)    #分离文件名和路径
    # if not os.path.exists(fpath):
    #     os.makedirs(fpath)                #创建路径
    shutil.move(srcfile,dstfile)          #移动文件
    print ("move %s -> %s"%( srcfile,dstfile))

if __name__ == '__main__':
    srcfile = '/Users/jay_fu/Catpatch/training/'
    dstfile = '/Users/jay_fu/Catpatch/validation'

    for i in range(250):
        imgs = os.listdir(srcfile)
        kkkfo = srcfile + imgs[random.randint(0, len(imgs))]
        mymovefile(kkkfo, dstfile)
    
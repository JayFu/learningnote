import requests
import random
import time
from datetime import datetime

class Catpatch_get():

    def __init__(self):
        # self.Uurl = 'http://www.11315.com/authCode?'
        self.Uurl = 'http://jwsys.ctbu.edu.cn/CheckCode.aspx??'
    def Catch(self):
        Hheader = {
            'User-Agent':'User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
        }
        for i in range(20):            
            t = time.time()
            self.Uurl += str(random.randint(3, 31423141))
            # img = requests.get(self.Uurl) 
            # f.write(img.content)
            image = requests.get(self.Uurl)
            f = open('/Users/jay_fu/tasks/%s.png' % i, 'ab')
            f.write(image.content)
            f.close()
            print (i,t)


if __name__ == '__main__':
    s1 = Catpatch_get()
    s1.Catch()
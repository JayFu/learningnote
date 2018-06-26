import requests
import random

class Catpatch_get():

    def __init__(self):
        self.Uurl = 'http://www.11315.com/authCode?'
    def Catch(self):
        Hheader = {
            'User-Agent':'User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
        }
        for i in range(500):
            self.Uurl += str(random.randint(3, 31423141))
            # img = requests.get(self.Uurl) 
            # f.write(img.content)
            image = requests.get(self.Uurl)
            f = open('/Users/jay_fu/tasks/%s.jpg' % i, 'ab')
            f.write(image.content)
            f.close()

if __name__ == '__main__':
    s1 = Catpatch_get()
    s1.Catch()
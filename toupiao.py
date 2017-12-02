import requests

class tooupiao():
    def __init__(self):
        self.UUUrl = 'http://weike.enetedu.com/js_support.asp?vodid=187851_5&xiangmu=22&nxxx=0.6479469329751237'

    def tttou(self):
        Hheader = {
            'User-Agent':'User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
        }
        req = requests.get(self.UUUrl, headers = Hheader)
        print(req.text)

s1 = tooupiao()
s1.tttou()
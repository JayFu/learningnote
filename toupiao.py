import requests

class tooupiao():
    def __init__(self):
        # 五星
        # self.UUUrl = 'http://weike.enetedu.com/js_support.asp?vodid=187851_5&xiangmu=22&nxxx=0.6479469329751237'
        
        # 我采用
        # self.UUUrl = 'http://weike.enetedu.com/js_useradopt.asp?vodid=187851&xiangmu=22&nzz=0.3306213882457867'
        
        # 随便选一个人打分
        self.UUUrl = 'http://weike.enetedu.com/js_support.asp?vodid=180123_3&xiangmu=3&nxxx=0.5703565045885992'
    
    def tttou(self):
        Hheader = {
            'User-Agent':'User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
        }
        # 编写requests参数header
        req = requests.get(self.UUUrl, headers = Hheader)

        # print(req.text)
        # 抛出结果判断是否成功

if __name__ == '__main__':
    s1 = tooupiao()
    for i in range(2000): #刷票数量
        s1.tttou()

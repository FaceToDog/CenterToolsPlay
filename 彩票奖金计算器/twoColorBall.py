import requests
import random


class twoColorBall:
    def __init__(self):
        self.addmoney = []
        self.addmoney2 = []
        self.blue = []
        self.blue2 = []
        self.code = []
        self.content = []
        self.date = []
        self.detailsLink = []
        self.m2add = []
        self.msg = []
        self.name = []
        self.poolmoney = []
        self.red = []
        self.sales = []
        self.videoLink = []
        self.week = []
        self.z2add = []

    def twoColorBallNum(self):
        print("hello")

    def createRandomNum(self):
        numbers = random.sample(range(1, 81), 10)
        return self.quickSort(numbers)

    def quickSort(self, num):
        if len(num) <= 1:  # 边界条件
            return num
        key = num[0]  # 取数组的第一个数为基准数
        llist, rlist, mlist = [], [], [key]  # 定义空列表，分别存储小于/大于/等于基准数的元素
        for i in range(1, len(num)):  # 遍历数组，把元素归类到3个列表中
            if num[i] > key:
                rlist.append(num[i])
            elif num[i] < key:
                llist.append(num[i])
            else:
                mlist.append(num[i])
        return self.quickSort(llist) + mlist + self.quickSort(rlist)  # 对左右子列表快排，拼接3个列表并返回

    def getTwoColorBallALL(self, name='ssq', pageSize=15, *args, **kwargs):
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                                "/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
                  }
        url = "http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=" + name + \
              "&issueCount=&issueStart=&issueEnd=&dayStart=&dayEnd=&pageNo=1&pageSize=" + str(pageSize) + \
              "&week=&systemType=PC"
        response = requests.get(url=url, headers=header)
        response.encoding = "utf-8"  # 设置响应对象的编码方式为utf-8
        text = response.json()  # 获取网页源码，以文本形式显示
        var = text["result"]
        self.readNum(var)

    def readNum(self, var):
        for v in var:
            self.red.append(v['red'])
            self.addmoney.append(v['addmoney'])
            self.addmoney2.append(v['addmoney2'])
            self.blue.append(v['blue'])
            self.blue2.append(v['blue2'])
            self.code.append(v['code'])
            self.content.append(v['content'])
            self.date.append(v['date'])
            self.detailsLink.append(v['detailsLink'])
            self.m2add.append(v['m2add'])
            self.msg.append(v['msg'])
            self.name.append(v['name'])
            self.poolmoney.append(v['poolmoney'])
            self.sales.append(v['sales'])
            self.videoLink.append(v['videoLink'])
            self.week.append(v['week'])
            self.z2add.append(v['z2add'])
        print(self.red)
        print(self.blue)
        print(self.date)
        print(self.code)
        print(self.name)
        # 返回json数据，99期双色球号码
        # print(var2)
        # return var

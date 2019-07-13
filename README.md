# zxgkw
# 查查贾跃亭有多少官司和债务,依此类推。[2019-07-13]

声明：本案例仅用作学习和研究，切勿用作其它用途。

### 不用cookies，也能po到查询数据。  
### 用了最新的requests_html库，顺利解决js问题。  
### 经过测试发现，服务器验证前端验证码，不需要cookies也可以通过并拿到数据。  
### 在2017-2019年，贾跃亭先生共收获32个法院确定执行的案号，至于每个官司里的多少钱，还有待进一步细数，确实太多太大了，汗哦。  

######python 3.6+   
######PIL  
######pytesseract  

```
from requests_html import HTMLSession, user_agent  
from PIL import Image  
from pytesseract import pytesseract  

//验证码破解用简单的pytesseract示范

while True:
    captchaid = '03eabd0b7dad46d28d197f3ca{}b9c1'.format(str(random.randint(111,999)))
    time.sleep(1)
    while True:
        time.sleep(1)
        url = 'http://zxgk.court.gov.cn/zhzxgk/captcha.do?captchaId={}&random=0.0356847153767{}'.format(captchaid,str(random.randint(11111,99999)))
        # 启动
        session = HTMLSession()
        r = session.get(url,headers={'User-Agent': user_agent(), "Host": 'zxgk.court.gov.cn'})
        with open('./yzm.png','wb') as f:
            f.write(r.content)
        img = Image.open(r'./yzm.png')
        yzm = pytesseract.image_to_string(img).strip()
        yzm = "".join(yzm.split())
        print(yzm)
        if len(yzm) ==4:
            break
    checkurl ='http://zxgk.court.gov.cn/zhzxgk/checkyzm?captchaId={}&pCode={}'.format(captchaid,str(yzm))
    r = session.get(checkurl, headers={'User-Agent': user_agent(), "Host": 'zxgk.court.gov.cn'})
    print(r.text)
    if "1" in str(r.text):
        break

//得到正确验证码后，post执行，一个验证码，可查3-5个人。失效后，可以再去取验证码哦。
post_url = 'http://zxgk.court.gov.cn/zhzxgk/searchZhcx.do'
headers = {'Host': 'zxgk.court.gov.cn',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Origin': 'http://zxgk.court.gov.cn',
           'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3770.80 Safari/537.36',
           'DNT': '1',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Referer': 'http://zxgk.court.gov.cn/zhzxgk/',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9'}
//传参，验证码和验证码的captchaid不可少
data = {
    'searchCourtName': '全国法院（包含地方各级法院）',
    'pName': '贾跃亭',
    'pCode': str(yzm),
    'captchaId': str(captchaid),
    'currentPage': '1',
    'selectCourtArrange': '1',
    'selectCourtId': '0',
    'pCardNum': ''
}
res = requests.post(post_url, data=data, headers=headers)
print(res.text)
```

### 下面是反馈的数据，这里用了“贾跃亭”为搜索关键词，找不到人了，忽然想起他了，别打我，哈  

 
*[{"autoCount":true,"currentPage":1,"delIds":"","filters":"","firstResult":0,"pageSize":10,"privileges":{},"result":[{"ah":"","caseCode":"(2017)京03执644号","caseCreateTime":{"date":3,"day":4,"hours":0,"minutes":0,"month":7,"seconds":0,"time":1501689600000,"timezoneOffset":-480,"year":117},"caseState":"","execCourtBelongM":0,"execCourtBelongS":0,"execCourtId":0,"execCourtName":"","execMoney":"","focusNumber":0,"gistId":"","id":0,"jsonObject":"{\"caseCode\":\"(2017)京03执644号\",\"pname\":\"贾跃亭\",\"caseCreateTime\":\"2017年08月03日\"}","partyCardNum":"","pname":"贾跃亭","sexname":"","urlcpws":"","urltszb":"","xm":"","zxfymc":""},{"ah":"","caseCode":"(2017)京03执608号","caseCreateTime":{"date":17,"day":1,"hours":0,"minutes":0,"month":6,"seconds":0,"time":1500220800000,"timezoneOffset":-480,"year":117},"caseState":"","execCourtBelongM":0,"execCourtBelongS":0,"execCourtId":0,"execCourtName":"","execMoney":"","focusNumber":0,"gistId":"","id":0,"jsonObject":"{\"caseCode\":\"(2017)京03执608号\",\"pname\":\"贾跃亭\",\"caseCreateTime\":\"2017年07月17日\"}","partyCardNum":"","pname":"贾跃亭","sexname":"","urlcpws":"","urltszb":"","xm":"","zxfymc":""},{"ah":"","caseCode":"(2017)京03执607号","caseCreateTime":{"date":17,"day":1,"hours":0,"minutes":0,"month":6,"seconds":0,"time":1500220800000,"timezoneOffset":-480,"year":117},"caseState":"","execCourtBelongM":0,"execCourtBelongS":0,"execCourtId":0,"execCourtName":"","execMoney":"","focusNumber":0,"gistId":"","id":0,"jsonObject":"{\"caseCode\":\"(2017)京03执607号\",\"pname\":\"贾跃亭\",\"caseCreateTime\":\"2017年07月17日\"}","partyCardNum":"","pname":"贾跃亭","sexname":"","urlcpws":"","urltszb":"","xm":"","zxfymc":""},{"ah":"","caseCode":"(2017)京03执755号","caseCreateTime":{"date":28,"day":4,"hours":0,"minutes":0,"month":8,"seconds":0,"time":1506528000000,"timezoneOffset":-480,"year":117},"caseState":"","execCourtBelongM":0,"execCourtBelongS":0,"execCourtId":0,"execCourtName":"","execMoney":"","focusNumber":0,"gistId":"","id":0,"jsonObject":"{\"caseCode\":\"(2017)京03执755号\",\"pname\":\"贾跃亭\",\"caseCreateTime\":\"2017年09月28日\"}","partyCardNum":"","pname":"贾跃亭","sexname":"","urlcpws":"","urltszb":"","xm":"","zxfymc":""},{"ah":"","caseCode":"(2017)京03执610号","caseCreateTime":{"date":17,"day":1,"hours":0,"minutes":0,"month":6,"seconds":0,"time":1500220800000,"timezoneOffset":-480,"year":117},"caseState":"","execCourtBelongM":0,"execCourtBelongS":0,"execCourtId":0,"execCourtName":"","execMoney":"","focusNumber":0,"gistId":"","id":0,"jsonObject":"{\"caseCode\":\"(2017)京03执610号\",\"pname\":\"贾跃亭\",\"caseCreateTime\":\"2017年07月17日\"}","partyCardNum":"","pname":"贾跃亭","sexname":"","urlcpws":"","urltszb":"","xm":"","zxfymc":""},{"ah":"","caseCode":"(2017)京03执646号","caseCreateTime":{"date":8,"day":2,"hours":0,"minutes":0,"month":7,"seconds":0,"time":1502121600000,"timezoneOffset":-480,"year":117},"caseState":"","execCourtBelongM":0,"execCourtBelongS":0,"execCourtId":0,"execCourtName":"","execMoney":"","focusNumber":0,"gistId":"","id":0,"jsonObject":"{\"caseCode\":\"(2017)京03执646号\",\"pname\":\"贾跃亭\",\"caseCreateTime\":\"2017年08月08日\"}","partyCardNum":"","pname":"贾跃亭","sexname":"","urlcpws":"","urltszb":"","xm":"","zxfymc":""},{"ah":"","caseCode":"(2018)京03执60号","caseCreateTime":{"date":9,"day":2,"hours":0,"minutes":0,"month":0,"seconds":0,"time":1515427200000,"timezoneOffset":-480,"year":118},"caseState":"","execCourtBelongM":0,"execCourtBelongS":0,"execCourtId":0,"execCourtName":"","execMoney":"","focusNumber":0,"gistId":"","id":0,"jsonObject":"{\"caseCode\":\"(2018)京03执60号\",\"pname\":\"贾跃亭\",\"caseCreateTime\":\"2018年01月09日\"}","partyCardNum":"","pname":"贾跃亭","sexname":"","urlcpws":"","urltszb":"","xm":"","zxfymc":""},{"ah":"","caseCode":"(2017)京03执753号","caseCreateTime":{"date":28,"day":4,"hours":0,"minutes":0,"month":8,"seconds":0,"time":1506528000000,"timezoneOffset":-480,"year":117},"caseState":"","execCourtBelongM":0,"execCourtBelongS":0,"execCourtId":0,"execCourtName":"","execMoney":"","focusNumber":0,"gistId":"","id":0,"jsonObject":"{\"caseCode\":\"(2017)京03执753号\",\"pname\":\"贾跃亭\",\"caseCreateTime\":\"2017年09月28日\"}","partyCardNum":"","pname":"贾跃亭","sexname":"","urlcpws":"","urltszb":"","xm":"","zxfymc":""},{"ah":"","caseCode":"(2018)苏01执1367号","caseCreateTime":{"date":29,"day":5,"hours":0,"minutes":0,"month":5,"seconds":0,"time":1530201600000,"timezoneOffset":-480,"year":118},"caseState":"","execCourtBelongM":0,"execCourtBelongS":0,"execCourtId":0,"execCourtName":"","execMoney":"","focusNumber":0,"gistId":"","id":0,"jsonObject":"{\"caseCode\":\"(2018)苏01执1367号\",\"pname\":\"贾跃亭\",\"caseCreateTime\":\"2018年06月29日\"}","partyCardNum":"","pname":"贾跃亭","sexname":"","urlcpws":"","urltszb":"","xm":"","zxfymc":""},{"ah":"","caseCode":"(2019)京03执446号","caseCreateTime":{"date":8,"day":1,"hours":0,"minutes":0,"month":3,"seconds":0,"time":1554652800000,"timezoneOffset":-480,"year":119},"caseState":"","execCourtBelongM":0,"execCourtBelongS":0,"execCourtId":0,"execCourtName":"","execMoney":"","focusNumber":0,"gistId":"","id":0,"jsonObject":"{\"caseCode\":\"(2019)京03执446号\",\"pname\":\"贾跃亭\",\"caseCreateTime\":\"2019年04月08日\"}","partyCardNum":"","pname":"贾跃亭","sexname":"","urlcpws":"","urltszb":"","xm":"","zxfymc":""}],"sidx":"","sord":"","totalPage":4,"totalSize":32}]  



### 结果：通过数据分析可见，在2017-2019年，贾跃亭先生共收获32个法院确定执行的案号，预计明年还会持续增加滴哟。  


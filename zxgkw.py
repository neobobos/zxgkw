#encoding=utf-8
from requests_html import HTMLSession, user_agent
from PIL import Image
from pytesseract import pytesseract
import time
import random
import requests

#验证码破解用简单的pytesseract示范

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

#得到正确验证码后，post执行，一个验证码，可查3-5个人。失效后，可以再去取验证码哦。
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
#传参，验证码和验证码的captchaid不可少
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
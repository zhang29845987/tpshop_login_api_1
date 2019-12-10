import requests


# api层

# 登陆
class Api_login(object):
    def __init__(self):
        self.session = requests.session()
        self.login_url = "http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.2116151275612923 "
        self.header={"Content-Type":"application/x-www-form-urlencoded"}
        self.code="http://127.0.0.1/index.php?m=Home&c=User&a=verify&r=0.5721331113793504"

    #获取网站验证码cookie
    def verify(self):
        return self.session.get(self.code)


    #登陆网站
    def login(self, username, password, verify_code):
        data = {"username": username, "password": password, "verify_code": verify_code}
        return self.session.post(url=self.login_url, data=data,headers=self.header)



if __name__ == '__main__':
    ss=Api_login()
    r=ss.verify()
    s=r.cookies
    print(s)
    print(s["PHPSESSID"])
    # text=ss.login("18246640990","123456","8888")
    # print(text.json())

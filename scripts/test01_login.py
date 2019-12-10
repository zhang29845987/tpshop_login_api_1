import unittest
from parameterized import parameterized
from api.api_login import Api_login

from tools.assert_comment import assert_comment
from tools.read_data import login_data


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.api_login = Api_login()

    def setUp(self) -> None:
        self.api_login.verify()

    def tearDown(self) -> None:
        pass

    @parameterized.expand(login_data)
    def test001(self,a,b,c,d):
        f=self.api_login.login(a,b,c)
        assert_comment(self,d,f)



    # def test002(self):
    #     f=self.api_login.login("14789445555","123456","8888")
    #     assert_comment(self,"账号不存在",f)
    #
    # def test003(self):
    #     f=self.api_login.login("18246640990","errror","8888")
    #     assert_comment(self,"密码错误",f)









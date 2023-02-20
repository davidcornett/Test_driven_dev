import unittest
from check_pwd import check_pwd


class TestCheckPWDFunc(unittest.TestCase):

    # test short borderline pwd
    def test1(self):
        pwd = "abc1234"
        check_pwd(pwd)
        self.assertFalse(check_pwd(pwd), msg='Check_PWD_Test({})'.format(pwd))

    # test long borderline pwd
    def test2(self):
        pwd = "abc123456712345671234"
        check_pwd(pwd)
        self.assertFalse(check_pwd(pwd), msg='Check_PWD_Test({})'.format(pwd))

    # test no lowercase letters but correct length
    def test3(self):
        pwd = "abcdefghi"
        check_pwd(pwd)
        self.assertFalse(check_pwd(pwd), msg='Check_PWD_Test({})'.format(pwd))

if __name__ == '__main__':
    unittest.main()
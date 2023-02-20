import unittest
from check_pwd import check_pwd


class TestCheckPWDFunc(unittest.TestCase):

    # test short borderline pwd
    def test1(self):
        pwd = "abc1234"
        self.assertFalse(check_pwd(pwd), msg='Check_PWD_Test({})'.format(pwd))

    # test long borderline pwd
    def test2(self):
        pwd = "abc123456712345671234"
        self.assertFalse(check_pwd(pwd), msg='Check_PWD_Test({})'.format(pwd))

    # test no uppercase letters but correct length
    def test3(self):
        pwd = "abcdefghi"
        self.assertFalse(check_pwd(pwd), msg='Check_PWD_Test({})'.format(pwd))

    # test no lowercase letters but correct length
    def test4(self):
        pwd = "ABCDEFGHI"
        self.assertFalse(check_pwd(pwd), msg='Check_PWD_Test({})'.format(pwd))

    # test numbers only
    def test5(self):
        pwd = "123456789"
        self.assertFalse(check_pwd(pwd), msg='Check_PWD_Test({})'.format(pwd))

    # no digits
    def test6(self):
        pwd = "abCdefghi"
        self.assertFalse(check_pwd(pwd), msg='Check_PWD_Test({})'.format(pwd))

    # no special chars: ~`!@#$%^&*()_+-=
    def test7(self):
        pwd = "abCdefg2i"
        self.assertFalse(check_pwd(pwd), msg='Check_PWD_Test({})'.format(pwd))

    # use of special char % (should return TRUE)
    def test8(self):
        pwd = "%bCd%fg2i"
        self.assertTrue(check_pwd(pwd), msg='Check_PWD_Test({})'.format(pwd))



if __name__ == '__main__':
    unittest.main()

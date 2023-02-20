import unittest
from check_pwd import check_pwd


class TestCheckPWDFunc(unittest.TestCase):

    # test short borderline pwd
    def test1(self):
        pwd = "abc1234"
        check_pwd(pwd)
        self.assertFalse(check_pwd(pwd), msg='Check_PWD_Test({})'.format(pwd))




if __name__ == '__main__':
    unittest.main()
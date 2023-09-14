import unittest
import utils

REVERSED_ANSWER_SET = [False, False, False, 4321, 1, 21, False, False]
BINARY_ANSWER_SET = [False, False, False, '0b10011010010', '0b1010', '0b1100', False, False]
OCTAL_ANSWER_SET = [False, False, False, '0o2322', '0o12', '0o14', False, False]


class UtilsTest(unittest.TestCase):
    def test_reverse_test_case(self):
        self.obj = utils.utils()
        self.res = self.obj.execute_code()
        test_res = self.res[0]
        self.assertEqual(test_res, REVERSED_ANSWER_SET)

    def test_binary_formatter_case(self):
        self.obj = utils.utils()
        self.res = self.obj.execute_code()
        binary_res = self.res[1]
        self.assertEqual(binary_res, BINARY_ANSWER_SET)

    def test_octal_formatter_case(self):
        self.obj = utils.utils()
        self.res = self.obj.execute_code()
        octal_res = self.res[2]
        self.assertEqual(octal_res, OCTAL_ANSWER_SET)


def util_class_tester():
    tester = unittest.TestSuite()
    tester.addTests([UtilsTest("test_reverse_test_case"), UtilsTest("test_binary_formatter_case"), UtilsTest("test_octal_formatter_case")])
    #tester.addTest(UtilsTest('test_binary_formatter_case'))
    return tester


if __name__ == "__main__":
    begin_test = unittest.TextTestRunner()
    begin_test.run(util_class_tester())

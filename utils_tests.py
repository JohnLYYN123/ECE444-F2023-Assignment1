import utils

TEST_SET = ["1234", "string", 12.34, 1234, 10, 12, 1.4, "31314151"]
REVERSED_ANSWER_SET = [False, False, False, 4321, 1, 21, False, False]
BINARY_ANSWER_SET = [False, False, False, '0b10011010010', '0b1010', '0b1100', False, False]
OCTAL_ANSWER_SET = [False, False, False, '0o2322', '0o12', '0o14', False, False]


def reverse_test():
    print("___________PERFORMING REVERSE TEST___________")
    obj = utils.utils()
    reversed_list = (obj.execute_code())[0]
    for res, ans, case in zip(reversed_list, REVERSED_ANSWER_SET, TEST_SET):
        print("\nCase of " + str(case) + ": ")
        if res == ans:
            print("PASS")
        else:
            print("FAIL")


def formatter_test():
    print("___________PERFORMING FORMATTER TEST___________")
    obj = utils.utils()
    bi_comment = "BINARY TEST: "
    oct_comment = "OCTAL TEST: "
    binary_list = (obj.execute_code())[1]
    octal_list = (obj.execute_code())[2]
    for bi_res, oct_res, bi_ans, oct_ans, case in zip(binary_list, octal_list, BINARY_ANSWER_SET, OCTAL_ANSWER_SET, TEST_SET):
        print("\nCase of " + str(case) + ": ")

        # compare binary results with answer set
        if bi_res == bi_ans:
            print(bi_comment + "PASS")
        else:
            print(bi_comment + "FAIL")

        # compare octal results with answer set
        if oct_res == oct_ans:
            print(oct_comment + "PASS")
        else:
            print(oct_comment + "FAIL")

    return None


if __name__ == "__main__":
    reverse_test()
    formatter_test()


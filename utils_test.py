import utils
#import itertools

TEST_SET = ["1234", "string", 12.34, 1234, 10, 12, 1.4, "31314151"]
REVERSED_ANSWER_SET = [False, False, False, 4321, 1, 21, False, False]


def reverse_test():
    obj = utils.utils()
    reversed_list = obj.execute_code()
    for res, ans, case in zip(reversed_list, REVERSED_ANSWER_SET, TEST_SET):
        print("\nCase of " + str(case) + ": ")
        if res == ans:
            print("PASS")
        else:
            print("FAIL")



if __name__ == "__main__":
    reverse_test()


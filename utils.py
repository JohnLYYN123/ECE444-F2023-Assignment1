# This is the utils class

TEST_SET = ["1234", "string", 12.34, 1234, 10, 12, 1.4, "31314151"]

class utils:
    def execute_code(self):
        rev_result = []
        for i in TEST_SET:
            rev_result.append(self.reversed(i))
        return rev_result

    def reversed(self, number):
        # if the given is not of type integer (int), we print a msg and we return false
        if isinstance(number, int) is False:
            # print("the given parameter is not an integer")
            return False

        rev_num = 0
        while number != 0:
            digit = number % 10
            rev_num = rev_num * 10 + digit
            number = int(number / 10)

        return rev_num


if __name__ == "__main__":
    obj = utils()
    rev_list = obj.execute_code()
    print("the reversed list is " + str(rev_list))

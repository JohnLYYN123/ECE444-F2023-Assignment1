# This is the utils class
# commit 3
TEST_SET = ["1234", "string", 12.34, 1234, 10, 12, 1.4, "31314151"]


class utils:
    def execute_code(self):
        rev_res = []
        formatter_res = []
        for i in TEST_SET:
            rev_res.append(self.reversed(i))
            formatter_res.append(self.formatter(i))

        binary_res = []
        octal_res = []
        for i in formatter_res:
            if i is not False:
                binary_res.append(i[0])
                octal_res.append(i[1])
            else:
                binary_res.append(i)
                octal_res.append(i)

        return [rev_res, binary_res, octal_res]

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

    def formatter(self, number):
        if isinstance(number, int) is False:
            # print("the given parameter is not an integer")
            return False

        bi_num = bin(number)
        oct_num = oct(number)
        return [bi_num, oct_num]


if __name__ == "__main__":
    obj = utils()
    res_list = obj.execute_code()
    print(res_list)

class MyNumber:
    def init(self):
        pass

    def check_numbers(self):
        r = int(input("How many values do you want? "))

        for i in range(0, r):
            x = int(input("Enter x value: \n"))

            if x > 0 & x <= 10:
                if x % 2 == 0:
                    print(x, " is even")
                else:
                    print(x, " is odd")


m = MyNumber()
m.check_numbers()

# Snack = https://www.urionlinejudge.com.br/judge/en/problems/view/1038
from sys import stdin

class Switcher(object):
    def numbers_to_code_and_amount(self, code, amount):
        """Dispatch method"""
        code_name = 'code_' + str(code)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, code_name, lambda: "Invalid CODE!!!")
        # Call the method as we return it
        return method() * amount
 
    def code_1(self):
        return 4.00
 
    def code_2(self):
        return 4.50
 
    def code_3(self):
        return 5.00
    
    def code_4(self):
        return 2.00

    def code_5(self):
        return 1.50


numsArr = [int(x) for x in stdin.readline().split(" ")]
a=Switcher()
price = a.numbers_to_code_and_amount(numsArr[0], numsArr[1])
print("Total: R$ {:.2f}".format(price))


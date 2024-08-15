class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar_bill = 0
        ten_dollar_bill = 0
        for bill in bills:
            if bill == 5:
                five_dollar_bill += 1
            elif bill == 10:
                if five_dollar_bill == 0:
                    return False
                else:
                    five_dollar_bill -= 1
                ten_dollar_bill += 1
            else:
                if (ten_dollar_bill == 0 and five_dollar_bill >= 3):
                    five_dollar_bill -= 3
                elif (ten_dollar_bill >=1 and five_dollar_bill >= 1):
                    ten_dollar_bill -= 1
                    five_dollar_bill -= 1
                else:
                    return False
        return True
                 
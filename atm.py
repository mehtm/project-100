class atm():
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber
    def CashWithdrawal(self):
        print("cash withdrawn")
    def BalanceEnquiry(self):
        print("balance enquiry")

card = atm(345,123)
card.CashWithdrawal()
card.BalanceEnquiry()


class MasterFinances:
    def __init__(self):
        self.regular_outgoings = {}
        self.regular_incomings = {}
        self.general_account = GeneralAccount
        self.current_funds = float(0)
        self.bank_accounts = {}

    def view_current_funds(self):
        return f"Current funds in all accounts: £{self.current_funds}"
    
    def view_bank_accounts(self):
        if self.bank_accounts:
            bank_str = "==> Bank accounts:\n"
            for bank in self.bank_accounts:
                bank_str + f"\n{bank.name}: £{bank.current_funds}"
        return bank_str
        
class GeneralAccount:
    def __init__(self, name='All Accounts', current_funds=0):
        self.name = name
        self.current_funds = float(current_funds)
        self.regular_outgoings = {}
        self.regular_incomings = {}
        self.bank_accounts = {}
        #self.master = master - for updating balances?
    
    def add_funds(self, number):
        self.current_funds += float(number)
        return self.current_funds

    def subtract_funds(self, number):
        self.current_funds -= float(number)
        return self.current_funds

    def view_current_funds(self):
        return f"Current funds in {self.name}: £{self.current_funds}"
    
    def add_regular_outgoing(self):
        pass

    def add_bank_account(self, name, current_funds=0):
        self.bank_accounts[name.title()] = BankAccount(name, current_funds)


class BankAccount(GeneralAccount):
    def __init__(self, name='All Accounts'):
        super().__init__(name, current_funds=0)

        

class Outgoing:
    def __init__(self, name, cost, date):
        self.name = str(name)
        self.cost = float(cost)
        self.date = date #datetime obj? timedelta?

class Spend:
    def __init__(self, name, cost):
        self.name = str(name)
        self.cost = float(cost)

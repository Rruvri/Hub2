from datetimetracking import *


#remember to update datetimetracking with a better 'current date' i.e. change to 'current_date_str' and have current date point at dt object
class MasterFinances:
    def __init__(self):
        self.current_bank_funds = float(0)
        self.bank_accounts = {}
        self.cash = float(0)
        self.owed = []

    def get_current_funds(self):
        if self.bank_accounts:
            total = float(0)
            for acc in self.bank_accounts:
                total += self.bank_accounts[acc].current_funds
            self.current_bank_funds = total
        
        return f"Current funds in all accounts: £{self.current_bank_funds}"
    
    def get_bank_accounts(self):
        if self.bank_accounts:
            bank_str = "==> Bank accounts:\n"
            for bank in self.bank_accounts:
                bank_str + f"\n{bank.name}: £{bank.current_funds}"
                bank_str = bank_str + f"\n{bank}: £{self.bank_accounts[bank].current_funds}"
            return bank_str
        else:
            return None
    
    
    def get_cash(self):
        if self.cash:
            return f"Current cash: £{self.cash}"
        else:
            return None
    
    
    '''
    def view_all_funds(self):
        total = self.view_current_funds() + "\n"
        if self.view_cash():
            total = total + self.view_cash() + "\n"
        if self.view_bank_accounts():
            total = total + self.view_bank_accounts() + "\n"
        return total
    '''



        
    def get_all_funds(self):
        total = self.get_current_funds() + "\n"
        if self.get_cash():
            total = total + self.get_cash() + "\n"
        if self.get_bank_accounts():
            total = total + self.get_bank_accounts() + "\n"
        return total
    
    def create_owed_entry(self):
        name = input("Enter name of payee/ source: ")
        amount = input("Enter amount: ")
        self.owed.append(Gain(name, amount))
    
    def create_bank_account(self):
        name = input("Enter name of bank: ").title()
        current_funds = float(input("Enter current funds in bank, or [return] to  do later"))
        #if current_funds == '' or not type(current_funds) == float: #test this, not sure if that works
        #    current_funds = float(0)
        
        self.bank_accounts[name] = BankAccount(name, current_funds)

    def auto_check_finances(self, d=date.today()):
        checked_finances = []

        if self.bank_accounts:
            for acc in self.bank_accounts:
                acc_check = self.bank_accounts[acc].auto_check_bank_account(d)
                if acc_check:
                    checked_finances.append(acc_check)

        
        return checked_finances
        




        
class BankAccount:
    def __init__(self, name, current_funds=0):
        self.name = name.title()
        self.current_funds = float(current_funds)
        self.regular_outgoings = {}
        self.regular_incomings = {}
        self.history = {}
        
        #self.master = master - for updating balances?
    
    def add_funds(self, number, source, date):
        self.current_funds += float(number)
        
        #if date in self.history.keys():
            

        return self.current_funds

    def subtract_funds(self, spend, date=date.today()):
        
        self.check_hist_log(date)

        self.current_funds -= spend.cost
        if not spend.date:
            spend.date = date
        
        self.history[date].append(spend)
        return self.current_funds
    
    #above two could be merged with new spend and gain subclasses

    def get_current_funds(self):
        return f"Current funds in {self.name}: £{self.current_funds}"
    
    def add_regular_outgoing(self):
        pass

    def add_bank_account(self, name, current_funds=0):
        self.bank_accounts[name.title()] = BankAccount(name, current_funds)




    def create_regular_outgoing(self):
        name = input("Enter name of regular outgoing: ").title()
        cost = float(input("Enter cost of outgoing: "))
        date_ref = int(input("Enter the date this outgoing occurs on (no option for alternative date formats i.e. every Tuesday, yet...): "))
        
        if not self.regular_outgoings[date_ref]:
            self.regular_outgoings[date_ref] = []
        self.regular_outgoings[date_ref].append(Outgoing(name, cost, date_ref, self.name))


    def check_hist_log(self, date):
        if not self.history[date]:
            self.history[date] = []
    
    def auto_check_bank_account(self, d):
        if d <= date.today():
            self.check_hist_log(d)

        check_d = int(d.day())

        if self.regular_outgoings:
            if check_d in self.regular_outgoings.keys():
                for spend in self.regular_outgoings[check_d]:
                    self.subtract_funds(spend, d)
                return self.regular_outgoings[check_d]
        return None
            

class Outgoing:
    def __init__(self, name, cost, date, account):
        self.name = str(name)
        self.cost = float(cost)
        self.date = date #datetime obj? timedelta?
        self.account = account


'''
class Spend:
    def __init__(self, name, cost, date_ref, account):
        self.name = name.title()
        self.spend = Spend(name, cost)
        self.date_ref = int(date_ref) #datetime obj? timedelta?
        self.account = account.title()
'''
    
class MoneyObj:
    def __init__(self, name, cost, date=None):
        self.name = str(name).title()
        self.cost = float(cost)
        if date:
            self.date = date


class Spend(MoneyObj):
    def __init__(self, name, cost, date=None):
        super().__init__(name, cost, date)

class Gain(MoneyObj):
    def __init__(self, name, cost, date=None):
        super().__init__(name, cost, date)




master = MasterFinances()

def finances():
    while True:
        
        print(master.get_all_funds())
        
        
        menu = {'b': master.create_bank_account,
                'f': master.get_current_funds}
    
        choice = input("enter choice: ")

        menu[choice]()

finances()
        

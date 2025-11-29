class Person:
    def __init__(self,name):
        self.name=name
        self.balance=0

class Expense:
    def __init__(self,paid_by,amount,description,participants):
        self.paid_by=paid_by
        self.amount=amount
        self.description=description
        self.participants=participants

class ExpenseManager:
    def __init__(self):
        self.people={}
        self.expenses=[]
        
        
    def add_person(self,name):

        if name in self.people:
            print("Person exits")
            return
        
        self.people[name]=Person(name)

    def add_expense(self,paid_by,amount,description,participants):

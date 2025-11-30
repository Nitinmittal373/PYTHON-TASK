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
            print("Person exists")
            return
        
        self.people[name]=Person(name)
        print(f"{name} added")

        f=open("expenses.txt", "a") 
        f.write(f"Person Added: {name}\n")
        f.close()

    def add_expense(self,paid_by,amount,description,participants):
        if paid_by not in self.people:
            print("Not in the list.Add person first")
            return
        
        for p in participants:
            if p not in self.people:
                print(f"Participant {p} not found.Add person.")
                return 
            
        split_amount=amount/len(participants)

        for p in participants:
            if p!=paid_by:
                self.people[p].balance-=split_amount
                self.people[paid_by].balance+=split_amount

        print("Expense added sucessfully")        

        f=open("expenses.txt", "a") 
        f.write(f"Expense: {paid_by} paid {amount} for '{description}' split among {participants}\n")
        f.close()

    def Show_expense(self):
        print("\nBalances: ")
        f=open("expenses.txt", "a")
        f.write("\nBalance:\n")
        f.close()

        for name,person in self.people.items():
            if person.balance>0:
                print(f"{name} will receive {person.balance:.2f}\n")
                f=open("expenses.txt", "a") 
                f.write(f"{name} will receive {person.balance:.2f}\n")
                f.close()
            elif person.balance<0:
                print(f"{name} owes {-person.balance:.2f}\n")
                f=open("expenses.txt", "a") 
                f.write(f"{name} owes {-person.balance:.2f}\n")
                f.close()

            else:
                print(f"{name} is settled")
                f=open("expenses.txt", "a")
                f.write(f"{name} is settled.\n")
                f.close()



manager=ExpenseManager()

while True:
    print("1. Add person")
    print("2. Add Expense")
    print("3. Show Expense")
    print("4. Exit")
    
    option = int(input("Enter option: "))

    if option == 1:
        name=input("Enter person name: ")
        manager.add_person(name)

    elif option==2:
        paid_by=input("Who paid the bill? ")
        amount= float(input("Enter the amount: "))
        desc=input("What is the purpose? ")
        participants=[]
        count = int(input("How many participants? "))
        for i in range(count):
            name=input("Enter the name: ")
            participants.append(name)

        manager.add_expense(paid_by,amount,desc,participants)

    elif option == 3:
        manager.Show_expense() 

    elif option == 4:
        print("Exiting")
        break

    else:
        print("Not a correct option chosen")    


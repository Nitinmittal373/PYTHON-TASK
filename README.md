# PYTHON-TASK 
About the Project:
The project is based on Object-Oriented Programming(OOPs) in Python,using classes,objects,encapsulation,and relationships between objects.The name of the project is "EXPENSE SPLITTER".It is used to calculate and split expenses among people,which helps in managing money and knowing who owes how much money to the person who paid the bill.
This project firstly add the person name one by one.And then user have to type in the details of who paid the bill, what is the total amount, description and people involved in the split. After giving all this information system calculates how much money each person owe to whom and exact settlement amounts.And finally shows all the expenses.


**Classes used**


Explanation of the classes used in my project:
In this project, I have used three classes: Person, Expense, and ExpenseManager.
The Person class stores the name of each participant and their balance (initially 0).
The Expense class stores details of each expense such as who paid, the amount, description, and the participants involved.
The ExpenseManager class is the main class which contains a dictionary for storing Person objects and a list for storing Expense objects. It also includes methods like add_person, add_expense, view_expenses, and show_balances, which manage all the operations of the project.


**Sample Input & Output**


Sample input and output:

Input:
1
Enter person name: Nitin
1
Enter person name: Aman
1
Enter person name: Rohit
2
Who paid the bill? Nitin
Enter the amount: 900
What is the purpose? Dinner
How many participants? 3
Enter the name: Nitin
Enter the name: Aman
Enter the name: Rohit
3
4

Output:
1. Add person
2. Add Expense
3. Show Expense
4. Exit
Enter option: 1
Enter person name: Nitin
Nitin added

1. Add person
2. Add Expense
3. Show Expense
4. Exit
Enter option: 1
Enter person name: Aman
Aman added

1. Add person
2. Add Expense
3. Show Expense
4. Exit
Enter option: 1
Enter person name: Rohit
Rohit added

1. Add person
2. Add Expense
3. Show Expense
4. Exit
Enter option: 2
Who paid the bill? Nitin
Enter the amount: 900
What is the purpose? Dinner
How many participants? 3
Enter the name: Nitin
Enter the name: Aman
Enter the name: Rohit
Expense added successfully

1. Add person
2. Add Expense
3. Show Expense
4. Exit
Enter option: 3
Nitin will receive 600.00

Aman owes 300.00

Rohit owes 300.00

1. Add person
2. Add Expense
3. Show Expense
4. Exit
Enter option: 4
Exiting

This is how my project runs.



import datetime
from typing import List
from expense import Epense


def main():
    print(f"Theo doi chi phi")
    expense_file_path = "expense.csv"
    
    budget = 2000
    
    expense =  get_user_expense()
    
    
    save_expense_to_file(expense, expense_file_path)
    
    summarize_expenses(expense_file_path, budget)
    

def get_user_expense():
    print("chi phi nguoi dung: ")
    expense_name =  input("ten chi phi: ")
    expense_amount = float(input("nhap tong chi phi: "))
  
    expense_categories = [
        "Food", "Home", "Work", "Fun", "Misc" 
    ]
    
    while True:
        print("select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")
            
        value_range = f"[1 - {len(expense_categories)}]"
        
        selected_index = int(input(f"nhap so loai {value_range}: ")) - 1
        
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Epense(name = expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("loai ko ton tai, thu lai lan nua")
            
        
        
    
    
def save_expense_to_file(expense: Epense, expense_file_path): 
    print(f"luu chi phi: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    print(f"tom tat chi phi: ")
    expenses: List[Epense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
           
            expense_name, expense_amount, expense_category = line.strip().split(",")
          
            line_expense = Epense(
                name= expense_name, amount= float(expense_amount), category=expense_category
            )
            print(line_expense)
            expenses.append(line_expense)
            
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("chi phi boi loai")
    for key, amount in amount_by_category.items():
        print(f"{key}: {amount: .2f}")
    
    total_spent = sum([x.amount for x in expenses])
    
    print(f"b da tieu {total_spent:.2f} trong thang")
    
    remaining_budget = budget - total_spent
    
    print(f"budget remainning: {total_spent:.2f}")
    
    now = datetime.datetime.now()
    
    days_in_month = callable.monthrange(now.year, now.month)[1]
    
    remaining_days = days_in_month - now.day
    print("remaining day in the current moth:", remaining_days)
    daily_budget = remaining_budget/ remaining_days
    print(f"budget per day: {daily_budget:.2f}")
    
    
    
if __name__ == "__main__":
    main()
import pandas as pd
import datetime
import numpy
import os

x = datetime.datetime.now()

date = x.strftime("%x")
print(date)

while True:
    data_old = pd.read_csv("data2.csv")
    df = pd.DataFrame(data_old, columns=["DATE", "AMOUNT", "TYPE", "REASON", "NOTE"])
    print(df)
    data_entry = input("Enter expense and its type (EX: 150T): ").strip()
    if data_entry == "exit":
        break
    expense_type = data_entry[-1]
    expense = data_entry[:len(data_entry)-1]

    reason = input("Reason of expense: ")
    note = input("Note: ")
    if expense_type == "T":
        expense_type = "TICKET"
    elif expense_type == "R":
        expense_type = "RECHARGE"
    elif expense_type == "P":
        expense_type = "PAYMENT"
    elif expense_type == "F":
        expense_type = "FOOD"
    elif expense_type == "S":
        expense_type = "SHOPPING"
    else:
        expense_type = pd.NaN()

    data_set = {
            "DATE" : date,
            "AMOUNT" : expense,
            "TYPE" : expense_type,
            "REASON" : reason,
            "NOTE" : note
        }
    #print(data_set)
    new_data = pd.DataFrame(data_set,index=[0], columns=["DATE", "AMOUNT", "TYPE", "REASON", "NOTE"])
    #print(new_data)
    os.system("cls")
    try:
        new_data.to_csv("data2.csv", mode="a", index=False, header=False)
    except:
        print("No File Found")
    else:
        print("\n\033[92m---Data entered successfully!---\033[0m\n\n\n")

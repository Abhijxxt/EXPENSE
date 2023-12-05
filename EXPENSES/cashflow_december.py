import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data2.csv")
df = pd.DataFrame(data, columns=["DATE","AMOUNT","TYPE","REASON","NOTE"])
#print(df[df["TYPE"] == "FOOD"])
print(df)
'''
x = df["DATE"]
y = df["AMOUNT"]

plt.plot(x,y,'o')
plt.show()
'''
food=0
ticket=0
payment=0
shopping=0
recharge=0

prev_date = df.iloc[0]["DATE"]
print(prev_date)

for i in range(len(df)):
    line_data = df.iloc[i]
    if line_data["DATE"] == prev_date:
        if line_data["TYPE"] == "FOOD":
            food = food + int(line_data["AMOUNT"])
        elif line_data["TYPE"] == "TICKET":
            ticket = ticket + int(line_data["AMOUNT"])
        elif line_data["TYPE"] == "PAYMENT":
             payment = payment + int(line_data["AMOUNT"])
        elif line_data["TYPE"] == "SHOPPING":
            print("S")
            shopping = shopping + int(line_data["AMOUNT"])
        elif line_data["TYPE"] == "RECHARGE":
            recharge = recharge + int(line_data["AMOUNT"])
    else:
        if food != 0:
            plt.plot(prev_date, food, "o", color="orange")
        if ticket !=0:
            plt.plot(prev_date, ticket, "o", color="black")
        if payment !=0:
            plt.plot(prev_date, payment, "o", color="blue")
        if shopping !=0:
            plt.plot(prev_date, shopping, "o", color="red")
        if recharge !=0:
            plt.plot(prev_date, recharge, "o", color="olive")
        prev_date = line_data["DATE"]

        if line_data["TYPE"] == "FOOD":
            food = food + int(line_data["AMOUNT"])
        elif line_data["TYPE"] == "TICKET":
            ticket = ticket + int(line_data["AMOUNT"])
        elif line_data["TYPE"] == "PAYMENT":
             payment = payment + int(line_data["AMOUNT"])
        elif line_data["TYPE"] == "SHOPPING":
            print("S")
            shopping = shopping + int(line_data["AMOUNT"])
        elif line_data["TYPE"] == "RECHARGE":
            recharge = recharge + int(line_data["AMOUNT"])
        
        food,ticket,payment,shopping,recharge = 0,0,0,0,0
        

plt.show()

    
'''
for i in range(len(df)):
    line_data = df.iloc[i]
    if line_data["TYPE"] == "FOOD":
        plt.plot(line_data["DATE"],line_data["AMOUNT"],"o", color="orange")
    elif line_data["TYPE"] == "TICKET":
        plt.plot(line_data["DATE"],line_data["AMOUNT"],"o", color="black")
    elif line_data["TYPE"] == "PAYMENT":
        plt.plot(line_data["DATE"],line_data["AMOUNT"],"o", color="blue")
    elif line_data["TYPE"] == "SHOPPING":
        plt.plot(line_data["DATE"],line_data["AMOUNT"],"o", color="red")
    elif line_data["TYPE"] == "RECHARGE":
        plt.plot(line_data["DATE"],line_data["AMOUNT"],"o", color="olive")

'''

#This program calculate sales commsion

#create a variable to control the loop

#calculate a series of commissions
keep_going = "y"
while keep_going == "y":
#Get a salesperson's sales and comission rate

#calcaulate the comission
#display the commission
#See if the user want to do another one 

    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate:'))
    commision = sales*comm_rate
    print(f"The commision is $' {commision:,.2f}")
    keep_going = input("Do you want to calculate another commision (Enter y for yes): ")
    

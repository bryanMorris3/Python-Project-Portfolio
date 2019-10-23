#Bryan Morris
#9/19
#Cash Register
#Declare and initialize variables
numItems = 100
costPerItem = 3.75
taxRate = .09
#Calculate and store the sub-total
subTotal = numItems * costPerItem
#Calculate the amount of tax and store the result
taxAmount = subTotal * taxRate
#Calculate the total price and store the amount
totalPrice = taxAmount + subTotal
#Seperaters for print Statement
sep1 = ": "
sep2 = ": $"
#Show the full receipt to the screen
print("----SALES RECEIPT----")
print("Number of items         " , numItems, sep = sep1)
print("Cost per item             " ,costPerItem, sep = sep2)
print("Tax rate                    " , taxRate, sep = sep1)
print("Tax amount                ", taxAmount, sep = sep2)
print("Subtotal                    ", subTotal, sep = sep2)
print("TOTAL SALE PRICE " , totalPrice, sep = sep2)

input()

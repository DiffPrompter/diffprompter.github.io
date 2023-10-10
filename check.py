#Input data

cno=int(input("Enter consumer number:"))
pc=int(input("Enter power consumed:"))

bill_amt = 0

if pc>0 and pc<=100:
    bill_amt=pc*1
elif pc>100 and pc<=300:
    bill_amt=100+(pc-100)*1.25
elif pc>300 and pc<=500:
    bill_amt=350+(pc-300)*1.50
elif pc>500:
    bill_amt=650+(pc-500)*1.75
else:
    print("Invalid Power Consumed Unit")

print("ABC Power Company LTD.")
print("~"*60)
print("Consumer Number:",cno)
print("Consumer Units:",pc)
print("______")
print("Bill amount:",bill_amt)
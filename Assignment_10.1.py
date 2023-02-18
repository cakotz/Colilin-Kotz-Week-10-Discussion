import csv


print("Enter a file: ")
fileName = f"{input()}.csv"
print("Enter your name: ")
userName = input()
print("Enter your street address: ")
address = input()
print("Enter your phone number: ")
phone = input()

userInfo = [userName, address, phone]

with open(fileName, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(userInfo)

with open(fileName, newline="") as csvfile:
    reader = csv.reader(csvfile)
    print(next(reader))

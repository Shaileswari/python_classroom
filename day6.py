# total=0
# for i in range(1,6):
#     total+=i
# print(total)


correct_password="admin123"
for attempt in range(1,4):
    password=input("Enter your password:")
    if password==correct_password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")
        if attempt==3:
            print("Account Locked")



# current_users=int(input("Enter number of current users:"))
# new_users=50
# minutes=2
# total_users=current_users+(new_users*2)
# if total_users>1000:
#     print("Launch new server instance")
# else:
#     print("Server stable")


# uptime=97.5
# bill=50000
# if uptime>=99.9:
#     refund=0
# elif uptime>=98:
#     refund=bill*0.10
# else:
#     refund=bill*0.25
# print("Refund Amount:",refund)


weight=float(input("Enter weight in kg:"))
height=float(input("Enter height in metres:"))
bmi=weight/(height**2)
if bmi<18.5:
    category="underweight"
elif bmi<25:
    category="normal"
elif bmi<30:
    category="overweight"
else:
    category="obese"
print("BMI:",bmi)
print("category:",category)










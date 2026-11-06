# conditional statements

# rama_height=1.3
# raja_height=1.7
# if rama_height>raja_height:
#     print("Rama is taller")
# else:
#     print("Raja is taller")


total=float(input("Enter total purchase:"))
if total>=1000:
    discount=total*0.10
    final_amount=total-discount
    print("Discount applied:",discount)
    print("Final amount to pay:",final_amount)
else:
    print("No discount applied")
    print("Total amount",total)



items = ["1. Vanilla", "2. Chocolate", "3. Strawberry", "4. Mango", "5. Black Current", "6. Exit"]

van_typ = ["1. Regular Vanilla", "2. Vanilla with choco chips"]
choco_typ = ["1. Dark Chocolate", "2. Chocolate Fudge"]
str_typ = ["1. Fresh Strawberry", "2. Strawberry Cream"]
mng_typ = ["1. Mango Classic", "2. Mango Kulfi"]
blc_typ = ["1. Classic Black Current", "2. Black Current Sundae"]

# Display main menu
for i in items:
    print(i)

sel_items = int(input("Select flavour: "))

if sel_items == 1:
    print("Vanilla selected")
    for i in van_typ:
        print(i)
    van = int(input("Select vanilla flavour: "))
    if van == 1:
        print("Regular Vanilla selected")
    elif van == 2:
        print("Vanilla with choco chips selected")
    else:
        print("Invalid option")

elif sel_items == 2:
    print("Chocolate selected")
    for i in choco_typ:
        print(i)
    choco = int(input("Select chocolate flavour: "))
    if choco == 1:
        print("Dark Chocolate selected")
    elif choco == 2:
        print("Chocolate Fudge selected")
    else:
        print("Invalid option")

elif sel_items == 3:
    print("Strawberry selected")
    for i in str_typ:
        print(i)
    st = int(input("Select strawberry flavour: "))
    if st == 1:
        print("Fresh Strawberry selected")
    elif st == 2:
        print("Strawberry Cream selected")
    else:
        print("Invalid option")

elif sel_items == 4:
    print("Mango selected")
    for i in mng_typ:
        print(i)
    mng = int(input("Select mango flavour: "))
    if mng == 1:
        print("Mango Classic selected")
    elif mng == 2:
        print("Mango Kulfi selected")
    else:
        print("Invalid option")

elif sel_items == 5:
    print("Black Current selected")
    for i in blc_typ:
        print(i)
    blc = int(input("Select black current flavour: "))
    if blc == 1:
        print("Classic Black Current selected")
    elif blc == 2:
        print("Black Current Sundae selected")
    else:
        print("Invalid option")

elif sel_items == 6:
    print("Thank you 🍦 Visit again!")

else:
    print("Invalid choice")

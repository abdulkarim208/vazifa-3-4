def parol_yetarlimi(parol):
    if len(parol) >= 8:
        return True
    else:
        return False

parol = input("Parolni kiriting: ")
print(parol_yetarlimi(parol))
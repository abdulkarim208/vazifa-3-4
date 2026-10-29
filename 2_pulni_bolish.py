def pulni_bol(umumiy_pul, odamlar):
    return umumiy_pul / odamlar

umimiy_pul = int(input("umimiy pulni kiriting: "))
odamlar = int(input("odamlar sonini kiriting: "))

print(pulni_bol(umimiy_pul, odamlar))
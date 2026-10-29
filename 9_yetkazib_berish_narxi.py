def yetkazish_narxi(masofa):
    if masofa <= 5:
        return 10000
    else:
        return 20000

masofa = float(input("masofani kiriting: "))

print(yetkazish_narxi(masofa))
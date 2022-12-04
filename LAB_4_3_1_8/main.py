def czy_przestepny(rok):
    if rok%4==0: return True

def dni_w_miesiacu(rok, miesiac):
    if miesiac == 2:
        if czy_przestepny(rok):
            return 29
        else:
            return 28
    elif miesiac in (4, 6, 9, 11):
        return 30
    elif miesiac in (1, 3, 5, 7, 8, 10, 12):
        return 31
    else:
        return 0

def dzien_w_roku(rok, miesiac, dzien):
    if dzien > dni_w_miesiacu(rok, miesiac) or miesiac > 12:
        return None
    else:
        suma = dzien
        for i in range(0, miesiac):
            suma += dni_w_miesiacu(rok, i)
        return suma


print(dzien_w_roku(2000,12,31))
print(dzien_w_roku(2001,12,31))
print(dzien_w_roku(2021,8,22))
print(dzien_w_roku(1996,16,5))
print(dzien_w_roku(2018,4,31))
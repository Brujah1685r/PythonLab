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



testuj_lata = [1900, 2001, 2016, 1987]
testuj_miesiace = [2, 2, 1, 11]
testuj_wynik = [29, 28, 31, 30]

for i in range(len(testuj_lata)):
	r = testuj_lata[i]
	m = testuj_miesiace[i]
	print(r, m, "-> ", end="")
	wynik = dni_w_miesiacu(r, m)
	if wynik == testuj_wynik[i]:
		print("OK")
	else:
		print("Nie powiodło się")

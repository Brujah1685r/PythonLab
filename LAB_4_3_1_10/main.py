galonTOlitr = 3.785411784
milaTOkm = 1.609344

def l100kmtompg(litry):
    x = 100 * 1 * galonTOlitr
    y = litry * milaTOkm * 1
    wynik = x/y
    return wynik

def mpgtol100km(mile):
    x = 100 * 1 * galonTOlitr
    y = mile * milaTOkm * 1
    wynik = x / y
    return wynik


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

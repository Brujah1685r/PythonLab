def czy_pierwsza(liczba):
    iloscDzielnikow = 0
    for i in range(1, liczba):
        if liczba % i == 0: iloscDzielnikow += 1
    if iloscDzielnikow < 3: return liczba

for i in range(1, 125):
	if czy_pierwsza(i + 1):
			print(i + 1, end=" ")


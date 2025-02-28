def wspolczynnikKorelacji (sredniaX, sredniaY, kolumnaX, kolumnaY, irysy):
    licznik = 0
    for i in range(irysy.shape[0]):
        roznicaX = irysy.iloc[i, kolumnaX] - sredniaX
        roznicaY = irysy.iloc[i, kolumnaY] - sredniaY
        licznik += (roznicaX * roznicaY)

    mianownik1 = 0
    mianownik2 = 0
    for i in range(irysy.shape[0]):
        roznicaX = irysy.iloc[i, kolumnaX] - sredniaX
        roznicaY = irysy.iloc[i, kolumnaY] - sredniaY
        mianownik1 += roznicaX ** 2
        mianownik2 += roznicaY ** 2

    mianownik = (mianownik1 * mianownik2) ** 0.5
    r = licznik / mianownik
    return r

def rownanieRegresji (sredniaX, sredniaY, kolumnaX, kolumnaY, irysy):
    licznik = 0
    mianownik = 0
    for i in range(irysy.shape[0]):
        roznicaX = irysy.iloc[i, kolumnaX] - sredniaX
        roznicaY = irysy.iloc[i, kolumnaY] - sredniaY
        licznik += (roznicaX * roznicaY)
        mianownik += roznicaX ** 2

    a = licznik / mianownik
    b = sredniaY - sredniaX * a
    return a, b

def srednia (i, irysy):
    suma = sum(irysy.iloc[:,i])
    srednia = suma / irysy.shape[0]
    return srednia

# funkcja oblicza procenty udziału gatunków irysów
def procent(liczba, suma):
    dzielenie = (liczba / suma) * 100
    wynik = dzielenie
    return wynik

# funkcja oblcizająca maksimum w każdej kolumnie
def maksimum(dane, column):
    max_value = dane.iloc[0, column]
    for i in range(1, len(dane)):
        if dane.iloc[i, column] > max_value:
            max_value = dane.iloc[i, column]
    return max_value

# funkcja oblicza minimum w każdej kolumnie
def minimum(dane, column):
    min_value = dane.iloc[0, column]
    for i in range(1, len(dane)):
        if dane.iloc[i, column] < min_value:
            min_value = dane.iloc[i, column]
    return min_value

# funkcja oblicza średnią arytmetyczne
def arytmetyczna(dane, column, mianownik):
    liczebnik = dane.iloc[:, column].sum()
    iloraz = liczebnik / mianownik
    srednia = iloraz
    return srednia

# funkcja oblicza odchylenie standardowe dla średniej arytmetycznej
def odchylenie_standardowe(dane, column, mianownik):
    srednia = arytmetyczna(dane, column, mianownik)
    suma_kwadratow = 0
    for i in dane[column]:
        roznica = i - srednia
        suma_kwadratow += roznica ** 2

    liczba = suma_kwadratow / len(dane[column])
    odchylenie = liczba ** 0.5
    return odchylenie

# funkcja oblicza mediane
def mediana(dane, suma, column):
    posortowane = dane.sort_values(by=column, ascending=True).reset_index(drop=True)
    if suma % 2 == 0:
        liczebnik =  posortowane.iloc[(suma // 2) - 1, column] + posortowane.iloc[(suma // 2) , column]
        iloraz = liczebnik / 2
        med = iloraz
        return med
    else:
        liczebnik = posortowane.iloc[suma // 2, column]
        med = liczebnik
        return med

# funkcja oblicza kwartyle górne i dolne
def kwartyle(dane, suma, column):
    posortowane = dane.sort_values(by=column, ascending=True).reset_index(drop=True)
    dolny = posortowane[:len(posortowane) // 2]
    Q1 = mediana(dolny, len(dolny), column)

    if len(posortowane) % 2 == 0:
        gorny = posortowane[len(posortowane) // 2:]
    else:
        gorny = posortowane[len(posortowane) // 2 + 1:]

    Q3 = mediana(gorny, len(gorny), column)
    tekst = f"({Q1}-{Q3})"
    return tekst
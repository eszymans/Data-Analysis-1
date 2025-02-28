import pandas as pd
import seaborn as sns
import funkcje_matematyczne as fn
import matplotlib.pyplot as plt
from pandas.plotting import table
import os

irysy = pd.read_csv("data1.csv", header=None)

#Zadanie 1
# sumy poszczególnych wierszy gatunków kwaitów
setosa_suma = (irysy.iloc[:,4] == 0).sum()
versicolor_suma = (irysy.iloc[:,4] == 1).sum()
virginica_suma = (irysy.iloc[:,4] == 2).sum()
suma = irysy.iloc[:,4].sum()

# tabela 1
dane1 = {"Gatunek": ["Setosa", "Versicolor", "Virginica", "Razem"],
           "Liczbność(%)": [
               f"{setosa_suma} ({round(fn.procent(setosa_suma, suma),2)}%)",
               f"{versicolor_suma} ({round(fn.procent(versicolor_suma, suma),2)}%)",
               f"{virginica_suma} ({round(fn.procent(virginica_suma, suma),2)}%)",
               f"{suma} (100.00%)"
           ]
           }

tabela1 = pd.DataFrame(dane1)
print(tabela1)

plt.show()



#tabela 2
dane2 = {"Cecha": ["Długość działki kielicha (cm)", "Szerokość działki kielicha (cm)",
                   "Długość płatka (cm)", "Szerokość płatka (cm)"],
         "Minimum": [
             f"{fn.minimum(irysy, 0)}",
             f"{fn.minimum(irysy, 1)}",
             f"{fn.minimum(irysy, 2)}",
             f"{fn.minimum(irysy, 3)}",
         ],
          "Śr. arytm. (± odch. stand.)" : [
              f"{round(fn.arytmetyczna(irysy,0, suma),2)} (± {round(fn.odchylenie_standardowe(irysy,0, suma),2)})",
              f"{round(fn.arytmetyczna(irysy,1, suma),2)} (± {round(fn.odchylenie_standardowe(irysy,1, suma),2)})",
              f"{round(fn.arytmetyczna(irysy,2, suma),2)} (± {round(fn.odchylenie_standardowe(irysy,2, suma),2)})",
              f"{round(fn.arytmetyczna(irysy,3, suma),2)} (± {round(fn.odchylenie_standardowe(irysy,3, suma),2)})",
          ],
          "Mediana (Q1 - Q3)" :[
              f"{round(fn.mediana(irysy, suma, 0),2)} {fn.kwartyle(irysy, suma, 0)}",
              f"{round(fn.mediana(irysy, suma, 1),2)} {fn.kwartyle(irysy, suma, 1)}",
              f"{round(fn.mediana(irysy, suma, 2),2)} {fn.kwartyle(irysy, suma, 2)}",
              f"{round(fn.mediana(irysy, suma, 3),2)} {fn.kwartyle(irysy, suma, 3)}",
          ],
           "Maksimum" : [
               f"{fn.maksimum(irysy, 0)}",
               f"{fn.maksimum(irysy, 1)}",
               f"{fn.maksimum(irysy, 2)}",
               f"{fn.maksimum(irysy, 3)}",
           ]
         }

pd.set_option('display.max_columns', None)
tabela2 = pd.DataFrame(dane2)
print(tabela2)

plt.show()

#Zadanie 2
# funkcja rysuje histogramy
def histogram(dane, kolumna, tytulOsiX, tytul, ax, i):
    kolumna_dane = dane.iloc[:, kolumna]
    sns.histplot(kolumna_dane, ax=ax)
    ax.set_xlabel(tytulOsiX, size=27)
    ax.set_ylabel("Liczebność", size=27)
    ax.set_title(tytul, size=27)
    ax.set_title("Histogram " + str(i) + ".", size=27, loc = 'left', y=-0.15)
    ax.tick_params(axis='both',labelsize=27)

# funkcja rysuje wykresy pudełkowe
def wykresPudełkowy(dane, tytulOsiY, kolumna, ax, i):
    kopiaDanych = dane.copy()
    gatunki = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    kopiaDanych["Gatunek"] = kopiaDanych.iloc[:, 4].replace(gatunki)
    sns.boxplot(x="Gatunek", y=dane.iloc[:, kolumna], data=kopiaDanych, ax=ax)
    ax.set_xlabel("Gatunek", size=27)
    ax.set_ylabel(tytulOsiY, size=27)
    ax.tick_params(axis='both',labelsize=27)
    ax.set_title("Wykres " + str(i) + ".", size=27, loc = 'left', y=-0.15)

fig, axes = plt.subplots(4, 2, figsize=(25, 30))


histogram(irysy, 0, "Długość (cm)", "Długość działki kielicha (cm)", axes[0,0], 1)
histogram(irysy, 1, "Szerokość (cm)", "Szerokość działki kielicha (cm)", axes[1,0], 2)
histogram(irysy, 2, "Długość (cm)", "Długość płatka (cm)", axes[2,0], 3)
histogram(irysy, 3, "Szerokość (cm)", "Szerokość płatka (cm)", axes[3,0], 4)

wykresPudełkowy(irysy, "Długość (cm)", 0, axes[0,1], 1)
wykresPudełkowy(irysy, "Szerokość (cm)", 1, axes[1,1], 2)
wykresPudełkowy(irysy, "Długość (cm)", 2, axes[2,1], 3)
wykresPudełkowy(irysy, "Szerokość (cm)", 3, axes[3,1], 4)

plt.subplots_adjust(hspace=0.5)
plt.tight_layout()

#Zapis do pdf
# output_dir = "../doc"
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
#
# plt.savefig(f"{output_dir}/wykresy1.png")

plt.show()

#Zadanie 3
def rysowanieWykresu(kolumnaX, kolumnaY, ax, tytulOsiX, tytulOsiY,i):
    x_values = irysy[irysy.columns[kolumnaX]]
    r = fn.wspolczynnikKorelacji(fn.srednia(kolumnaX, irysy), fn.srednia(kolumnaY, irysy), kolumnaX, kolumnaY, irysy)
    wspolczynniki = fn.rownanieRegresji(fn.srednia(kolumnaX, irysy), fn.srednia(kolumnaY, irysy), kolumnaX, kolumnaY, irysy)
    y_values = wspolczynniki[0] * x_values + wspolczynniki[1]
    sns.scatterplot(data=irysy, x=irysy.columns[kolumnaX], y=irysy.columns[kolumnaY], ax=ax)
    ax.plot(x_values, y_values, color='red', linewidth=2)
    ax.set_xlabel(tytulOsiX, size=20)
    ax.set_ylabel(tytulOsiY, size=20)
    r = round (r,2)
    ax.set_title(f"r = {r}; y = {round(wspolczynniki[0],1)}x + {round(wspolczynniki[1],1)}", size=20)
    ax.set_title("Wykres " + str(i) + ".", size=20, loc='left', y=-0.2)
    ax.tick_params(axis='both', labelsize=20)

#Main
fig, axes = plt.subplots(3, 2, figsize=(15, 20))

rysowanieWykresu(0,1,axes[0][0],"Długość działki kielicha (cm)","Szerokość działki kielicha (cm)", 5)
rysowanieWykresu(0,2,axes[0][1],"Długość działki kielicha (cm)","Długość płatka (cm)", 6)
rysowanieWykresu(0,3,axes[1][0],"Szerokość płatka (cm)","Długość działki kielicha (cm)", 7)
rysowanieWykresu(1,2,axes[1][1],"Szerokość działki kielicha (cm)","Długość płatka (cm)", 8)
rysowanieWykresu(1,3,axes[2][0],"Szerokość płatka (cm)","Szerokość działki kielicha (cm)", 9)
rysowanieWykresu(2,3,axes[2][1],"Szerokość płatka (cm)","Długość płatka (cm)", 10)

plt.tight_layout()
#Zapis do pdf
# output_dir = "../doc"
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
#
# plt.savefig(f"{output_dir}/wykresy2.png")

plt.show()



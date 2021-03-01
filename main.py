# Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne

a, b, c, d, e, f, g, h = "Ala", "drzewo w lesie", 1.2, 12.76, -2, -3000, 12 + 21j, -12835j
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

# Zad2. Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne

a = input("Podaj 1 liczbe: ")
b = input("Podaj znak działania : ")
c = input("Podaj 2 liczbe: ")
if b == "+":
    print("Suma= ")
    print(int(a) + int(c))
elif b == "-":
    print("Różnica= ")
    print(int(a) - int(c))
elif b == "*":
    print("Iloczyn= ")
    print(int(a) * int(c))
elif b == "/":
    print("Iloraz= ")
    print(int(a) / int(c))
else:
    print("nieprawidłowy znak")

# Zad3. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %

a = 5
a += 1
print(a)
b = 10
b -= 2
print(b)
c = 33
c *= 2
print(c)
d = 100
d /= 15
print(d)
e = 100
e **= 1 / 2
print(e)
f = 20
f %= 6
print(f)

# Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia:
from math import *

e **= 10
print(e)

# Zad.5 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami.
# Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe.
# (trzeba użyć metody capitalize)

d = "D"
a = "A"
w = "W"
i = "I"
p = "P"
l = "Ł"
o = "o"
c = "C"
h = "H"
r = "R"
c = "C"
z = "Z"
y = "Y"
k = "K"
print(str.capitalize(d + a + w + i + d))
print(str.capitalize(p + l + o + c + h + a + r + c + z + y + k))

# Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się słowami
# np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”.
# (trzeba użyć metody count)

string = "lala, rata la gapala cikulla la la na na na na na"
print(string.count("la"))

# Zad.7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.

i = "Janusz"
print("druga litera imienia")
print(i[1])
print("ostatnia litera imienia")
print(i[5])

# Zad.8 Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6
# i spróbuj ją podzielić na poszczególne wyrazy.
# (trzeba użyć metody split)

string = "lala, rata la gapala cikulla la la na na na na na"
print(string.split())
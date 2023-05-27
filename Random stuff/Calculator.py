# Beunutzereingabe steuern:
Zahl1=float(input("1. Zahl: "))
Zahl2=float(input("2. Zahl: "))
Rechenzeichen=input("Addieren? (+), Subtrahieren? (-), Multiplizieren? (*), Dividieren? (/): ")


# Ergebnis berechnen:
Ergebnis=0
if Rechenzeichen=="+":
    Ergebnis=Zahl1+Zahl2
if Rechenzeichen=="-":
    Ergebnis=Zahl1-Zahl2
if Rechenzeichen=="*":
    Ergebnis=Zahl1*Zahl2
if Rechenzeichen=="/":
    Ergebnis=Zahl1/Zahl2


# Ergebnis ausgeben:
print("Das Ergebnis ist:", Ergebnis)
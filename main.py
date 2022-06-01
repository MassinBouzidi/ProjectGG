import sys

#Wo kommt die Variable Zeile her?
#ToDo Zeile 20 verstehen

liste = {

}


def initialize():
    
    with open("GG.txt", "r") as datei:      #Öffnet und liest die Datei + Speichern in Variable datei
        for zeile in datei:
            #artikelNummer = ""
            if zeile.startswith("Artikel ") and len(zeile)<=15:     #Um zu prüfen ob ein neuer Artikel beginnt
                artikelNummer = zeile.replace("Artikel ", "")   #"Artikel" wird mit leer_String ersetzt
                liste[artikelNummer] = zeile
            else:                                               #Wenn artikelNummer != Artikelkopf --> Abspeichern von ???
                liste[artikelNummer] = liste[artikelNummer]+zeile   #Was passiert hier?


def showArtikel(artikelNummer):
    pass

if __name__ == '__main__':
    initialize()

    i = input("Eingabe: ")
    while i!="x":
        print(liste[i])     # i nimmt den wert der Artikel Nummer ein
        i = input("Eingabe: ")

    #print(liste)

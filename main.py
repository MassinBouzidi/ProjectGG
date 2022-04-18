import sys

liste = {

}


def initialize():
    
    with open("GG.txt", "r") as datei:
        for zeile in datei:
            #artikelNummer = ""
            if zeile.startswith("Artikel ") and len(zeile)<=15:
                artikelNummer = zeile.replace("Artikel ", "")
                liste[artikelNummer] = zeile
            else:
                liste[artikelNummer] = liste[artikelNummer]+zeile


def showArtikel(artikelNummer):
    pass

if __name__ == '__main__':
    initialize()

    i = input("Eingabe: ")
    while i!="x":
        print(liste[i])
        i = input("Eingabe: ")

    #print(liste)

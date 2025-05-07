from pojisteny import Pojisteny
from evidence import Evidence

class Aplikace:
    def __init__(self):
        self.evidence = Evidence()

    def spustit(self):
        while True:
            self.vypis_menu()
            volba = input("Vyberte si akci: ")
            if volba == "1":
                self.zadej_a_pridej()
            elif volba == "2":
                self.evidence.vypis_vsechny()
            elif volba == "3":
                self.zadej_a_vyhledat()
            elif volba == "4":
                print("Ukončuji aplikaci...")
                break
            else:
                print("Neplatná volba, zkuste to znovu.")
            input("Pokračujte stiskem Enter...")

    def vypis_menu(self):
        print("==============================")
        print("Evidence pojištěných")
        print("==============================")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

    def zadej_a_pridej(self):
        jmeno, prijmeni = self.zadej_jmeno_prijmeni()
        telefon = input("Zadejte telefonní číslo: ")
        vek = input("Zadejte věk: ")
        try:
            pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
            self.evidence.pridat_pojisteneho(pojisteny)
            print("Data byla uložena.")
        except ValueError as e:
            print(f"Chyba: {e}")

    def zadej_a_vyhledat(self):
        jmeno, prijmeni = self.zadej_jmeno_prijmeni()
        self.evidence.vyhledat_pojisteneho(jmeno, prijmeni)

    def zadej_jmeno_prijmeni(self):
        jmeno = input("Zadejte jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení: ")
        return jmeno, prijmeni



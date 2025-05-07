class Evidence:
    def __init__(self):
        self.pojisteni = []

    def pridat_pojisteneho(self, pojisteny):
        self.pojisteni.append(pojisteny)

    def vypis_vsechny(self):
        if not self.pojisteni:
            print("Žádní pojištění nejsou evidováni.")
        else:
            for p in self.pojisteni:
                print(p)

    def vyhledat_pojisteneho(self, jmeno, prijmeni):
        nalezeni = []
        for p in self.pojisteni:
            if p.jmeno.lower().strip() == jmeno.lower().strip() and p.prijmeni.lower().strip() == prijmeni.lower().strip():
                nalezeni.append(p)
        if nalezeni:
            for p in nalezeni:
                print(f"V evidanci existuje:  {p}")
        else:
            print("Pojištěný nenalezen.")
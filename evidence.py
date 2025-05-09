class Evidence:
    def __init__(self):
        self.pojisteni = []

    def pridej_pojisteneho(self, pojisteny):
        self.pojisteni.append(pojisteny)

    def vypis_vsechny(self):
        if not self.pojisteni:
            print("Žádní pojištění nejsou evidováni.")
        else:
            for pojistenec in self.pojisteni:
                print(pojistenec)

    def vyhledej_pojisteneho(self, jmeno, prijmeni):
        nalezeni = []
        for pojistenec in self.pojisteni:
            if pojistenec.jmeno.lower().strip() == jmeno.lower().strip() and pojistenec.prijmeni.lower().strip() == prijmeni.lower().strip():
                nalezeni.append(pojistenec)
        if nalezeni:
            for pojistenec in nalezeni:
                print(f"V evidanci existuje:  {pojistenec}")
        else:
            print("Pojištěný nenalezen.")
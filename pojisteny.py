class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        if not jmeno.strip() or not prijmeni.strip():
            raise ValueError("Jméno a příjmení nesmí být prázdné.")
        
        try:
            vek = int(vek)
        except ValueError:
            raise ValueError("Věk musí být celé číslo.")
        
        if not (0 <= vek <= 150):
                raise ValueError("Věk musí být v rozmezí 0 až 150.")
        

        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno:<15} {self.prijmeni:<15} {self.vek:<5} {self.telefon}"
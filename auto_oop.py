class Auto:
    def __init__(self, verbrauch = 6.2):
        # Definition der Attribute mit Anfangswert
        self.tankfüllung = 0 # Liter
        self.kilometerstand = 0 # km
        self.benzinverbrauch = verbrauch # Liter/ 100 km

    # Definition der Aktionen
    def Tanken(self, menge ):
        self.tankfüllung += menge
        print('Aktion: Tanken', menge)



    def Fahren(self, strecke):
        self.kilometerstand += strecke
        self.tankfüllung =- strecke/100.0*self.benzinverbrauch
        print('Aktion: Fahren', strecke)

    def Anzeigen(self):
        print('-'*30)
        print('Tank', self.tankfüllung)
        print('Kilometerstand', self.kilometerstand)
        print('Benzinverbrauch', self.benzinverbrauch)


auto_objekt = Auto(0)
auto_objekt2 = Auto(5.5)



auto_objekt.Anzeigen()
auto_objekt.Tanken( 60 )
auto_objekt.Anzeigen()
auto_objekt.Fahren( 120 )
auto_objekt.Anzeigen()

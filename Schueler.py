class Schueler:
    def __init__(self, vorname, nachname, klasse):
        self.vorname = vorname
        self.nachname = nachname
        self.klasse = klasse
        self.noten = []
        self.wahlfacher = []

    def hinzufuegenNoten(self, note):
        self.noten.append( note )

    def hinzufuegenWahlfaecher(self, fach ):
        self.wahlfacher.append( fach )

        

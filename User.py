"""
Klasse Kunde

Useranlage:
Oeffnen externe Datei
Lesen aus externer Datei
Eingabe Vorname
Eingabe Nachname
Eingabe Geburtsdatum
Eingabe Kontaktmoeglichkeit: emailAdresse und/oder Handynummer fuer Informationen
Auswahl Bevorzugte Zahlungsmethode
Zur Auswahl: Prepaid, Kreditkarte, Rechnung(Bezahlautomat)
User-ID automatisch vergeben (Zahl?, oder Generierung aus Name und Geburtsdatum?)
Schreiben in externe Datei
Schliessen externe Datei

Daten aendern:
Oeffnen externe Datei
Lesen aus externer Datei
(Menu fuer Aktion) - eigentlich auch aus App heraus
Name aendern
Zahlungsmethode aendern
Kontaktmoeglichkeit aendern
Schreiben in externe Datei
Schliessen externe Datei

Userloeschung:
Oeffnen externe Datei
Lesen aus externer Datei
Kontokontrolle
	Wenn Kontostand „0“ dann weiter, 		sonst Abbruch, und Hinweis auf Ausgleich
Sicherheitsabfrage
	„ja“ dann weiter, 		„nein“ dann Abbruch
Schreiben in externe Datei
Schliessen externe Datei

Zahlungsmoeglichkeiten:
Oeffnen externe Datei
Lesen aus externer Datei
Lasten draufbuchen (Trigger von App)
Kontostand sehen
Lastenausgleich nach Zahlungsmethode (Prepaid, Kredikarte, Rechnung auf Bezahlautomat beim Ausgang)
Schreiben in externe Datei
Schliessen externe Datei




Externe Datei: Kunde.txt
Kunde = {
1:{UserID, Name, Vorname, Geburtsdatum, Kontaktmoeglichkeit, Zahlungsmethode, Kontostand}
2:{UserID, Name, Vorname, Geburtsdatum, Kontaktmoeglichkeit, Zahlungsmethode, Kontostand}
}
"""




class User:

    userID = "placeholder"

    def __init__(self, uID):
        self.userID = uID
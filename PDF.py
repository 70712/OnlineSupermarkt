from fpdf import FPDF
from datetime import datetime, timedelta
from random import randint
from tkinter import *


class PDF:
    datum = datetime.today().strftime('%d.%m.%Y')
    datum2 = (datetime.today() + timedelta(days=30)).strftime('%d.%m.%Y')

    kundennummer = str(randint(1000000000, 9999999999))
    kontonummer = str(randint(100000000000000, 999999999999999))
    iban = 'DE' + str(kontonummer)
    rechnungsnummer = str(randint(1000000000, 9999999999))

    db = None
    pdf = None

    def __init__(self, db, shoppingbag, dir, vorname, nachname, email, telefon, strasse, plz, ort, list_products, shoppingbag_instance):
        self.db = db

        if len(str(vorname.get())) == 0 or str(vorname.get()).isspace() or len(str(nachname.get())) == 0 or str(nachname.get()).isspace() or len(str(email.get())) == 0 or str(email.get()).isspace() or len(str(telefon.get())) == 0 or str(telefon.get()).isspace() or len(str(strasse.get())) == 0 or str(strasse.get()).isspace() or len(str(plz.get())) == 0 or str(plz.get()).isspace() or len(str(ort.get())) == 0 or str(ort.get()).isspace():
            error = Tk()
            error.title("Fehler")
            error.resizable(0, 0)

            frame = Frame(error, width=240, height=20, bg='white')

            var_error = StringVar(master=error, value='Kontoinformationen unvollständig!')
            error_output = Entry(frame, width=30, font=("Calibri", 12), fg='red', textvariable=var_error, borderwidth=0)
            error_output.place(x=0, y=0)

            frame.pack()
            error.mainloop()

        # PDF initialisieren
        self.pdf = FPDF(orientation='P', unit='mm', format='A4')
        self.pdf.add_page()
        self.pdf.image("rechnung_background.gif", x=0, y=0, w=210)

        # Rechnung
        self.pdf.set_xy(100, 66)
        self.pdf.set_font("Times", style='B', size=48)
        self.pdf.set_text_color(255, 173, 22)
        self.pdf.cell(93, 13, txt="RECHNUNG", ln=1, align="R")

        # Name
        name = str(vorname.get()) + " " + str(nachname.get())
        self.pdf.set_xy(6, 30)
        self.pdf.set_font("Times", style='', size=12)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.cell(100, 4, txt=name, ln=1, align="L")

        # Straße
        self.pdf.set_xy(6, 37)
        self.pdf.cell(100, 4, txt=str(strasse.get()), ln=1, align="L")

        # PLZ und Ort
        plz_ort = str(plz.get()) + " " + str(ort.get())
        self.pdf.set_xy(6, 44)
        self.pdf.cell(100, 4, txt=plz_ort, ln=1, align="L")

        # E-Mail-Adresse
        self.pdf.set_xy(6, 63)
        self.pdf.set_font_size(9)
        self.pdf.set_text_color(255, 173, 22)
        self.pdf.cell(100, 4, txt="E-Mail", ln=1, align="L")

        self.pdf.set_xy(18, 63)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.cell(100, 4, txt=str(email.get()), ln=1, align="L")

        # Telefonnummer
        self.pdf.set_xy(6, 69)
        self.pdf.set_text_color(255, 173, 22)
        self.pdf.cell(100, 4, txt="Tel", ln=1, align="L")

        self.pdf.set_xy(14, 69)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.cell(100, 4, txt=str(telefon.get()), ln=1, align="L")

        # Datum
        self.pdf.set_xy(6, 75)
        self.pdf.set_text_color(255, 173, 22)
        self.pdf.cell(100, 4, txt="Datum", ln=1, align="L")

        self.pdf.set_xy(18, 75)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.cell(100, 4, txt=str(self.datum), ln=1, align="L")

        # Kundennummer
        self.pdf.set_xy(6, 81)
        self.pdf.set_text_color(255, 173, 22)
        self.pdf.cell(100, 4, txt="Kundennummer", ln=1, align="L")

        self.pdf.set_xy(30, 81)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.cell(100, 4, txt=self.kundennummer, ln=1, align="L")

        # Rechnungsnummer
        self.pdf.set_xy(6, 87)
        self.pdf.set_text_color(255, 173, 22)
        self.pdf.cell(100, 4, txt="Rechnungsnummer", ln=1, align="L")

        self.pdf.set_xy(35, 87)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.cell(100, 4, txt=self.rechnungsnummer, ln=1, align="L")

        # -------------------------------------------------------

        # Einleitung
        self.pdf.set_xy(13, 120)
        self.pdf.set_font("Times", style='', size=12)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.cell(100, 4, txt="Hiermit stellen wir Ihnen folgende Positionen in Rechnung.", ln=1, align="L")

        # -------------------------------------------------------

        # Tabelle Kopfzeile
        self.pdf.set_xy(20, 140)
        self.pdf.set_font("Times", style='b', size=10)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.cell(100, 4, txt="Artikelnummer", ln=1, align="L")

        self.pdf.set_xy(62, 140)
        self.pdf.cell(100, 4, txt="Name", ln=1, align="L")

        self.pdf.set_xy(110, 140)
        self.pdf.cell(100, 4, txt="Einzelpreis", ln=1, align="L")

        self.pdf.set_xy(145, 140)
        self.pdf.cell(100, 4, txt="Menge", ln=1, align="L")

        self.pdf.set_xy(175, 140)
        self.pdf.cell(100, 4, txt="Betrag", ln=1, align="L")

        # -------------------------------------------------------

        # Produkte
        self.pdf.set_font("Times", style='', size=10)
        self.pdf.set_text_color(0, 0, 0)

        query = {'in_shoppingbag': {'$gt': 0}}
        doc = db.col.find(query)
        y = 149
        for entry in doc:
            self.addEntry(y, str(entry['artikelnummer']), str(entry['name']), str(float(entry['preis']) - float(entry['rabatt']) + float(entry['pfand'])), str(entry['in_shoppingbag']), str(float(float(entry['preis']) - float(entry['rabatt']) + float(entry['pfand'])) * int(entry['in_shoppingbag'])))
            self.pdf.image("separator.gif", x=0, y=y+6, w=210)
            y += 9
            if y == 257 or y == 365 or y == 473:
                self.pdf.add_page()
                y = 32

        # -------------------------------------------------------

        # Mehrwertsteuer und Rechnungsbetrag errechnen
        summe = 0.0
        query = {'in_shoppingbag': {'$gt': 0}}
        doc = db.col.find(query)
        for entry in doc:
            summe += float((float(entry['preis']) - float(entry['rabatt']) + float(entry['pfand'])) * int(
                entry['in_shoppingbag']))
        mwst = 0.19 * summe
        rechnungsbetrag = StringVar(value=str("%.2f" % float(summe)))
        mwst = StringVar(value=str("%.2f" % float(mwst)))

        # Mehrwertsteuer
        self.pdf.set_xy(145, y)
        self.pdf.cell(100, 4, txt="davon MwSt.", ln=1, align="L")

        self.pdf.set_xy(175, y)
        self.pdf.cell(100, 4, txt=str(mwst.get()) + " " + chr(128), ln=1, align="L")

        y += 9

        # Rechnungsbetrag
        self.pdf.image("rechnungsbetrag_background.gif", x=140, y=y-2, w=70)
        self.pdf.set_font("Times", style='b', size=10)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.set_xy(145, y)
        self.pdf.cell(100, 4, txt="Rechnungsbetrag", ln=1, align="L")

        self.pdf.set_xy(175, y)
        self.pdf.cell(100, 4, txt=str(rechnungsbetrag.get()) + " " + chr(128), ln=1, align="L")

        # -------------------------------------------------------

        # Schluss
        self.pdf.set_font("Times", style='', size=12)
        self.pdf.set_text_color(0, 0, 0)
        self.pdf.set_xy(13, y + 30)
        self.pdf.cell(100, 4, txt="Bitte überweisen Sie den Rechnungsbetrag bis zum " + str(self.datum2) + " auf unser Konto mit der ", ln=1, align="L")
        self.pdf.set_xy(13, y + 38)
        self.pdf.cell(100, 4, txt="IBAN '" + str(self.iban) + "' und dem Verwendungszweck '" + str(self.rechnungsnummer) + "'.", ln=1, align="L")

        # -------------------------------------------------------

        dir = str(dir).replace("/", "\\")

        if len(dir) > 0:
            # auf_lager reduzieren
            query = {'in_shoppingbag': {'$gt': 0}}
            doc = db.col.find(query)
            for entry in doc:
                entry_query = {'artikelnummer': int(entry['artikelnummer'])}
                new = int(entry['auf_lager']) - int(entry['in_shoppingbag'])
                newvalue = {'$set': {'auf_lager': int(new)}}
                db.col.update_one(entry_query, newvalue)
            # Anzeigen und Einträge aktualisieren
            for prod in list_products:
                query = {'artikelnummer': prod.entry['artikelnummer']}
                doc = db.col.find(query)
                for entry in doc:
                    prod.setentry(entry)
                if prod.info:
                    prod.var_auflager.set(int(prod.entry['auf_lager']))
                prod.var_inshoppingbag.set(0)
                newvalue = {'$set': {'in_shoppingbag': 0}}
                db.col.update_one(query, newvalue)
                img_shoppingbag_empty = PhotoImage(file='shoppingbag_empty_small.gif')
                prod.product_shoppingbag.config(image=img_shoppingbag_empty)
                prod.product_shoppingbag.photo = img_shoppingbag_empty
                shoppingbag_instance.update()

            # Fenster schließen und Rechnungs-PDF erstellen
            shoppingbag.destroy()
            self.pdf.output(str(dir) + "\\Rechnung.pdf")

        # -------------------------------------------------------
            # Erfolg Fenster
            success = Tk()
            success.title("Erfolg")
            success.resizable(0, 0)

            frame = Frame(success, width=240, height=20, bg='white')

            var_success = StringVar(master=success, value='Rechnung erfolgreich erstellt!')
            success_output = Entry(frame, width=30, font=("Calibri", 12), fg='green', textvariable=var_success, borderwidth=0)
            success_output.place(x=0, y=0)

            frame.pack()
            success.mainloop()


    # Eintrag zur Rechnungsübersicht mit Positionen und Inhalten hinzufügen
    def addEntry(self, y, artikelnummer, name, einzelpreis, menge, betrag):
        self.pdf.set_xy(20, y)
        self.pdf.cell(100, 4, txt=artikelnummer, ln=1, align="L")

        #   Name
        self.pdf.set_xy(62, y)
        self.pdf.cell(100, 4, txt=name, ln=1, align="L")

        #   Einzelpreis
        self.pdf.set_xy(110, y)
        self.pdf.cell(100, 4, txt=str("%.2f" % float(einzelpreis)) + " " + chr(128), ln=1, align="L")

        #   Menge
        self.pdf.set_xy(145, y)
        self.pdf.cell(100, 4, txt=menge, ln=1, align="L")

        #   Menge
        self.pdf.set_xy(175, y)
        self.pdf.cell(100, 4, txt=str("%.2f" % float(betrag)) + " " + chr(128), ln=1, align="L")

from tkinter import *


class Product:
    ##############################
    # Grundlegende Variablen
    id = None
    product_frame = None
    artikelnummer = None

    overview_canvas = None
    entry = None
    info = False
    var_inshoppingbag = None
    var_auflager = None
    product_shoppingbag = None

    color_grey = '#CCCCCC'
    color_lightgrey = '#EAEAEA'

    def __init__(self, window, x, y, overview_canvas, db, artikelnummer, shoppingbag_instance):
        # Finde Produkt in Datenbank
        self.artikelnummer = artikelnummer
        self.overview_canvas = overview_canvas
        col = db.col
        query = {'artikelnummer': artikelnummer}
        doc = col.find(query)
        for e in doc:
            self.entry = e

        # Produkt-Images
        img_background = PhotoImage(file='product_background.gif')
        img_img = PhotoImage(file=str(self.entry['img']))
        img_shoppingbag_empty = PhotoImage(file='shoppingbag_empty_small.gif')
        img_shoppingbag_full = PhotoImage(file='shoppingbag_full_small.gif')
        img_down = PhotoImage(file='down.gif')
        img_klappe = PhotoImage(file="klappe.gif")
        img_pfand = PhotoImage(file="pfand.gif")
        img_left = PhotoImage(file="left.gif")
        img_right = PhotoImage(file="right.gif")
        img_bio = PhotoImage(file="bio.gif")
        img_line = PhotoImage(file="line.gif")

        # Frame
        self.product_frame = Frame(overview_canvas, width=240, height=420, bg="white")
        self.product_frame.grid(row=0, column=0)
        product_canvas = Canvas(self.product_frame, width=236, height=416, bg="white")
        product_canvas.grid(row=0, column=0)

        # Hintergrund
        product_background = Label(product_canvas, image=img_background, bg='white', borderwidth=0)
        product_background.photo = img_background
        product_background.place(x=0, y=0)

        # Bild
        product_img = Label(product_canvas, image=img_img, bg=self.color_lightgrey, borderwidth=0)
        product_img.photo = img_img
        product_img.place(x=1, y=50)

        # Warenkorb
        self.product_shoppingbag = Label(product_canvas, image=img_shoppingbag_empty, bg=self.color_lightgrey, borderwidth=0)
        self.product_shoppingbag.photo = img_shoppingbag_empty
        if int(self.entry['in_shoppingbag']) > 0:
            self.product_shoppingbag.config(image=img_shoppingbag_full)
            self.product_shoppingbag.photo = img_shoppingbag_full
        self.product_shoppingbag.place(x=12, y=268)

        # Klappe
        product_klappe = Label(product_canvas, image=img_klappe, borderwidth=0)
        product_klappe.photo = img_klappe

        # Kategorie Text
        var_kategorie = StringVar(master=window, value=str(self.entry['kategorie']))
        text_kategorie = Label(product_canvas, width=19, height=1, font=("Calibri", 10, 'bold'), bg=self.color_lightgrey, highlightbackground=self.color_lightgrey, textvariable=var_kategorie, borderwidth=0, anchor='w')

        # Artikelnummer Text
        var_artikelnummer = StringVar(master=window, value=artikelnummer)
        text_artikelnummer = Label(product_canvas, width=10, height=1, font=("Calibri", 9), bg=self.color_lightgrey, highlightbackground=self.color_lightgrey, textvariable=var_artikelnummer, borderwidth=0, anchor='w')

        # Hersteller Text
        var_hersteller = StringVar(master=window, value=str(self.entry['hersteller']))
        text_hersteller = Label(product_canvas, width=20, height=1, font=("Calibri", 8), bg=self.color_lightgrey, highlightbackground=self.color_lightgrey, textvariable=var_hersteller, borderwidth=0, anchor='w')

        # Auf-Lager Text
        self.var_auflager = StringVar(master=window, value=int(self.entry['auf_lager']))
        text_auflager = Label(product_canvas, width=10, height=1, font=("Calibri", 9), bg=self.color_lightgrey, highlightbackground=self.color_lightgrey, textvariable=self.var_auflager, borderwidth=0, anchor='w')

        # Pfand Text
        zzglpfand = Label(product_canvas, image=img_pfand, bg=self.color_lightgrey, borderwidth=0)
        zzglpfand.photo = img_pfand
        var_pfand = StringVar(master=window, value=str("%.2f" % self.entry['pfand']) + '€')
        text_pfand = Label(product_canvas, width=10, height=1, font=("Calibri", 9), bg=self.color_lightgrey, highlightbackground=self.color_lightgrey, textvariable=var_pfand, borderwidth=0, anchor='w')

        # Anzahl anpassen
        self.var_inshoppingbag = StringVar(master=window, value=int(self.entry['in_shoppingbag']))
        inshoppingbag = Label(product_canvas, width=3, height=1, font=("Calibri", 11), bg=self.color_lightgrey, highlightbackground=self.color_lightgrey, textvariable=self.var_inshoppingbag, borderwidth=0)

        def updateShoppingbag(new):
            query = {'artikelnummer': self.artikelnummer}
            newvalue = {'$set': {'in_shoppingbag': new}}

            db.col.update_one(query, newvalue)
            query = {'artikelnummer': artikelnummer}
            doc = col.find(query)
            for e in doc:
                self.entry = e

        def leftbutton_clicked():
            if int(self.var_inshoppingbag.get()) > 0:
                self.var_inshoppingbag.set(int(self.var_inshoppingbag.get()) - 1)
            if int(self.var_inshoppingbag.get()) == 0:
                self.product_shoppingbag.config(image=img_shoppingbag_empty)
                self.product_shoppingbag.photo = img_shoppingbag_empty
            updateShoppingbag(int(self.var_inshoppingbag.get()))
            shoppingbag_instance.update()

        leftbutton = Button(product_canvas, image=img_left, command=leftbutton_clicked, bg=self.color_lightgrey, highlightbackground=self.color_grey, borderwidth=0)
        leftbutton.photo = img_left

        def rightbutton_clicked():
            if int(self.entry['auf_lager']) > int(self.entry['in_shoppingbag']):
                self.var_inshoppingbag.set(int(self.var_inshoppingbag.get()) + 1)
                self.product_shoppingbag.config(image=img_shoppingbag_full)
                self.product_shoppingbag.photo = img_shoppingbag_full
                updateShoppingbag(int(self.var_inshoppingbag.get()))
                shoppingbag_instance.update()

        rightbutton = Button(product_canvas, image=img_right, command=rightbutton_clicked, bg=self.color_lightgrey, highlightbackground=self.color_grey, borderwidth=0)
        rightbutton.photo = img_right

        # Bio Logo
        bio = Label(product_canvas, image=img_bio, bg=self.color_lightgrey, borderwidth=0)
        bio.photo = img_bio

        # Info Ausklappen Knopf
        def downbutton_clicked():
            self.info = not self.info
            if self.info:
                product_klappe.place(x=90, y=1)
                text_kategorie.place(x=100, y=10)
                text_artikelnummer.place(x=106, y=72)
                text_hersteller.place(x=106, y=116)
                text_auflager.place(x=154, y=140)
                if float(self.entry['pfand']) > 0:
                    zzglpfand.place(x=103, y=168)
                    text_pfand.place(x=162, y=164)
                inshoppingbag.place(x=153, y=269)
                leftbutton.place(x=135, y=269)
                rightbutton.place(x=183, y=269)
                if str(self.entry['bio']) == 'True':
                    bio.place(x=134, y=203)
            else:
                product_klappe.place_forget()
                text_kategorie.place_forget()
                text_artikelnummer.place_forget()
                text_hersteller.place_forget()
                text_auflager.place_forget()
                zzglpfand.place_forget()
                text_pfand.place_forget()
                inshoppingbag.place_forget()
                leftbutton.place_forget()
                rightbutton.place_forget()
                bio.place_forget()

        infobutton = Button(product_canvas, image=img_down, command=downbutton_clicked, bg=self.color_lightgrey, borderwidth=0)
        infobutton.photo = img_down
        infobutton.place(x=10, y=10)

        # Name
        var_name = StringVar(master=window, value=str(self.entry['name']))
        product_name = Label(product_canvas, width=23, height=1, font=("Calibri", 14), bg='white', highlightbackground='white', textvariable=var_name, borderwidth=0, anchor='center')
        product_name.place(x=4, y=340)

        # Preis
        var_preis = StringVar(master=window, value=str("%.2f" % float(self.entry['preis'])) + '€')
        product_preis = Label(product_canvas, width=29, height=1, font=("Calibri", 12), bg='white', highlightbackground='white', textvariable=var_preis, borderwidth=0, anchor='center')
        product_preis.place(x=4, y=376)

        # Reduzierter Preis
        if float(self.entry['rabatt']) > 0:
            line = Label(product_canvas, image=img_line, bg=self.color_lightgrey, borderwidth=0)
            line.photo = img_line
            line.place(x=96, y=385)

            var_reduzierterpreis = StringVar(master=window, value=str("%.2f" % float(float(self.entry['preis']) - float(self.entry['rabatt']))) + '€')
            produkt_reduzierterpreis = Label(product_canvas, width=6, height=1, font=("Calibri", 12), fg='red', bg='white', highlightbackground='white', textvariable=var_reduzierterpreis, borderwidth=0, anchor='center')
            produkt_reduzierterpreis.place(x=152, y=376)

        # Packen
        self.id = overview_canvas.create_window((x, y), window=self.product_frame, anchor='nw')
        self.product_frame.update_idletasks()

    def setentry(self, entry):
        self.entry = entry

    def getid(self):
        return self.id

    def setid(self, id):
        self.id = id

    def getproductframe(self):
        return self.product_frame


class ShoppingbagProduct:
    ##############################
    # Grundlegende Variablen
    id = None
    product_frame = None
    artikelnummer = None

    shoppingbag_overview_canvas = None
    entry = None

    color_grey = '#CCCCCC'
    color_lightgrey = '#EAEAEA'

    def __init__(self, shoppingbag, x, y, shoppingbag_overview_canvas, db, artikelnummer, var_summe_all, var_mwst):
        # Finde Produkt in Datenbank
        self.artikelnummer = artikelnummer
        self.shoppingbag_overview_canvas = shoppingbag_overview_canvas
        col = db.col
        query = {'artikelnummer': artikelnummer}
        doc = col.find(query)
        for e in doc:
            self.entry = e

        # Warenkorb-Images
        img_background = PhotoImage(file='shoppingbag_product_background.gif', master=shoppingbag)
        img_img = PhotoImage(file=str(self.entry['img']), master=shoppingbag)
        img_left = PhotoImage(file="left.gif", master=shoppingbag)
        img_right = PhotoImage(file="right.gif", master=shoppingbag)

        # Frame
        self.product_frame = Frame(shoppingbag_overview_canvas, width=596, height=196, bg="white")
        self.product_frame.grid(row=0, column=0)
        product_canvas = Canvas(self.product_frame, width=596, height=196, bg="white")
        product_canvas.grid(row=0, column=0)

        # Hintergrund
        product_background = Label(product_canvas, image=img_background, bg='white', borderwidth=0)
        product_background.photo = img_background
        product_background.place(x=0, y=0)

        # Bild
        product_bild = Label(product_canvas, image=img_img, bg='white', borderwidth=0)
        product_bild.photo = img_img
        product_bild.place(x=1, y=1)

        # Name
        var_name = StringVar(master=shoppingbag, value=str(self.entry['name']))
        product_name = Label(product_canvas, width=23, height=1, font=("Calibri", 14), bg='white', highlightbackground='white', textvariable=var_name, borderwidth=0, anchor='center')
        product_name.place(x=300, y=20)

        # Preis
        var_preis = StringVar(master=shoppingbag, value=str("%.2f" % float(float(self.entry['preis']) - float(self.entry['rabatt']) + float(self.entry['pfand']))) + " €")
        product_preis = Label(product_canvas, width=10, height=1, font=("Calibri", 12), bg='white', highlightbackground='white', textvariable=var_preis, borderwidth=0, anchor='center')
        product_preis.place(x=260, y=142)

        # Summe
        var_summe = StringVar(master=shoppingbag, value=str("%.2f" % float((float(self.entry['preis']) - float(self.entry['rabatt']) + float(self.entry['pfand'])) * int(self.entry['in_shoppingbag']))) + " €")
        product_summe = Label(product_canvas, width=10, height=1, font=("Calibri", 12), bg='white', highlightbackground='white', textvariable=var_summe, borderwidth=0, anchor='center')
        product_summe.place(x=500, y=142)

        # Anzahl
        def updateSumme():
            summe = 0.0
            query = {'in_shoppingbag': {'$gt': 0}}
            doc = db.col.find(query)
            for entry in doc:
                summe += float((float(entry['preis']) - float(entry['rabatt']) + float(entry['pfand'])) * int(
                    entry['in_shoppingbag']))
            mwst = 0.19 * summe
            var_summe_all.set(str("%.2f" % float(summe)) + ' €')
            var_mwst.set(str("%.2f" % float(mwst)) + ' €')

        def updateShoppingbag(new):
            query = {'artikelnummer': int(self.artikelnummer)}
            newvalue = {'$set': {'in_shoppingbag': new}}
            db.col.update_one(query, newvalue)
            query = {'artikelnummer': artikelnummer}
            doc = col.find(query)
            for e in doc:
                self.entry = e

        var_inshoppingbag = StringVar(master=shoppingbag, value=int(self.entry['in_shoppingbag']))
        anzahl_label = Label(product_canvas, width=4, height=1, font=("Calibri", 11), bg='white', highlightbackground='white', textvariable=var_inshoppingbag, borderwidth=0)
        anzahl_label.place(x=403, y=143)

        def leftbutton_clicked():
            if int(var_inshoppingbag.get()) > 0:
                var_inshoppingbag.set(int(var_inshoppingbag.get()) - 1)
            updateShoppingbag(int(var_inshoppingbag.get()))
            var_summe.set(str("%.2f" % float((float(self.entry['preis']) - float(self.entry['rabatt']) + float(self.entry['pfand'])) * int(self.entry['in_shoppingbag']))) + " €")
            updateSumme()

        leftbutton = Button(product_canvas, image=img_left, command=leftbutton_clicked, bg='white', borderwidth=0)
        leftbutton.photo = img_left
        leftbutton.place(x=387, y=142)

        def rightbutton_clicked():
            var_inshoppingbag.set(int(var_inshoppingbag.get()) + 1)
            updateShoppingbag(int(var_inshoppingbag.get()))
            var_summe.set(str("%.2f" % float((float(self.entry['preis']) - float(self.entry['rabatt']) + float(self.entry['pfand'])) * int(self.entry['in_shoppingbag']))) + " €")
            updateSumme()

        rightbutton = Button(product_canvas, image=img_right, command=rightbutton_clicked, bg='white', borderwidth=0)
        rightbutton.photo = img_right
        rightbutton.place(x=437, y=142)


        # Packen
        self.id = shoppingbag_overview_canvas.create_window((x, y), window=self.product_frame, anchor='nw')
        self.product_frame.update_idletasks()

    def getid(self):
        return self.id

    def setid(self, id):
        self.id = id

    def getproductframe(self):
        return self.product_frame


class ListVar:
    list = []

    def __init__(self, list):
        self.list = list

    def set(self, list):
        self.list = list

    def get(self):
        return self.list


class Shoppingbag:
    amount = 0
    db = None
    shoppingbagbutton = None
    var_shoppingbag = None
    img_shoppingbag_empty = None
    img_shoppingbag_full = None

    def __init__(self, db, shoppingbagbutton, var_shoppingbag, img_shoppingbag_empty, img_shoppingbag_full):
        self.db = db
        self.shoppingbagbutton = shoppingbagbutton
        self.var_shoppingbag = var_shoppingbag
        self.img_shoppingbag_empty = img_shoppingbag_empty
        self.img_shoppingbag_full = img_shoppingbag_full

    def update(self):
        self.amount = 0
        col = self.db.col
        for artikelnummer in self.db.artikelnummern_all:
            query = {'artikelnummer': artikelnummer}
            doc = col.find(query)
            entry = None
            for e in doc:
                entry = e
            self.amount += int(entry['in_shoppingbag'])
        self.var_shoppingbag.set(str(self.amount))
        if self.amount == 0:
            self.shoppingbagbutton.config(image=self.img_shoppingbag_empty)
            self.shoppingbagbutton.photo = self.img_shoppingbag_empty
        else:
            self.shoppingbagbutton.config(image=self.img_shoppingbag_full)
            self.shoppingbagbutton.photo = self.img_shoppingbag_full

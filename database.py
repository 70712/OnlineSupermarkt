import pymongo

class Database():
    db = None
    col = None
    artikelnummern_all = []

    def __init__(self, db):
        self.db = db
        self.col = db["products"]

    def insert(self, artikelnummer, name, hersteller, preis, pfand, kategorie, verfuegbar, verkauft, rabatt, bio, img, imgsmall):
        self.col.insert_one({
            'artikelnummer': artikelnummer,
            'name': name,
            'hersteller': hersteller,
            'preis': preis,
            'pfand': pfand,
            'kategorie': kategorie,
            'auf_lager': verfuegbar,
            'verkauft': verkauft,
            'rabatt': rabatt,
            'bio': bio,
            'in_shoppingbag': 0,
            'img': img,
            'imgsmall': imgsmall
        })
        self.artikelnummern_all.append(artikelnummer)

    def delete_many(self):
        self.col.delete_many({})
        self.artikelnummern_all = []

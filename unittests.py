from GUI import *


class TestCaseSort:
    all = [68073502, 38300244, 19880725, 72382285, 48825245, 53544068, 15501683, 53608769, 92865433, 46859398, 91515248, 70463214, 33677993, 10772237, 71768367, 38254554, 48864636, 13240739, 11537301, 83786068, 17461900, 54510048, 78731831, 36045914, 71355504, 13384419, 43997885, 22922661, 13577022, 90817217, 43034251, 51213745, 39056772, 51120140, 43984753, 49599605, 58759164, 71388255, 33438174, 94207829, 90662885, 64652408, 67132299, 10365520, 53746620, 92675461, 22722890, 33158387, 36908628, 35549586, 44491844, 54647949, 74357588, 39370352,  96652679, 85804439, 80454788, 46945362, 62617958, 44505619, 19959459, 41160965, 67219414,  98338053, 46411951, 79489036, 56646084, 44811259, 32430413, 39904854, 59072412, 93827923,  98334007, 69214220, 56818109, 42795214]
    some = [19880725, 15501683, 91515248, 71768367, 11537301, 17461900, 43997885, 22922661, 51213745, 39056772, 71388255, 33438174, 67132299, 10365520, 54647949, 74357588, 80454788, 46945362, 46411951, 32430413, 98334007]
    one = [10772237]
    none = []

    def test_all_preis_aufsteigend(self):
        result = [41160965, 22922661, 74357588, 67219414, 98338053, 13384419, 43997885, 44505619, 70463214, 32430413, 71768367, 38254554, 48864636, 13240739, 11537301, 83786068, 17461900, 22722890, 36908628, 35549586, 46945362, 92865433, 10772237, 71355504, 51213745, 91515248, 44491844, 39370352, 38300244, 48825245, 15501683, 33677993, 39056772, 90662885, 53746620, 85804439, 62617958, 79489036, 98334007, 78731831, 68073502, 72382285, 53544068, 36045914, 19959459, 39904854, 44811259, 51120140, 56646084, 58759164, 53608769, 46859398, 54510048, 71388255, 94207829, 10365520, 96652679, 80454788, 46411951, 56818109, 64652408, 59072412, 69214220, 19880725, 43984753, 33438174, 67132299, 92675461, 93827923, 49599605, 33158387, 42795214, 54647949, 43034251, 13577022, 90817217]
        assert set(sort(self.all, 4)) == set(result), "Preis-Aufsteigend-Reihenfolge falsch"

    def test_all_beliebtheit(self):
        result = [98338053, 46411951, 41160965, 33677993, 35549586, 54647949, 92675461, 51213745, 53544068, 62617958, 93827923, 71355504, 69214220, 39904854, 71388255, 44811259, 56818109, 17461900, 70463214, 53746620, 46945362, 78731831, 44505619, 38254554, 43997885, 33438174, 22722890, 80454788, 92865433, 51120140, 90817217, 90662885, 59072412, 43034251, 19959459, 74357588, 43984753, 94207829, 13384419, 54510048, 13240739, 53608769, 11537301, 46859398, 71768367, 10365520, 44491844, 48864636, 83786068, 10772237, 22922661, 67132299, 96652679, 98334007, 36908628, 39370352, 13577022, 36045914, 49599605, 79489036, 58759164, 38300244, 72382285, 85804439, 19880725, 56646084, 15501683, 39056772, 33158387, 64652408, 91515248, 48825245, 68073502, 32430413, 42795214, 67219414]
        assert set(sort(self.all, 2)) == set(result), "Beliebtheit-Reihenfolge falsch"

    def test_some_preis_absteigend(self):
        result = [54647949, 67132299, 33438174, 19880725, 46411951, 80454788, 10365520, 71388255, 98334007, 39056772, 15501683, 91515248, 51213745, 46945362, 17461900, 11537301, 71768367, 32430413, 43997885, 74357588, 22922661]
        assert set(sort(self.some, 3)) == set(result), "Preis-Absteigend-Reihenfolge falsch"

    def test_one_alphabetisch_Z_A(self):
        result = [10772237]
        assert set(sort(self.one, 1)) == set(result), "Alphabetisch (Z-A)-Reihenfolge falsch"

    def test_none_alphabetisch_A_Z(self):
        result = []
        assert set(sort(self.none, 0)) == set(result), "Alphabetisch (A-Z)-Reihenfolge falsch"


tc_sort = TestCaseSort()
tc_sort.test_all_preis_aufsteigend()
tc_sort.test_all_beliebtheit()
tc_sort.test_some_preis_absteigend()
tc_sort.test_one_alphabetisch_Z_A()
tc_sort.test_none_alphabetisch_A_Z()


class TestCaseInsert:
    def test_standard(self):
        db.delete_many()
        db.insert(16517816, "Testprodukt", "Testhersteller", 1.99, 0.25, "Testkategorie", 275, 21, 0.15, True, None, None)

        assert db.artikelnummern_all == [16517816], "Artikelnummernliste-Insert fehlerhaft"

        assert db.col.find()[0]['artikelnummer'] == 16517816, "Artikelnummer-Insert fehlerhaft"
        assert db.col.find()[0]['name'] == "Testprodukt", "Name-Insert fehlerhaft"
        assert db.col.find()[0]['hersteller'] == "Testhersteller", "Hersteller-Insert fehlerhaft"
        assert db.col.find()[0]['preis'] == 1.99, "Preis-Insert fehlerhaft"
        assert db.col.find()[0]['pfand'] == 0.25, "Pfand-Insert fehlerhaft"
        assert db.col.find()[0]['kategorie'] == "Testkategorie", "Kategorie-Insert fehlerhaft"
        assert db.col.find()[0]['auf_lager'] == 275, "Verfügbar-Insert fehlerhaft"
        assert db.col.find()[0]['verkauft'] == 21, "Verkauft-Insert fehlerhaft"
        assert db.col.find()[0]['rabatt'] == 0.15, "Rabatt-Insert fehlerhaft"
        assert db.col.find()[0]['bio'] == True, "Bio-Insert fehlerhaft"
        assert db.col.find()[0]['img'] == None, "img-Insert fehlerhaft"
        assert db.col.find()[0]['imgsmall'] == None, "imgsmall-Insert fehlerhaft"

    def test_standard_twice(self):
        db.delete_many()
        db.insert(16517816, "Testprodukt", "Testhersteller", 1.99, 0.25, "Testkategorie", 275, 21, 0.15, True, None, None)
        db.insert(16517816, "Testprodukt", "Testhersteller", 1.99, 0.25, "Testkategorie", 275, 21, 0.15, True, None, None)

        assert db.artikelnummern_all == [16517816, 16517816], "Artikelnummernliste-Insert fehlerhaft"

        assert db.col.find()[0]['artikelnummer'] == 16517816, "Artikelnummer-Insert fehlerhaft"
        assert db.col.find()[0]['name'] == "Testprodukt", "Name-Insert fehlerhaft"
        assert db.col.find()[0]['hersteller'] == "Testhersteller", "Hersteller-Insert fehlerhaft"
        assert db.col.find()[0]['preis'] == 1.99, "Preis-Insert fehlerhaft"
        assert db.col.find()[0]['pfand'] == 0.25, "Pfand-Insert fehlerhaft"
        assert db.col.find()[0]['kategorie'] == "Testkategorie", "Kategorie-Insert fehlerhaft"
        assert db.col.find()[0]['auf_lager'] == 275, "Verfügbar-Insert fehlerhaft"
        assert db.col.find()[0]['verkauft'] == 21, "Verkauft-Insert fehlerhaft"
        assert db.col.find()[0]['rabatt'] == 0.15, "Rabatt-Insert fehlerhaft"
        assert db.col.find()[0]['bio'] == True, "Bio-Insert fehlerhaft"
        assert db.col.find()[0]['img'] == None, "img-Insert fehlerhaft"
        assert db.col.find()[0]['imgsmall'] == None, "imgsmall-Insert fehlerhaft"

        assert db.col.find()[1]['artikelnummer'] == 16517816, "Artikelnummer-Insert fehlerhaft"
        assert db.col.find()[1]['name'] == "Testprodukt", "Name-Insert fehlerhaft"
        assert db.col.find()[1]['hersteller'] == "Testhersteller", "Hersteller-Insert fehlerhaft"
        assert db.col.find()[1]['preis'] == 1.99, "Preis-Insert fehlerhaft"
        assert db.col.find()[1]['pfand'] == 0.25, "Pfand-Insert fehlerhaft"
        assert db.col.find()[1]['kategorie'] == "Testkategorie", "Kategorie-Insert fehlerhaft"
        assert db.col.find()[1]['auf_lager'] == 275, "Verfügbar-Insert fehlerhaft"
        assert db.col.find()[1]['verkauft'] == 21, "Verkauft-Insert fehlerhaft"
        assert db.col.find()[1]['rabatt'] == 0.15, "Rabatt-Insert fehlerhaft"
        assert db.col.find()[1]['bio'] == True, "Bio-Insert fehlerhaft"
        assert db.col.find()[1]['img'] == None, "img-Insert fehlerhaft"
        assert db.col.find()[1]['imgsmall'] == None, "imgsmall-Insert fehlerhaft"

    def test_string(self):
        db.delete_many()
        db.insert("Testartikelnummer", "Testprodukt", "Testhersteller", "Testpreis", "Testpfand", "Testkategorie", "Testverfügbar", "Testverkauft", "Testrabatt", "True", "None", "None")

        assert db.artikelnummern_all == ["Testartikelnummer"], "Artikelnummernliste-Insert fehlerhaft"

        assert db.col.find()[0]['artikelnummer'] == "Testartikelnummer", "Artikelnummer-Insert fehlerhaft"
        assert db.col.find()[0]['name'] == "Testprodukt", "Name-Insert fehlerhaft"
        assert db.col.find()[0]['hersteller'] == "Testhersteller", "Hersteller-Insert fehlerhaft"
        assert db.col.find()[0]['preis'] == "Testpreis", "Preis-Insert fehlerhaft"
        assert db.col.find()[0]['pfand'] == "Testpfand", "Pfand-Insert fehlerhaft"
        assert db.col.find()[0]['kategorie'] == "Testkategorie", "Kategorie-Insert fehlerhaft"
        assert db.col.find()[0]['auf_lager'] == "Testverfügbar", "Verfügbar-Insert fehlerhaft"
        assert db.col.find()[0]['verkauft'] == "Testverkauft", "Verkauft-Insert fehlerhaft"
        assert db.col.find()[0]['rabatt'] == "Testrabatt", "Rabatt-Insert fehlerhaft"
        assert db.col.find()[0]['bio'] == "True", "Bio-Insert fehlerhaft"
        assert db.col.find()[0]['img'] == "None", "img-Insert fehlerhaft"
        assert db.col.find()[0]['imgsmall'] == "None", "imgsmall-Insert fehlerhaft"

    def test_many_none(self):
        db.delete_many()
        db.insert(None, None, "Testhersteller", None, 0.25, "Testkategorie", None, 21, 0.15, None, None, None)

        assert db.artikelnummern_all == [None], "Artikelnummernliste-Insert fehlerhaft"

        assert db.col.find()[0]['artikelnummer'] == None, "Artikelnummer-Insert fehlerhaft"
        assert db.col.find()[0]['name'] == None, "Name-Insert fehlerhaft"
        assert db.col.find()[0]['hersteller'] == "Testhersteller", "Hersteller-Insert fehlerhaft"
        assert db.col.find()[0]['preis'] == None, "Preis-Insert fehlerhaft"
        assert db.col.find()[0]['pfand'] == 0.25, "Pfand-Insert fehlerhaft"
        assert db.col.find()[0]['kategorie'] == "Testkategorie", "Kategorie-Insert fehlerhaft"
        assert db.col.find()[0]['auf_lager'] == None, "Verfügbar-Insert fehlerhaft"
        assert db.col.find()[0]['verkauft'] == 21, "Verkauft-Insert fehlerhaft"
        assert db.col.find()[0]['rabatt'] == 0.15, "Rabatt-Insert fehlerhaft"
        assert db.col.find()[0]['bio'] == None, "Bio-Insert fehlerhaft"
        assert db.col.find()[0]['img'] == None, "img-Insert fehlerhaft"
        assert db.col.find()[0]['imgsmall'] == None, "imgsmall-Insert fehlerhaft"

    def test_all_none(self):
        db.delete_many()
        db.insert(None, None, None, None, None, None, None, None, None, None, None, None)

        assert db.artikelnummern_all == [None], "Artikelnummernliste-Insert fehlerhaft"

        assert db.col.find()[0]['artikelnummer'] == None, "Artikelnummer-Insert fehlerhaft"
        assert db.col.find()[0]['name'] == None, "Name-Insert fehlerhaft"
        assert db.col.find()[0]['hersteller'] == None, "Hersteller-Insert fehlerhaft"
        assert db.col.find()[0]['preis'] == None, "Preis-Insert fehlerhaft"
        assert db.col.find()[0]['pfand'] == None, "Pfand-Insert fehlerhaft"
        assert db.col.find()[0]['kategorie'] == None, "Kategorie-Insert fehlerhaft"
        assert db.col.find()[0]['auf_lager'] == None, "Verfügbar-Insert fehlerhaft"
        assert db.col.find()[0]['verkauft'] == None, "Verkauft-Insert fehlerhaft"
        assert db.col.find()[0]['rabatt'] == None, "Rabatt-Insert fehlerhaft"
        assert db.col.find()[0]['bio'] == None, "Bio-Insert fehlerhaft"
        assert db.col.find()[0]['img'] == None, "img-Insert fehlerhaft"
        assert db.col.find()[0]['imgsmall'] == None, "imgsmall-Insert fehlerhaft"


tc_insert = TestCaseInsert()
tc_insert.test_standard()
tc_insert.test_standard_twice()
tc_insert.test_string()
tc_insert.test_many_none()
tc_insert.test_all_none()

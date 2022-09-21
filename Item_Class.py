from main import scanning


class Item:
    def __init__(self, name, price, location, description, satisfaction, type_of_sale):
        self.name = name
        self.price = price
        self.location = location
        self.description = description
        self.satisfaction = satisfaction
        self.type_of_sale = type_of_sale


example_item = Item('Fahrrad Maxim Sevilla Banana 26 Zoll Helm Schloss', 220, '48165 Münster (Westfalen) - Hiltrup',
                    'Hallo, anbei das Fahrrad unseres Sohnes, in einem sehr guten Zustand, da es immer im Keller stand und kaum genutzt wurde. Keine Kratzer. Alles Funktioniert. Mit Helm und Schloss, sofort fahrbereit. NP lag bei 340 Euro.',
                    'TOP', 'Privater Nutzer')
# ELEMENT_TO_SEARCH = Item()
# print(scanning.products[0])

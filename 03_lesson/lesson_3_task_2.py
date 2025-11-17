from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 14", "+79110000001"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79110000002"))
catalog.append(Smartphone("Xiaomi", "Mi 12", "+79110000003"))
catalog.append(Smartphone("Google", "Pixel 7", "+79110000004"))
catalog.append(Smartphone("Nokia", "3310", "+79110000005"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")

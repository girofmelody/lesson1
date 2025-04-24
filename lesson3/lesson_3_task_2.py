from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 14", "+79001234567"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79007654321"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 11", "+79009876543"))
catalog.append(Smartphone("Google", "Pixel 6", "+79003456789"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79004567890"))

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")

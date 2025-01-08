peugeot_208 = {"color": "grise", "fuel": "électrique", "mode": "automatique", "owner": "Valentin", "brand": "Peugeot", "model": "208"}
clio_3 = {"color": "blanche", "fuel": "essence", "mode": "manuelle", "owner": "Maxime", "brand": "Renault", "model": "Clio 3"}

def get_car_string(car: dict) -> str:
    # return f"La {car['brand']} {car['model']} de {car['owner']} est {car['color']}, {car['mode']} et {car['fuel']}."
    return "La {} {} de {} est {}, {} et {}.".format(car['brand'], car['model'], car['owner'], car['color'], car['mode'], car['fuel'])

print(get_car_string(peugeot_208))
print(get_car_string(clio_3))

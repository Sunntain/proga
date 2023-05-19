import json
def z1():
    file = 'products.json'
    try:
        with open(file) as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"products": []}
        product = {}
        product['name'] = input("Введите название продукта: ")
        product['price'] = int(input("Введите цену продукта: "))
        product['available'] = input("Продукт есть в наличии? (да/нет): ").lower() == 'да'
        product['weight'] = int(input("Введите вес продукта: "))
        data['products'].append(product)
    with open(file, 'w') as f:
        json.dump(data, f)
    products = data['products']
    for product in products:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

def z2():
    with open("en-ru.txt", "r") as file:
        lines = file.readlines()
    slovar = {}
    for line in lines:
        key_value = line.strip().split(" - ")
        key = key_value[1]
        values = key_value[0].split(", ")
        slovar[key] = values
    sorted_keys = sorted(slovar.keys())
    sorted_values = []
    for key in sorted_keys:
        values = slovar[key]
        for value in values:
            sorted_values.append(value)
    with open("ru-en.txt", "w") as file:
        for key in sorted_keys:
            values = slovar[key]
            for value in values:
                file.write(key + " - " + value + "\n")

z2()
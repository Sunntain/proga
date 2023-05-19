from PIL import Image, ImageFilter
import os

def z1():
    a = ["1.png","2.png","3.jpg","4.png","5.jpg"]
    k = 0
    for file in a:
        if file.endswith('.jpg') or file.endswith('.png'):
            k += 1
            img = Image.open(file)
            newimg = img.filter(ImageFilter.EMBOSS)
            newimg.show()
            try:
                os.mkdir("C:/Users/эльдо750/Desktop/GBNJY/9")
            except:
                pass
            newimg.save(f"C:/Users/эльдо750/Desktop/GBNJY/9/newimg{k}.png")

def z2():
    r = 0
    with open('ex.csv', 'r') as f:
        lines = f.readlines()
        print("Нужно купить: ")
        for line in lines[1:]:
            product, quantity, price = line.strip().split(',')
            r += int(quantity) * int(price)
            print(f"{product} - {quantity} шт. за {price} руб.")
        print(f"Итоговая сумма: {r} руб.")

z1()
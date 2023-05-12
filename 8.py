from PIL import Image

def z1():
 filename = "postcard.jpg"
 with Image.open(filename) as imgp:
     imgp.load()
 cropp = imgp.crop((380,120,720,420))
 cropp.save("crpostcard.jpg")

def z2():
    dic = {"8 марта":"8m.jpg", "23 февраля":"23f.jpg", "день рождения":"dr.jpg", "день торта":"dt.jpg", "день птиц":"dp.jpg"}
    a = input('какой праздник? ')
    file = dic[a]
    with Image.open(file) as img:
         img.load()
         img.show()

def z3():
    from PIL import Image, ImageDraw, ImageFont

    name = input('введите имя получателя: ')
    file = "postcard.jpg"
    with Image.open(file) as img:
        img.load()
    font = ImageFont.truetype("arial.ttf", 36)
    font2 = ImageFont.truetype("beer-money12.ttf", 40)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img.width // 2, 15),
        name + ", поздравляю!",
        font=font,
        stroke_width=2,
        fill=('red')
    )
    draw_text.text(
        (img.width // 2, img.height // 2 + 200),
        name + ", поздравляю!",
        font=font2,
        stroke_width=2,
        fill=('yellow')
    )
    img.show()
    img.save("newpostcard.png")
    
z3()


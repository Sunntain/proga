from PIL import Image, ImageFilter

def z1():
 filename = "sobaken.jpg"
 with Image.open(filename) as img:
     img.load()
     img.show()
     width, height = img.size
     format = img.format
     mode = img.mode
 print("Ширина: ", width)
 print("Высота:  ", height)
 print("Формат: ", format)
 print("Цветовая модель:", mode)

def z2():
    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()
    new_img = img.resize((img.width // 3, img.height // 3))
    new_img.save("resized_sobaken.jpg")
    newww_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    newww_img.save("fliptombottom.jpg")
    newww_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    newww_img.save("flipleftright.jpg")

def z3():
    filenames = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for i in filenames:
        image = Image.open(i)
        image = image.filter(ImageFilter.EMBOSS)
        image.save("new" + i)

def z4():
    w = "watermark.png"
    with Image.open(w) as imgw:
        imgw.load()
    imgw = Image.open(w)
    imgw = imgw.resize((imgw.width // 2, imgw.height // 2))
    filename = "sobaken.jpg"
    with Image.open(filename) as imgs:
        imgs.load()
    imgs.paste(imgw, [50,50], mask=imgw)
    imgs.save("wsobaken.jpg")


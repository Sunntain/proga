def z1():
    class IceCreamStand:
        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors
        def show_flavors(self):
            print("доступные вкусы мороженого:")
            for flavor in self.flavors:
                print("- " + flavor)
    my_stand = IceCreamStand("мороз", ['ванильное', 'шоколадное', 'клубничное', 'фисташковое'])
    my_stand.show_flavors()

def z2():
    class IceCreamStand:
        def __init__(self, name, flavors, location, working_hours, type_flavors):
            self.name = name
            self.flavors = flavors
            self.location = location
            self.working_hours = working_hours
            self.type_flavors = type_flavors
        def show_flavors(self):
            print("доступные вкусы мороженого:")
            for flavor in self.flavors:
                print("- " + flavor)
        def add_flavor(self, flavor):
            self.flavors.append(flavor)
            print(f'вкус {flavor} добавлен')
        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f'вкус {flavor} удален')
            else:
                print(f'вкус {flavor} не найден в списке')
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f'вкус {flavor} есть в списке')
            else:
                print(f'вкуса {flavor} нет в списке')
        def describe_stand(self):
            print(f"кафе-мороженное {self.name}")
            print(f"место: {self.location}")
            print(f"время работы: {self.working_hours}")
        def show_Typesflavors(self):
            print("доступные типы мороженого:")
            for types in self.type_flavors:
                print("- " + types)
    my_stand = IceCreamStand("мороз 2.0", ['ванильное', 'шоколадное', 'клубничное', 'фисташковое'], 'ленинский проспект 89', '7.00 - 23.00', ['эскимо', 'рожок', 'фруктоввый лед'])
    my_stand.describe_stand()
    my_stand.show_flavors()
    my_stand.show_Typesflavors()
    my_stand.check_flavor("ванильное")
    my_stand.check_flavor("арбузное")
    my_stand.add_flavor("арбузное")
    my_stand.check_flavor("арбузное")
    my_stand.remove_flavor("ванильное")
    my_stand.check_flavor("ванильное")


def z3():
    class IceCreamStand:
        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors
        def get_menu(self):
            menu = "добро пожаловать в" + self.name + "\n"
            menu += "в меню следующие вкусы:\n"
            for flavor in self.flavors:
                menu += "- " + flavor + "\n"
            return menu
    import tkinter as tk
    a = IceCreamStand("мороз 3.0", ["ванильное", "фисташковое", "арбузное"])
    root = tk.Tk()
    root.title("мороз 3.0")
    menu_label = tk.Label(root, text=a.get_menu())
    menu_label.pack()
    root.mainloop()


z1()
z2()
z3()
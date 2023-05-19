def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"ресторан {self.restaurant_name}, {self.cuisine_type} кухня")
        def open_restaurant(self):
            print("ресторан открыт!")
    newRestaurant = Restaurant("юань", "китайская")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"ресторан {self.restaurant_name}, {self.cuisine_type} кухня")
    restaurant1 = Restaurant("тхт", "корейская")
    restaurant2 = Restaurant("мертвый анархист", "европейская")
    restaurant3 = Restaurant("отличный", "вкусная")
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print(f"ресторан {self.restaurant_name}, {self.cuisine_type} кухня")
            print(f"рейтинг ресторана: {self.rating}")
        def update_rating(self, new_rating):
            self.rating = new_rating
    restaurant1 = Restaurant("юань", "китайская", 3.9)
    restaurant1.describe_restaurant()
    restaurant1.update_rating(4.4)
    restaurant1.describe_restaurant()

z3()
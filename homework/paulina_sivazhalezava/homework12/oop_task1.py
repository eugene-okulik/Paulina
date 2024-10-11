class Flowers:
    blooms = True

    def __init__(self, price, blooming_time, freshness, color, stem_length):
        self.price = price
        self.blooming_time = blooming_time
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length

    def __lt__(self, other):
        return ((self.price, self.blooming_time, self.stem_length) <
                (other.price, other.blooming_time, other.stem_length))

    def __gt__(self, other):
        return ((self.price, self.blooming_time, self.stem_length) >
                (other.price, other.blooming_time, other.stem_length))

    def __str__(self):
        if self.freshness == "good":
            return "свежесть цветка хорошая"
        elif self.freshness == "medium":
            return "свежесть цветка средняя"
        else:
            return "свежесть цветка низкая"


class Dianthus(Flowers):
    scent = "Strong"

    def __init__(self, price, blooming_time, freshness, color, stem_length, location, name):
        super().__init__(price, blooming_time, freshness, color, stem_length)
        self.location = location
        self.name = name


class WaterLily(Flowers):

    def __init__(self, price, blooming_time, freshness, color, stem_length, water_required, name):
        super().__init__(price, blooming_time, freshness, color, stem_length)
        self.water_required = water_required
        self.name = name


class Lavender(Flowers):

    def __init__(self, price, blooming_time, freshness, color, stem_length, years_of_growing, name):
        super().__init__(price, blooming_time, freshness, color, stem_length)
        self.years_of_growing = years_of_growing
        self.name = name


dianthus_chinese = Dianthus(10, 30, "good", "red", 25, "China", "Dianthus Chinese")
dianthus_wild = Dianthus(5, 8, "medium", "white", 15, "Belarus", "Dianthus Wild")
lotus = WaterLily(45, 60, "low", "violet", 45, "20 l", "Lotus")
lavender_french = Lavender(18, 14, "good", "lavender", 20, 5, "French Lavender")


class Bouquet:
    def __init__(self):
        self.flowers_in_bouquet = []

    def add_flower(self, flower):
        self.flowers_in_bouquet.append(flower)

    def bouquet_price(self):
        return sum(flower.price for flower in self.flowers_in_bouquet)

    def bouquet_blooms(self):
        return int(sum(flower.blooming_time for flower in self.flowers_in_bouquet) / len(self.flowers_in_bouquet))

    def find_flower_color(self):
        enter_color = input('Введите цвет на английском языке: ')
        found_flowers = [flower for flower in self.flowers_in_bouquet if flower.color == enter_color]
        if found_flowers:
            return found_flowers
        else:
            print("Цветов такого цвета нет в букете.")
            return None


my_bouquet = Bouquet()
my_bouquet.add_flower(dianthus_chinese)
my_bouquet.add_flower(dianthus_wild)
my_bouquet.add_flower(lotus)
my_bouquet.add_flower(lavender_french)

print(f"Стоимость букета: {my_bouquet.bouquet_price()} USD")
print(f"Время увядания: {my_bouquet.bouquet_blooms()} дней")
print(lotus.price > lavender_french.price)
print(dianthus_chinese.blooming_time < dianthus_wild.blooming_time)
print(dianthus_chinese)
print(lotus)

display_found_flowers = my_bouquet.find_flower_color()
if display_found_flowers is not None:
    for display_flower in display_found_flowers:
        print(f"Найден цветок: {display_flower.name}, Цвет: {display_flower.color}, Цена: {display_flower.price}")

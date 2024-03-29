def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
pass

def get_spiciest_foods(spicy_foods):
    max_heat_level = max(food["heat_level"] for food in spicy_foods)
    return [food for food in spicy_foods if food["heat_level"] == max_heat_level]
pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} - Cuisine: {food['cuisine']} - Heat Level: {food['heat_level']}")
pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food for food in spicy_foods if food["cuisine"] == cuisine]
pass

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
pass

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    return total_heat_level / len(spicy_foods)
pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
pass

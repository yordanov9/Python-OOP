class PizzaDelivery:

    def __init__(self, name, price, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and, we can't make any changes!"

        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0

        self.ingredients[ingredient] += quantity
        self.price += ingredient_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
        if self.ingredients[ingredient] < quantity:
            return f'Please check again the desired quantity of {ingredient}!'

        self.ingredients[ingredient] -= quantity
        self.price -= ingredient_price

    def make_order(self):
        ingredients_list = [f'{ingredient}: {quantity}' for ingredient, quantity in self.ingredients.items()]
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join(ingredients_list)} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('cheese', 1, 2)
margarita.add_extra('mozzarella', 1, 2.5)
margarita.remove_ingredient('bacon', 1, 5)
print(margarita.remove_ingredient('tomatoes', 2, 2))
print(margarita.remove_ingredient('tomatoes', 1, 2))
print(margarita.make_order())
print(margarita.add_extra('mozzarella', 1, 2))

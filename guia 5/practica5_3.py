# exercise 4

recipes = [
    {'recipe': 'Arroz con Verduras', 'ingredients': ['arroz', 'cebolla', 'morron', 'zanahoria', 'castañas', 'zuchini']},
    {'recipe': 'Ensalada de Quinoa', 'ingredients': ['quinoa', 'huevo', 'cebolla morada', 'tomate', 'morron', 'almendras']},
    {'recipe': 'Carne al Horno', 'ingredients': ['colita', 'papa', 'zanahoria', 'batata', 'cebolla', 'ajo']},
    {'recipe': 'Fideos al Pesto', 'ingredients': ['fideos', 'queso', 'nueces', 'albahaca', 'ajo', 'aceite de oliva']},
    {'recipe': 'Guiso de Lentejas', 'ingredients': ['lentejas', 'cebolla', 'zanahoria', 'papa', 'carne', 'puerro', 'morron']},
]
ingredients = []


def recipe_recommender():
    recommended_recipe = []

    for input_ingredient in ingredients:
        for recipe_dict in recipes:
            for input_ingredients in recipe_dict['ingredients']:
                if recipe_dict not in recommended_recipe:
                    recommended_recipe.append(recipe_dict)
                #  print(recipe_dict["recipe"])
    return recommended_recipe


def main_menu():
    print("\n @@@@@@@@@@@@@@@@@@@")
    print("  ¿Qué cocino hoy?")
    print("@@@@@@@@@@@@@@@@@@@@\n")

    while True:
        print("\t 1) Agregar Ingrediente \n\t 2) Buscar Receta \n\t 3) A Cocinar")
        option = input(">>")
        if option == "1":
            ingredient = input("\t Ingrediente >> ")
            ingredients.append(ingredient)
        elif option == "2":
            if len(ingredients) >= 2:
                recipe = recipe_recommender()
                print(f"Receta: {recipe}")
            else:
                print("Debe ingresar al menos dos ingredientes")
        elif option == "3":
            break
        else:
            print("Opción Inválida")


main_menu()

#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = None
    can_produce = True

    for key in recipe:
        print(f'{key} requires {recipe[key]}')
        if key in ingredients:
            print(f'{key} on hand {ingredients[key]}')
            new_batches = ingredients[key] // recipe[key]
            print(f'{new_batches} batches possible')
            if new_batches == 0:
                print(f'Not enough {key} to make a single batch')
            elif batches is None and new_batches > 0:
                batches = new_batches
            elif new_batches < batches:
                batches = new_batches

        else:
            print(f'{key} ingredient not found')
            batches = 0
            return batches
    return batches


# recipe = {'milk': 100, 'butter': 50, 'cheese': 10}
# ingredients = {'milk': 198, 'butter': 52, 'cheese': 10}
# recipe_batches(recipe, ingredients)

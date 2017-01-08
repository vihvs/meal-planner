from collections import defaultdict

import requests
import tablib
from decouple import config
from yaml import load, Loader

token = config('TOKEN')
key = config('KEY')
list_id = config('LIST_ID')
trello_endpoint = 'https://api.trello.com/1'
list_cards_endpoint = '/lists/%s/cards/open' % list_id
auth_params = {'key': key, 'token': token}

recipes_cards = requests.get(trello_endpoint + list_cards_endpoint, auth_params).json()
recipes = [load(recipe['desc'][4:-4], Loader=Loader) for recipe in recipes_cards]

shopping_list = defaultdict(float)

for recipe in recipes:
    for ingredient in recipe['ingredients']:
        shopping_list[ingredient['name']] += ingredient['quantity']

headers = ('ingredient', 'Quantity')
csv_list = tablib.Dataset(*shopping_list.items(), headers=headers).csv

print(csv_list)

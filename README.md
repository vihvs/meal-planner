Meal Planner: Tools to help planning weekly meals
=================================================

### Overview
Python tools to help automate some tasks for plan the weekly meal

### Shopping list

We need to generate a shopping list of all ingredients needed for all the meals for that week. To do this we use a [Trello](https://trello.com>) board and some conventions.

#### Trello conventions
- Have a board with a list of cards for each recipe you want
- Each recipe card must use a YAML description of the recipe also inside ``` to make easy to read:

Example:
```
    ```
name: Strogonoff
ingredients:
    - name        : Filet
      quantity    : 0.3
      unit        : kg
    - name        : Mushrooms
      quantity    : 0.1
      unit        : kg
portions: 2
prep-time: 30min
steps:
    - Do this
    - then do that
    - and finish with this
    ```
```

#### Trello API tips
To use this you first need Trello key and token. The easiest way is just go to: https://trello.com/app-key and follow the instructions.

To get the `LIST_ID` just open the Chrome dev tools, inspect the network while change the list name.

#### How to use
* `pip install -r requirements.txt`
* Create a settings.ini file.
Example:
```
[settings]
TOKEN=<YOUR TRELLO USER TOKEN>
KEY=<YOUR TRELLO KEY>
LIST_ID=<YOUR LIST ID WITH RECIPES>
```
* `python shopping-list.py > list.csv`

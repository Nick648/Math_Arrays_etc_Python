import json


def write_json(data_dict: dict[list], file_name: str) -> None:
    with open(file=file_name, mode="w", encoding="utf-8") as json_file:
        json.dump(data_dict, json_file, ensure_ascii=False, indent=4)


def load_json() -> dict:
    with open(file='cocktails_ingredient.json', mode="r", encoding="utf-8") as json_file:
        cocktails = json.load(json_file)
    return cocktails


def manual_split(input_str: str, input_data: str = None) -> tuple[str, int, str]:
    while True:
        if input_data:
            splits = input_data.split()
        else:
            splits = input(input_str).split()
        if len(splits) < 3:
            return splits[0], 0, ''
        try:
            name_split = " ".join(splits[:-2]).strip().title()
            amount_split = int(splits[-2].strip())
            dimension_split = splits[-1].strip().lower()
            return name_split, amount_split, dimension_split
        except Exception as _:
            input_data = None
            print('ERROR TRY AGAIN!')


def manual_input() -> dict:
    cocktails = {}
    while True:
        name = input(f'{"-" * 50}\nName cocktail: ')
        if not name:
            print('Cocktails create!')
            break
        ingredients = {}
        total_volume = 0
        while True:
            ingredient = input('Ingredient (name amount dimension) >>> ')
            if not ingredient:
                print('Ingredients create!')
                break
            name_ingredient, amount_ingredient, dimension_ingredient = \
                manual_split('Ingredient (name amount dimension) >>> ', ingredient)
            ingredients[name_ingredient] = {"amount": 0, "dimension": '-'}
            ingredients[name_ingredient]["amount"] = amount_ingredient
            ingredients[name_ingredient]["dimension"] = dimension_ingredient
            total_volume += amount_ingredient
            # ingredients.append([name_ingredient, amount, dimension])
        cocktails[name] = ingredients
        cocktails[name]['Tableware'] = [manual_split('Tableware: ')]
        cocktails[name]['Decoration'] = [manual_split('Decoration: ')]
        cocktails[name]['Category'] = input('Category: ').strip().title()
        cocktails[name]['Volume'] = total_volume

    return cocktails


def get_total_info(data: dict) -> dict:
    total_info = {'Total count': len(data), 'Ingredients Count': {}, 'Decoration Count': {}, 'Tableware Count': {},
                  'Category Count': {}, 'Volume Count': 0}
    for cocktail_name, specifications in data.items():
        for key in specifications.keys():
            if key == 'Tableware':
                tableware, count, dim = specifications[key][0]
                if tableware in total_info['Tableware Count']:
                    total_info['Tableware Count'][tableware] += count
                else:
                    total_info['Tableware Count'][tableware] = count
            elif key == 'Decoration':
                decoration, count, dim = specifications[key][0]
                if decoration in total_info['Decoration Count']:
                    total_info['Decoration Count'][decoration] += count
                else:
                    total_info['Decoration Count'][decoration] = count
            elif key == 'Category':
                category = specifications[key]
                if category in total_info['Category Count']:
                    total_info['Category Count'][category] += 1
                else:
                    total_info['Category Count'][category] = 1
            elif key == 'Volume':
                total_info['Volume Count'] += specifications[key]
            else:
                amount, dim = specifications[key]['amount'], specifications[key]['dimension']
                if key in total_info['Ingredients Count'] and total_info['Ingredients Count'][key]['dimension'] == dim:
                    total_info['Ingredients Count'][key]['amount'] += amount
                elif key in total_info['Ingredients Count']:
                    total_info['Ingredients Count'][f'{key}-1'] = {'amount': 0, 'dimension': ''}
                    total_info['Ingredients Count'][f'{key}-1']['amount'] = amount
                    total_info['Ingredients Count'][f'{key}-1']['dimension'] = dim
                else:
                    total_info['Ingredients Count'][key] = {'amount': 0, 'dimension': ''}
                    total_info['Ingredients Count'][key]['amount'] = amount
                    total_info['Ingredients Count'][key]['dimension'] = dim
    return total_info


def main() -> None:
    # data = manual_input()
    # write_json(data_dict=data, file='cocktails_ingredient.json')
    data_json = load_json()
    # print(data_json)
    total_info = get_total_info(data_json)
    write_json(data_dict=total_info, file_name='total_info_cocktails.json')


if __name__ == '__main__':
    main()

"""
{
    "Шот лимон": {
        "Лимончелло": {
            "amount": 30,
            "dimension": "мл"
        },
        "Водка": {
            "amount": 50,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 30,
            "dimension": "мл"
        },
        "Сахар": {
            "amount": 40,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Шот",
                4,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Сахар Оконтовка",
                4,
                "шт"
            ]
        ],
        "Category": "Шот",
        "Volume": 150
    },
    "Почти Меган": {
        "Джин": {
            "amount": 40,
            "dimension": "мл"
        },
        "Мартини Фиеро": {
            "amount": 25,
            "dimension": "мл"
        },
        "Трипл Сек": {
            "amount": 25,
            "dimension": "мл"
        },
        "Сироп Малина": {
            "amount": 40,
            "dimension": "мл"
        },
        "Вода": {
            "amount": 20,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Шот",
                4,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Виноград",
                4,
                "шт"
            ]
        ],
        "Category": "Шот",
        "Volume": 150
    },
    "Винсент ": {
        "Абсент": {
            "amount": 50,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 50,
            "dimension": "мл"
        },
        "Сироп Банан": {
            "amount": 50,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Шот",
                4,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Вейдж Яблока",
                4,
                "шт"
            ]
        ],
        "Category": "Шот",
        "Volume": 150
    },
    "Мармеладный дайкири": {
        "Ром": {
            "amount": 50,
            "dimension": "мл"
        },
        "Трипл Сек": {
            "amount": 30,
            "dimension": "мл"
        },
        "Мартини Бьянко": {
            "amount": 20,
            "dimension": "мл"
        },
        "Сироп (Киви)": {
            "amount": 30,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 20,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Шот",
                4,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Мармеладка",
                4,
                "шт"
            ]
        ],
        "Category": "Шот",
        "Volume": 150
    },
    "Мадам Маракуйбл": {
        "Виски": {
            "amount": 50,
            "dimension": "мл"
        },
        "Апельсиновый Сок": {
            "amount": 50,
            "dimension": "мл"
        },
        "Сироп Маракуйя": {
            "amount": 30,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 20,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Шот",
                4,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Мята",
                4,
                "шт"
            ]
        ],
        "Category": "Шот",
        "Volume": 150
    },
    "Апельсиновый мохито Б/А": {
        "Лайм": {
            "amount": 1,
            "dimension": "шт"
        },
        "Апельсин": {
            "amount": 1,
            "dimension": "шт"
        },
        "Мята": {
            "amount": 1,
            "dimension": "шт"
        },
        "Сок Лайма": {
            "amount": 30,
            "dimension": "мл"
        },
        "Сироп Мохито": {
            "amount": 30,
            "dimension": "мл"
        },
        "Апельсиновый Сок": {
            "amount": 60,
            "dimension": "мл"
        },
        "Содовая": {
            "amount": 120,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 300 мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Мята+Лайм",
                1,
                "шт"
            ]
        ],
        "Category": "Б/А",
        "Volume": 243
    },
    "Мятный смузи": {
        "Мята": {
            "amount": 5,
            "dimension": "гр"
        },
        "Персиковый Сок": {
            "amount": 240,
            "dimension": "мл"
        },
        "Сироп Маракуйя": {
            "amount": 40,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 40,
            "dimension": "мл"
        },
        "Банан": {
            "amount": 1,
            "dimension": "шт"
        },
        "Tableware": [
            [
                "Бокал 500 мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Мята",
                1,
                "шт"
            ]
        ],
        "Category": "Б/А",
        "Volume": 326
    },
    "Клубничный лимонад": {
        "Клубника Замороженная": {
            "amount": 70,
            "dimension": "гр"
        },
        "Сироп Клубника": {
            "amount": 20,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 20,
            "dimension": "мл"
        },
        "Содовая": {
            "amount": 120,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 200 мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Клубника",
                1,
                "шт"
            ]
        ],
        "Category": "Б/А",
        "Volume": 230
    },
    "О, ситро!": {
        "Сироп (Мандарин)": {
            "amount": 40,
            "dimension": "мл"
        },
        "Вода": {
            "amount": 20,
            "dimension": "мл"
        },
        "Апельсиновый Сок": {
            "amount": 30,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 10,
            "dimension": "мл"
        },
        "Содовая": {
            "amount": 100,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 200 мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Лайм",
                1,
                "шт"
            ]
        ],
        "Category": "Б/А",
        "Volume": 200
    },
     "Апельсиновый мохито ": {
        "Лайм": {
            "amount": 1,
            "dimension": "шт"
        },
        "Апельсин": {
            "amount": 1,
            "dimension": "шт"
        },
        "Мята": {
            "amount": 1,
            "dimension": "шт"
        },
        "Сок Лайма": {
            "amount": 30,
            "dimension": "мл"
        },
        "Сироп Мохито": {
            "amount": 30,
            "dimension": "мл"
        },
        "Ром": {
            "amount": 120,
            "dimension": "мл"
        },
        "Апельсиновый Сок": {
            "amount": 60,
            "dimension": "мл"
        },
        "Содовая": {
            "amount": 120,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 500 Мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Апельсин",
                1,
                "шт"
            ]
        ],
        "Category": "Лонг",
        "Volume": 363
    },
    "Клубничная маргарита ": {
        "Текила": {
            "amount": 40,
            "dimension": "мл"
        },
        "Трипл Сек": {
            "amount": 30,
            "dimension": "мл"
        },
        "Клубника Замороженная": {
            "amount": 70,
            "dimension": "гр"
        },
        "Сироп Клубника": {
            "amount": 20,
            "dimension": "мл"
        },
        "Вода": {
            "amount": 20,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 20,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 300 Мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Клубника",
                1,
                "шт"
            ]
        ],
        "Category": "Лонг",
        "Volume": 200
    },
    "Апероль Спритц": {
        "Апероль": {
            "amount": 60,
            "dimension": "мл"
        },
        "Игристрое Брют": {
            "amount": 60,
            "dimension": "мл"
        },
        "Содовая": {
            "amount": 80,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 200 Мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Апельсин",
                1,
                "шт"
            ]
        ],
        "Category": "Лонг",
        "Volume": 200
    },
    "Лонг-Айленд": {
        "Водка": {
            "amount": 25,
            "dimension": "мл"
        },
        "Ром": {
            "amount": 25,
            "dimension": "мл"
        },
        "Текила": {
            "amount": 25,
            "dimension": "мл"
        },
        "Джин": {
            "amount": 25,
            "dimension": "мл"
        },
        "Трипл Сек": {
            "amount": 25,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 25,
            "dimension": "мл"
        },
        "Сахар": {
            "amount": 25,
            "dimension": "мл"
        },
        "Кола": {
            "amount": 125,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 300 Мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Апельсин",
                1,
                "шт"
            ]
        ],
        "Category": "Лонг",
        "Volume": 300
    },
    "Корбен Даллас": {
        "Виски": {
            "amount": 40,
            "dimension": "мл"
        },
        "Фиеро": {
            "amount": 60,
            "dimension": "мл"
        },
        "Сироп Малина": {
            "amount": 30,
            "dimension": "мл"
        },
        "Апельсиновый Сок": {
            "amount": 50,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 20,
            "dimension": "мл"
        },
        "Тоник": {
            "amount": 100,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 300 Мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Апельсин",
                1,
                "шт"
            ]
        ],
        "Category": "Лонг",
        "Volume": 300
    },
    "Виски Гамми": {
        "Виски": {
            "amount": 100,
            "dimension": "мл"
        },
        "Персиковый Сок": {
            "amount": 100,
            "dimension": "мл"
        },
        "Сироп Маракуйя": {
            "amount": 20,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 20,
            "dimension": "мл"
        },
        "Тоник": {
            "amount": 60,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 300 Мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Лимон Вейдж",
                1,
                "шт"
            ]
        ],
        "Category": "Лонг",
        "Volume": 300
    },
    "Пэшн Джин Тоник": {
        "Джин": {
            "amount": 80,
            "dimension": "мл"
        },
        "Апельсиновый Сок": {
            "amount": 50,
            "dimension": "мл"
        },
        "Сироп Маракуйя": {
            "amount": 30,
            "dimension": "мл"
        },
        "Тоник": {
            "amount": 140,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 300 Мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Апельсин Вейдж",
                1,
                "шт"
            ]
        ],
        "Category": "Лонг",
        "Volume": 300
    },
    "Клякса": {
        "Джин": {
            "amount": 40,
            "dimension": "мл"
        },
        "Водка": {
            "amount": 40,
            "dimension": "мл"
        },
        "Люкер Блю Кюрасао": {
            "amount": 30,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 50,
            "dimension": "мл"
        },
        "Тоник": {
            "amount": 120,
            "dimension": "мл"
        },
        "Гренадин": {
            "amount": 20,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 300 Мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Лимон Вейдж",
                1,
                "шт"
            ]
        ],
        "Category": "Лонг",
        "Volume": 300
    },
    "Мартини Фиеро Тоник": {
        "Мартини Фиеро": {
            "amount": 70,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 10,
            "dimension": "мл"
        },
        "Тоник": {
            "amount": 70,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 200 Мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Апельсин Кольцо",
                1,
                "шт"
            ]
        ],
        "Category": "Лонг",
        "Volume": 150
    },
    "Мартини Бьянко Тоник": {
        "Мартини Бьянко": {
            "amount": 70,
            "dimension": "мл"
        },
        "Лимонный Сок": {
            "amount": 10,
            "dimension": "мл"
        },
        "Тоник": {
            "amount": 70,
            "dimension": "мл"
        },
        "Tableware": [
            [
                "Бокал 200 Мл",
                1,
                "шт"
            ]
        ],
        "Decoration": [
            [
                "Лимон Кольцо",
                1,
                "шт"
            ]
        ],
        "Category": "Лонг",
        "Volume": 150
    }
}
"""

import json

questions = {"Транспорт": {"100": {"question": "plane", "answer": "самолет", "asked": False},
                           "200": {"question": "train", "answer": "поезд", "asked": False},
                           "300": {"question": "car", "answer": "автомобиль", "asked": False}},
             "Животные": {"100": {"question": "dog", "answer": "собака", "asked": False},
                         "200": {"question": "shark", "answer": "акула", "asked": False},
                         "300": {"question": "sparrow", "answer": "воробей", "asked": False}},
             "Еда": {"100": {"question": "apple", "answer": "яблоко", "asked": False},
                     "200": {"question": "banana", "answer": "банан", "asked": False},
                     "300": {"question": "orange", "answer": "апельсин", "asked": False}}
             }

with open("questions.json", "w") as file:
    json.dump(questions, file, ensure_ascii=False)

def show_field(questions):
    for category, bet in questions.items():
        print(category.ljust(10), end='\t')
        for key, value in bet.items():
            if value['asked']:
                print(' '.ljust(6), end='\t')
            else:
                print(key.ljust(6), end='\t')
        print()

def parse_input():
    category, bet = input("Вопрос и ставка: ").split()
    return (category.title(), bet)

def show_question(questions, category: str, bet: str):
    if category not in questions:
        print("Такого вопроса нет. Попробуйте еще раз")
        return False
    elif bet not in questions[category]:
        print("Такого вопроса нет. Попробуйте еще раз")
        return False
    elif questions[category][bet]['asked']:
        print("Такого вопроса нет. Попробуйте еще раз")
        return False
    else:
        print(f"Слово {questions[category][bet]['question']} в переводе означает")
        return True

def show_stats(stats):
    print("Ваш счет: ", stats['points'])
    print("Верных ответов: ", stats['correct'])
    print("Неверных ответов: ", stats['incorect'])


def load_questions():
    with open("questions.json", "r") as file:
        questions = json.load(file)
    stats = {'points': 0, 'correct': 0, 'incorect': 0}
    questions_count = 0
    for value in questions.values():
        for item in value.values():
            if item['asked'] is False:
                questions_count += 1
    while questions_count > 0:
        show_field(questions)
        category, bet = parse_input()
        flag = show_question(questions, category, bet)
        while not flag:
            category, bet = parse_input()
            flag = show_question(questions, category, bet)
        answer = input("Ваш ответ: ").lower()
        if answer == questions[category][bet]['answer']:
            questions[category][bet]['asked'] = True
            stats['points'] += int(bet)
            stats['correct'] += 1
            print(f"Верно! +{bet}. Ваш счет: {stats['points']}")
        else:
            questions[category][bet]['asked'] = True
            stats['points'] -= int(bet)
            stats['incorect'] += 1
            print(f"Неверно! -{bet}. Ваш счет: {stats['points']}")
        questions_count -= 1
    print("Вопросы закончились!")
    show_stats(stats)

load_questions()
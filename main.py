import file_operations
import random
from faker import Faker
from pathlib import Path


def replacement_for_runic_font_skill(replace_skill: str):
    letter_mapping = {
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠', 'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠', 'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
        'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋', 'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒', 'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
        'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠', 'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋', 'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
        'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋', 'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋', 'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
        'Г': "Г͒͠", 'Д': 'Д̋', 'Е': 'Е', 'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠', 'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
        'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒', 'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠', 'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
        'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋', 'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋', 'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋', ' ': ' '
    }
    for letter in replace_skill:
        ancient_letter = letter_mapping[letter]
        replace_skill = replace_skill.replace(letter, ancient_letter)
    return replace_skill


def create_profile():
    skills = {'Стремительный прыжок', 'Электрический выстрел', 'Ледяной удар', 'Стремительный удар', 'Кислотный взгляд',
              'Тайный побег', 'Ледяной выстрел', 'Огненный заряд'}

    runic_skills = []
    for skill in skills:
        runic_skills.append(replacement_for_runic_font_skill(skill))
    unique_skills = random.sample(runic_skills, 3)

    fake = Faker('ru_RU')
    context = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": random.randint(8, 14),
        "agility": random.randint(8, 14),
        "endurance": random.randint(8, 14),
        "intelligence": random.randint(8, 14),
        "luck": random.randint(8, 14),
        "skill_1": unique_skills[0],
        "skill_2": unique_skills[1],
        "skill_3": unique_skills[2]
    }
    return context


for number in range(1, 11, 1):
    context_profile = create_profile()
    if not Path.is_dir(Path.cwd() / 'output'):
        Path.mkdir(Path.cwd() / 'output')
    file_operations.render_template('src/template.svg', 'output/charsheet-{}.svg'.format(number), context_profile)

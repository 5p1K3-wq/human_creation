import file_operations
import random
import os
from faker import Faker
from pathlib import Path

CHARACTER_INITIAL_CHARACTERIZATION = 8
CHARACTER_FINAL_CHARACTERIZATION = 14


def replace_with_runic_font():
    skills = {'Стремительный прыжок', 'Электрический выстрел', 'Ледяной удар', 'Стремительный удар', 'Кислотный взгляд',
              'Тайный побег', 'Ледяной выстрел', 'Огненный заряд'}

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

    replace_runic_skills = []
    for skill in skills:
        for letter in skill:
            ancient_letter = letter_mapping[letter]
            skill = skill.replace(letter, ancient_letter)
        replace_runic_skills.append(skill)

    return replace_runic_skills


def create_profile(unique_skills):
    fake = Faker('ru_RU')
    context = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": random.randint(CHARACTER_INITIAL_CHARACTERIZATION, CHARACTER_FINAL_CHARACTERIZATION),
        "agility": random.randint(CHARACTER_INITIAL_CHARACTERIZATION, CHARACTER_FINAL_CHARACTERIZATION),
        "endurance": random.randint(CHARACTER_INITIAL_CHARACTERIZATION, CHARACTER_FINAL_CHARACTERIZATION),
        "intelligence": random.randint(CHARACTER_INITIAL_CHARACTERIZATION, CHARACTER_FINAL_CHARACTERIZATION),
        "luck": random.randint(CHARACTER_INITIAL_CHARACTERIZATION, CHARACTER_FINAL_CHARACTERIZATION),
        "skill_1": unique_skills[0],
        "skill_2": unique_skills[1],
        "skill_3": unique_skills[2]
    }
    return context


def main():
    runic_skills = replace_with_runic_font()
    path_directory_new_profiles = Path.cwd() / r'output'
    os.makedirs(path_directory_new_profiles, exist_ok=True)
    for number in range(1, 11, 1):
        unique_skills = random.sample(runic_skills, 3)
        context_profile = create_profile(unique_skills)
        file_operations.render_template('src/template.svg', 'output/charsheet-{}.svg'.format(number), context_profile)


if __name__ == '__main__':
    main()

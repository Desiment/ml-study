class Categories:
    TECH_SCIENCE = 0
    NATURAL_SCIENCE = 1
    SOCIETY_SCIENCE = 2
    LANGUAGE_SCIENCE = 3
    HUMANITARIAN_SCIENCE = 4
    OTHER_SCIENCE = 5
    MULTI_SCIENCE = 6
    UNDEFINED = -1

    CATEGORY_NAMES = (
        'TECH',
        'NATURAL',
        'SOCIETY',
        'LANGUAGE',
        'HUMANITARIAN',
        'OTHER',
        'MULTI',
        'UNDEFINED'
    )

    SUBJECTS = {
        'астрономия': TECH_SCIENCE,
        'Физика': TECH_SCIENCE,
        'Информатика': TECH_SCIENCE,
        'Математика': TECH_SCIENCE,
        'Информатика и Информационно-коммуникационные технологии (ИКТ)': TECH_SCIENCE,
        'Биология': NATURAL_SCIENCE,
        'География': NATURAL_SCIENCE,
        'Химия': NATURAL_SCIENCE,
        'Экология': NATURAL_SCIENCE,
        'Изобразительное искусство': SOCIETY_SCIENCE,
        'История': SOCIETY_SCIENCE,
        'Мировая Художественная Культура (МХК)': SOCIETY_SCIENCE,
        'Обществознание': SOCIETY_SCIENCE,
        'Право': SOCIETY_SCIENCE,
        'Экономика': SOCIETY_SCIENCE,
        'Искусство (МХК)': SOCIETY_SCIENCE,
        'Бюджетная грамотность': SOCIETY_SCIENCE,
        'Иностранный язык (французский язык)': LANGUAGE_SCIENCE,
        'Иностранный язык (итальянский язык)': LANGUAGE_SCIENCE,
        'Иностранный язык (китайский язык)': LANGUAGE_SCIENCE,
        'Иностранный язык (английский язык)': LANGUAGE_SCIENCE,
        'Иностранный язык (испанский язык)': LANGUAGE_SCIENCE,
        'Иностранный язык (немецкий язык)': LANGUAGE_SCIENCE,
        'Латынь': LANGUAGE_SCIENCE,
        'филология': HUMANITARIAN_SCIENCE,
        'Русский язык': HUMANITARIAN_SCIENCE,
        'Литература': HUMANITARIAN_SCIENCE,
        'лингвистика': HUMANITARIAN_SCIENCE,
        'Технология': OTHER_SCIENCE,
        'Основы безопасности жизнедеятельности': OTHER_SCIENCE,
        'Физическая культура': OTHER_SCIENCE,
        'Робототехника': OTHER_SCIENCE,
        'Информационные технологии в профессиональной деятельности': OTHER_SCIENCE
    }

    @staticmethod
    def name_by_id(id):
        return Categories.CATEGORY_NAMES[id]

    @staticmethod
    def categories_amount():
        return len(Categories.CATEGORY_NAMES) - 1

    @staticmethod
    def get_profile_by_subject(name):
        if name in Categories.SUBJECTS:
            return Categories.SUBJECTS[name]
        else:
            return -1

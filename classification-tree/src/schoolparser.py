import csv

from categories import Categories


class Parser:
    FILENAME = '../data/schools.csv'

    def __init__(self):
        pass

    def get_data(self, name):
        res = [0] * (Categories.categories_amount() + 1)
        with open(self.FILENAME) as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['FullName'] == name or row['ShortName'] == name:
                    res[Categories.get_profile_by_subject(row['Subject'])] += 1
        return res

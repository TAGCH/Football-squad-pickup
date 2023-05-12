from csv import DictReader
import csv
import string

class MySquadManagement:
    def LoadMySquad():
        with open('players_22.csv', encoding="utf-8") as data_file:
            data = csv.DictReader(data_file)
            Res = []
            for row in data:
                Res.append(row)

        return Res
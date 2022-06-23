import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class leitura_arquivo:
    @classmethod
    def arquivo_csv(cls, path):
        data = []
        with open(path) as arquivo:
            jobs_reader = csv.DictReader(arquivo, delimiter=",", quotechar='"')
            for row in jobs_reader:
                data.append(row)
        arquivo.close()
        return data

    @classmethod
    def arquivo_json(cls, path):
        with open(path) as arquivo:
            data = json.load(arquivo)
        return data


class Inventory:

    list

    @classmethod
    def import_data(cls, path, report):
        if ".csv" in path:
            cls.list = leitura_arquivo.arquivo_csv(path)

        if ".json" in path:
            cls.list = leitura_arquivo.arquivo_json(path)

        if report == "simples":
            return SimpleReport.generate(cls.list)
        else:
            return CompleteReport.generate(cls.list)

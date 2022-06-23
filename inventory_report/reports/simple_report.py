from datetime import date


class SimpleReport:
    @classmethod
    def generate(cls, list):
        validade = []
        data_atual = date.today().isoformat()
        fabricacao = []
        contagem_produtos = dict()
        for product in list:
            if product["data_de_validade"] >= data_atual:
                validade.append(product["data_de_validade"])
            if product["nome_da_empresa"] not in contagem_produtos:
                contagem_produtos[product["nome_da_empresa"]] = 1
            else:
                contagem_produtos[product["nome_da_empresa"]] += 1
            fabricacao.append(product["data_de_fabricacao"])
        empresa_com_mais_produtos = max(
            contagem_produtos, key=lambda item: contagem_produtos[item]
        )
        return (
            f"Data de fabricação mais antiga: {min(fabricacao)}\n"
            f"Data de validade mais próxima: {min(validade)}\n"
            f"Empresa com mais produtos: {empresa_com_mais_produtos}"
        )

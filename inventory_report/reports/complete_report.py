from collections import Counter


class CompleteReport:
    def generate(products):
        fabricacao = list()
        validade = list()
        empresa = list()

        for prod in products:
            fabricacao.append(prod["data_de_fabricacao"])
            validade.append(prod["data_de_validade"])
            empresa.append(prod["nome_da_empresa"])

        empresa = Counter(empresa)
        empresa_com_mais_produtos = empresa.most_common(1)[0][0]
        fabricacao_mais_antiga = min(fabricacao)
        validade_mais_recente = min(validade)

        estoque_empresa = ""
        for empresa, quantidade in empresa.items():
            estoque_empresa += f"- {empresa}: {quantidade}\n"

        return (
            f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_recente}\n"
            f"Empresa com mais produtos: {empresa_com_mais_produtos}\n"
            f"Produtos estocados por empresa:\n"
            f"{estoque_empresa}"
        )

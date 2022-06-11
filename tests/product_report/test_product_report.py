from inventory_report.inventory.product import Product


def data_products(param):
    return (
        f"O produto {param.nome_do_produto}"
        f" fabricado em {param.data_de_fabricacao}"
        f" por {param.nome_da_empresa} com validade"
        f" até {param.data_de_validade}"
        f" precisa ser armazenado {param.instrucoes_de_armazenamento}."
    )


def test_relatorio_produto():
    product = Product(
        1,
        "teste01",
        "empresa01",
        "09/06/2022",
        "09/06/2023",
        "KLRDB62QZP",
        "Armazenar em nuvem",
    )

    assert str(product) == data_products(product)

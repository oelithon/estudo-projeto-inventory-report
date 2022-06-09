from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        1,
        "teste01",
        "empresa01",
        "09/06/2022",
        "09/06/2023",
        "KLRDB62QZP",
        "Armazenar em local núvem",
    )
    assert new_product.id == 1
    assert new_product.nome_do_produto == "teste01"
    assert new_product.nome_da_empresa == "empresa01"
    assert new_product.data_de_fabricacao == "09/06/2022"
    assert new_product.data_de_validade == "09/06/2023"
    assert new_product.numero_de_serie == "KLRDB62QZP"
    assert new_product.instrucoes_de_armazenamento == "Armazenar em local núvem"
